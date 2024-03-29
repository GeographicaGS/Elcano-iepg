app.view.tools.ComparisonPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#comparison_tool_template').html() ),

    _templateHelp : _.template( $('#comparison_tool_help_template').html() ),
    // Force fetch data of the left tool. Get the data for the first country
    _forceFetchDataSubToolLeft: false,
    // Force fetch data of the right tool. Get the data for the second country
    _forceFetchDataSubToolRight: false,
    // References to d3 tool
    _d3: { "iepg" : null, "iepe" : null },

    _models : { "iepg" : null, "iepe" : null },

    type: "comparison",

    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePoint();
        this.countries = new app.view.tools.common.Countries({
            "variable" : false,
            "draggable" : true
        });

        this._sunburstCDModel = new Backbone.Model();
        this._sunburstCDView = new app.view.tools.SunburstComparisonDataView({
            'model': this._sunburstCDModel,
            'iepgvsiepe' : true
        });
    },

 	_events: function(){
        return _.extend({},
            app.view.tools.Plugin.prototype._events.apply(this),
            {
               "mouseenter .infoover": function(e){
               		var $e = $(e.target);
                    $e.closest(".co_ranking").find(".content_infoover").fadeIn(300);
               },
               "mouseout .infoover": function(e){
               		var $e = $(e.target);
                    $e.closest(".co_ranking").find(".content_infoover").fadeOut(300);
               }
           }
        );
    },

    _setListeners: function(){
        app.view.tools.Plugin.prototype._setListeners.apply(this);

        this.stopListening(app.events,"slider:singlepointclick");
        this.listenTo(app.events,"slider:singlepointclick",function(year){
            var ctx = this.getGlobalContext();
            ctx.data.slider = [{
                "date" : new Date(year),
                "type" : "Point"
            }];
            ctx.saveContext();
            this.copyGlobalContextToLatestContext();

            this._forceFetchDataMap = true;

            this.render();

        });

        //redefine the contextchange:countries to not re-render each time a country is added
        this.stopListening(app.events,"contextchange:countries");
        this.listenTo(app.events,"contextchange:countries",function(){
            //TOREMOVE
            console.log("contextchange:countries at app.view.tools.ComparisonPlugin");

            var ctxObj = this.getGlobalContext(),
            	ctx = ctxObj.data,
                selection = ctx.countries.selection;


            if (!selection.length){
                // Let's force a re-render because we need to adapt the context.
                this._forceFetchDataTool = true;
                this.render(); // Implicit call to contextToURL
            }
            this.countries.render();

            this.copyGlobalContextToLatestContext();
        });

        this.listenTo(app.events,"countryclick",function(id_country){
            //TOREMOVE
            console.log("countryclick at app.view.tools.ComparisonPlugin");
             var ctxObj = this.getGlobalContext(),
                ctx = ctxObj.data,
                current = ctx.countries.selection[0];

            if (current != id_country){
                ctx.countries.selection[0] = id_country;
            	this._forceFetchDataTool = true;
            	this.render();
            }
        });

        this.listenTo(app.events,'sunburst:moveto',this._moveChartSectionByName);

    },

    resizeMe: function(){
        app.view.tools.Plugin.prototype.resizeMe.apply(this);
        this._renderSubTool("iepg");
        this._renderSubTool("iepe");
    },

    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.ComparisonPlugin");

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            year = ctx.slider[0].date.getUTCFullYear(),
            country = ctx.countries.selection[0];

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
        }));

        this.$co_left = this.$("#co_chart_left");
        this.$co_right = this.$("#co_chart_right");


        this.$chart_left = this.$co_left.find(".chart");
        this.$chart_right = this.$co_right.find(".chart");

        this.$chart_legend_left = this.$co_left.find(".chart_legend");
        this.$chart_legend_right = this.$co_right.find(".chart_legend");

        this.$('#data_legend').html(this._sunburstCDView.el);

        if (ctx.countries.list.length==0){
            this._showError("emptybar");
        }
        else if(country == null){
            this._showError("nocountry");
        }
        else if (year<= 2000 // No data avalaible for iepe before year 2000
            || country && country.length > 2  // Only blocks
            || app.blocks.XBEU[year].indexOf(country) == -1 // Only UE countries

            ){

            this._showError("generic");
        }

        else{

            // Get the data from server if _forceFetchDataTool is set to true.
            if (this._forceFetchDataTool){
                this._n_fetches = 0;
                this._errorfetch = false;

                // Fetch the data
                for (var family in {"iepg":null ,"iepe":null}){
                    this._fetchModelClosure(family);
                }
            }
            else{
                //We already have the data, let's draw directly

                if (!this._models["iepg"].get(year).family.global.value
                    || !this._models["iepe"].get(year).family.global.value){
                    this._showError("generic");
                }
                else{
                    this._showChart();

                    this._renderSubTool("iepg");
                    this._renderSubTool("iepe");
                    this._renderMap();
                }
            }
        }
    },

    _showError:function(type_error){
        this.$(".body > div").hide();
        this.$(".body > div.error."+type_error).show();
    },

    _showChart: function(){
        this.$(".body > div").hide();
        this.$(".body .container-comp").show();
    },

    _fetchModelClosure: function(family){

        this._models[family] = new app.model.tools.country({
            "id" : country,
            "family" : family
        });

        var _this = this;
        this._models[family].fetch({
            success: function(){
                _this._n_fetches++;

                if (!_this._models[family].get(year).family.global.value){
                    _this._errorfetch = true;
                }

                if (_this._n_fetches == 2){
                    _this._forceFetchDataTool = false;


                    if (_this._errorfetch){
                        _this._showError();
                    }
                    else{
                        _this._showChart();
                        _this._renderSubTool("iepg");
                        _this._renderSubTool("iepe");
                        _this._renderMap();
                    }
                }
            }
        });
    },

    _renderSubTool:function(family){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            country = ctx.countries.selection[0],
            // Links to DOM Elements
            $co_chart = family == "iepg" ? this.$co_left : this.$co_right;


        // Set country name
        $co_chart.find(".name").html(app.countryToString(country) + ' ' + ctx.slider[0].date.getUTCFullYear());

        this._drawD3Chart(family);

    },

    _fetchDataMap: function(){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        // Fetch the collection from the server
        this._mapCollection = new app.collection.CountryToolMap([],{
            "family" :  ctx.family,
            "variable" : ctx.variables[0],
            "date" : ctx.slider[0].date.getUTCFullYear()
        });

        this.listenTo(this._mapCollection,"reset",this._renderMapAsync);

        this._mapCollection.fetch({"reset":true});

    },

     _renderMapAsync: function(){
        this._forceFetchDataMap = false;
        var
            ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;
            variable = ctx.variables[0],
            year =  ctx.slider[0].date.getUTCFullYear(),
            family = ctx.family;

        this.mapLayer = app.map.drawChoropleth(this._mapCollection.toJSON(),year,variable,family);
    },

    _renderMap: function(){
        // draw the map
        if (this._forceFetchDataMap){

            this._fetchDataMap();
        }
        else{
            this._renderMapAsync();
        }
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();

        if (this._sunburstCDView) this._sunburstCDView.close();
    },

    /*
        This method adapt the global context. Call on every render.
    */
    adaptGlobalContext: function(){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            latestCtxObj = this.getLatestContext(),
            latestCtx = latestCtxObj.data;


        /*
        * This tool only could have two countries selected. The options are:
        *   1) The selection is empty
        *       1.1) If The latestContext has a selection the two first (which are present in the countries list) will be choosen.
        *       1.2) If The latestContext doesn't have a selection. Do nothing.
        *   2) The selection has elements.
                2.1) If selection has more than two element, we cut off them.
        */
        ctxObj.removeNullCountriesSelection();

        if (!ctx.countries.selection.length){
            // The selection is empty

            if (latestCtx.selection>0 ){
                //If the latestContext has a selection all the countries (which are present in the list of countries) will be copied.

                for(var i=0,limit=0;i<latestCtx.countries.list.length && limit<2;i++){
                    // Is the selected country in context list?
                    if (ctx.countries.list.indexOf(latestCtx.countries.selection[i]) != -1){
                        ctx.countries.selection.push(latestCtx.countries.selection[i]);
                        limit++;
                    }
                }

            }
            else{
                // the first on the list will be the selected
                ctx.countries.selection = ctx.countries.list.length ? [ctx.countries.list[0]] : [];
            }
        }
        else if (ctx.countries.selection.length>1){
            // Cut off extra elements in the selection
            ctx.countries.selection = ctx.countries.selection.slice(0,1);
        }

        // This tool works with a slider composed by a single point and a reference point.
        var firstPoint = ctxObj.getFirstSliderElement("Point");

        // Have we a point in the context?
        if (!firstPoint){
            // search the firstPoint on the latest context
            var firstPoint = latestCtxObj.getFirstSliderElement("Point");
            if (!firstPoint){
                // set the last year
                firstPoint = {
                    "type" : "Point",
                    "date" : app.config.SLIDER[app.config.SLIDER.length-1]
                };
            }
        }

        ctx.slider = [firstPoint];

        if (!ctx.family){
            if (latestCtx.family){
                ctx.family = latestCtx.family;
            }
            else{
                ctx.family = "iepg";
            }
        }

        if (!ctx.variables){
            if (latestCtx.variables){
                ctx.variables = latestCtx.variables;
            }
            else{
                ctx.variables = ["global"];
            }
        }


        // Save context
        ctxObj.saveContext();

        // update the latest context
        this.copyGlobalContextToLatestContext();
    },

    _drawD3Chart: function(family){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            model = this._models[family],
            year = ctx.slider[0].date.getUTCFullYear(),
            variables = model.get(year).family,
            $chart = family == "iepg" ? this.$co_left.find(".chart") : this.$co_right.find(".chart"),
            $co = family== "iepg" ? this.$co_left : this.$co_right,
            pos = family == "iepg" ? "left" : "right",
            width = $chart.width(),
            height = $chart.height(),
            radius = Math.min(width, height) / 2;

        //$co.find(".subheader .index .value").html(app.formatNumber(variables["global"].value));
        $co.find(".ranking").html(sprintf("<lang>Ranking %d</lang>%s",
                variables["global"].globalranking,
                app.ordchr(variables["global"].globalranking)));

        $chart.html("");

        var x = d3.scale.linear()
            .range([0, 2 * Math.PI]);

        var y = d3.scale.sqrt()
            .range([0, radius]);

        var color = d3.scale.category20c();

        var svg = d3.select(" #co_chart_" + pos +" .chart").append("svg")
            .attr("width", width)
            .attr("height", height)
          .append("g")
            .attr("transform", "translate(" + width / 2 + "," + (height / 2 ) + ")")
            .attr("class", "variable");

        // var partition = d3.layout.partition()
        //     .sort(null)
        //     .value(function(d) { debugger; return d.size; });

        var partition = d3.layout.partition()
            .sort(null)
            .value(function(d) { return d.perc; });

        var arc = d3.svg.arc()
            .startAngle(function(d) { return Math.max(0, Math.min(2 * Math.PI, x(d.x))); })
            .endAngle(function(d) { return Math.max(0, Math.min(2 * Math.PI, x(d.x + d.dx))); })
            .innerRadius(function(d) { return Math.max(0, y(d.y)); })
            .outerRadius(function(d) { return Math.max(0, y(d.y + d.dy)); });

        d3.select(self.frameElement).style("height", height + "px");

        // Interpolate the scales!
        function arcTween(d) {
          var xd = d3.interpolate(x.domain(), [d.x, d.x + d.dx]),
              yd = d3.interpolate(y.domain(), [d.y, 1]),
              yr = d3.interpolate(y.range(), [d.y ? 20 : 0, radius]);
          return function(d, i) {
            return i
                ? function(t) { return arc(d); }
                : function(t) { x.domain(xd(t)); y.domain(yd(t)).range(yr(t)); return arc(d); };
          };
        }

        var div = d3.select(".tooltip").style("opacity", 0);

        var obj = this;

        var tree =  new app.view.tools.utils.variablesTree(variables,family),
            path = svg.selectAll("path")
              .data(partition.nodes(tree.get()))
            .enter().append("path")
              .attr("d", arc)
              .style("fill", function(d) { return d.color; })
            .on("click", click)
            .on("mouseover", function(d) {

                var variable = model.get(year).family[d.name],
                // brother model
                bmodel = family == "iepg" ? obj._models["iepe"] : obj._models["iepg"],
                // brother variables
                bvariable = bmodel ? bmodel.get(year).family[d.name] : null;

                div.transition()
                    .duration(200)
                    .style("opacity", 1);
                div.html(obj._htmlToolTip(variable,bvariable,family))
                    .style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY - 28) + "px");
                $("path[data-variable='" + d.name+"']").attr("enhanced","true");
                })
            .on("mouseout", function(d) {
                div.transition()
                    .duration(500)
                    .style("opacity", 0);
                $("path[data-variable='" + d.name+"']").removeAttr("enhanced");
            })
            .attr("data-variable",function(d){return d.name });


            function click(d) {
                ctx.variables = [d.name];
                obj.contextToURL();

                if (d.name == "global" || d.name == "economic_global" ||
                    d.name == "soft_global" || d.name =="military_global")
                {
                    app.events.trigger('sunburst:moveto',['left','right'],d.name,750);
                }
                else{
                    obj._changeVariable(d.name);
                }
                //obj._refreshMapVariable(family,d.name);

          }

        this._d3[family] = {};
        this._d3[family].path = path;
        this._d3[family].tree = tree;
        this._d3[family].arcTween = arcTween;

        var optsmodel = {};
        optsmodel["tree_"+pos] = tree;
        optsmodel["family"] = this.getGlobalContext().data.family;
        this._sunburstCDModel.set(optsmodel);

        var data_variable;
        if (ctx.variables[0] == "global"){
            app.events.trigger('sunburst:moveto',[pos],ctx.variables[0]);
        }
        else{
            if (ctx.variables[0] == "economic_global" ||
                ctx.variables[0] == "soft_global" || ctx.variables[0] =="military_global"){
                data_variable = ctx.variables[0];
            }
            else{
                data_variable = tree.findParentInTreeByName(ctx.variables[0]);
            }

            app.events.trigger('sunburst:moveto',[pos],data_variable);
        }
    },


    _changeVariable: function(name){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        ctx.variables = [name];
        this.contextToURL();

        this._refreshMapVariable('iepg');

    },

     _moveChartSectionByName: function(pos,varname,speed){

        this._changeVariable(varname);
        var _this = this;

        for (var i =0;i<pos.length;i++){
            this._moveChartSection(pos[i],varname,speed ? speed : 0);
        }

    },

     _moveChartSection: function(pos,variable,speed){
        if (speed == undefined || speed=="undefined"){
            speed = 750;
        }
        var d3pos = pos=='left' ? 'iepg' : 'iepe';
        var _this = this;
        d3.select("#co_chart_" + pos +" .chart path[data-variable='" + variable  + "']").each(function(d, i) {
            _this._d3[d3pos].path.transition()
                         .duration(speed)
                         .attrTween("d", _this._d3[d3pos].arcTween(d));
        });


    },

    // _moveChartSection: function(family,d,callBrother,speed){

    //     if (speed == undefined || speed =="undefined"){
    //         speed = 720;
    //     }

    //     this._d3[family].path.transition()
    //                     .duration(speed)
    //                     .attrTween("d", this._d3[family].arcTween(d));
    //     this._renderChartLegend(family,d.name);

    //     if (!callBrother){
    //         return;
    //     }

    //     // Let's find d in the other tree.
    //     var  // brother family
    //         bfam = family == "iepg" ? "iepe" : "iepg";

    //     if (!this._d3[bfam]){
    //         // no brother chart
    //         return;
    //     }

    //     var    // brother tree
    //         btree = this._d3[bfam].tree,
    //         // brother data element
    //         bd = btree.findElementInTree(d.name);

    //      this._moveChartSection(bfam,bd,false);

    // },

    _htmlToolTip: function(variable,bvariable,family){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            ranking = variable.globalranking  ? variable.globalranking  : variable.relativeranking
            branking = bvariable.globalranking  ? bvariable.globalranking  : bvariable.relativeranking,
            bfamily = family == "iepg" ? "iepe" : "iepg",
            max = _.max([bvariable.value,variable.value]),
            progress = 100 * variable.value / max,
            bprogress = 100 * bvariable.value / max,
            colorVariable = this._d3[family].tree.findElementInTree(variable.variable).color,
            bcolorVariable = this._d3[bfamily].tree.findElementInTree(bvariable.variable).color,
            text = family == "iepg" ? "<lang>Presencia Global</lang>" : "<lang>Presencia Europea</lang>"
            btext = family == "iepe" ? "<lang>Presencia Global</lang>" : "<lang>Presencia Europea</lang>";

        return "<div>"
                +      "<span>" + ranking + app.ordchr(ranking) +" " + text + "</span>"
                +       "<span>" + variable.year + "</span>"
                +      "<div class='clear'></div>"
                +   "</div>"
                +   "<div>"
                +       "<span>" + app.variableToString(variable.variable,family) + "</span>"
                +       "<span>" + app.formatNumber(variable.value) + "</span>"
                +       "<div class='clear'></div>"
                +   "</div>"

                + "<div class='co_progress' style='margin-left:-10px;margin-right:-10px'>"
                    +       "<div class='progress' ><div  style='width:" + progress + "%;background-color:" + colorVariable + ";'></div></div>"
                    +       "<div class='progress'><div  style='width:" + bprogress + "%;background-color:" + bcolorVariable + ";'></div></div>"
                + "</div>"
                +   "<div class='compare'>"
                +       "<span class='ml vname'>" + app.variableToString(bvariable.variable,bfamily) + "</span>"
                +       "<span class='mr vvalue'>" + app.formatNumber(bvariable.value) + "</span>"
                +       "<div class='clear'></div>"
                +   "</div>"
                +   "<div class='compare'>"
                +       "<span class='white ml'>" + (branking ? branking + app.ordchr(branking) : "" ) + " " + btext +"</span>"
                +       "<span class='year mr'>" + bvariable.year + "</span>"
                +       "<div class='clear'></div>"
                +   "</div>";



    },

    // _renderChartLegend: function(family,name){

    //     $legend = family == "iepg" ? this.$chart_legend_left : this.$chart_legend_right;

    //     // Just a trick, this will be changed when service will be fixed
    //     if (name=="iepe") name="iepg";

    //     $legend.html(this._templateChartLegend({
    //         data: this._d3[family].tree.findElementInTree(name),
    //         family: family
    //     }));
    // },

    _refreshMapVariable: function(family){
        if (!this._mapCollection)
            return;
        // get data from server
        this._mapCollection._variable = this.getGlobalContext().data.variables[0];
        this._mapCollection._family = family;
        // trigger a call to renderMapAsync
        this._mapCollection.fetch({"reset":true});
    },

    contextToURL: function(){
        // This method transforms the current context of the tool in a valid URL.
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            countries = ctx.countries.list.length>0 ? ctx.countries.list.join(",") : "null",
            countries_sel = ctx.countries.selection.length>0 ? ctx.countries.selection.join(",") : "null",
            variable = ctx.variables[0],
            year = ctx.slider[0].date.getUTCFullYear(),
            filters = app.getFilters().length ? "/" + app.getFilters().join(",") : "";
            url = "comparison/" + variable + "/" + year + "/" + countries + "/" + countries_sel + filters;

        app.router.navigate(url ,{trigger: false});
    },

    URLToContext: function(url){
         var ctxObj = app.context,
            ctx = ctxObj.data;

        // set the slider
        ctx.countries.slider = [{
            "type": "Point",
            "date" : new Date(url.year)
        }];

        ctx.countries.list = url.countries != "null" ? url.countries.split(",") : [];
        ctx.countries.selection = url.countries_sel!= "null" ? url.countries_sel.split(",") : [];

        ctx.variables = [url.variable];

        // Do we have filters?
        if (url.filters){
            app.setFilters(url.filters.split(","));
        }

        // let's store the context.
        ctxObj.saveContext();

        // copy to latest context
        this.copyGlobalContextToLatestContext();
    },

    onBringToFront: function(){
        if (this._sunburstCDView)
            this._sunburstCDView.gofront();
    },

    onBringToBack: function(){
        if (this._sunburstCDView)
            this._sunburstCDView.goback();
    }
});
