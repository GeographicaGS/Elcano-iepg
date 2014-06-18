app.view.tools.ComparisonPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#comparison_tool_template').html() ),
   	// This is the template for the chart legend
    _templateChartLegend : _.template( $('#country_tool_chart_legend_template').html() ),
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
    },


    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.ComparisonPlugin");

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            year = ctx.slider[0].date.getFullYear();

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,

        }));

        this.$co_iepg = this.$("#piepg");
        this.$co_iepe = this.$("#piepe");

        this.$co_left = this.$("#co_chart_left");
        this.$co_right = this.$("#co_chart_right");


        this.$chart_left = this.$co_left.find(".chart");
        this.$chart_right = this.$co_right.find(".chart");

        this.$chart_legend_left = this.$co_left.find(".chart_legend");
        this.$chart_legend_right = this.$co_right.find(".chart_legend");

        // Get the data from server if _forceFetchDataTool is set to true. If _forceFetchDataTool is set to false data is not requested to server
        if (this._forceFetchDataTool){
            this._forceFetchDataSubToolLeft = true;
            this._forceFetchDataSubToolRight = true;
        }
        
        this._renderSubTool("iepg");
        this._renderSubTool("iepe");

        this._renderMap();

        this._forceFetchDataTool = false;

    },

    _renderSubTool:function(family){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            country = ctx.countries.selection[0],
            forceFetch = family == "iepg" ? this._forceFetchDataSubToolLeft : this._forceFetchDataSubToolRight,
            // Links to DOM Elements
           	$co_chart = family == "iepg" ? this.$co_left : this.$co_right;
           	
        // Set country name
        $co_chart.find(".name").html(app.countryToString(country));



        if (forceFetch){
            // Fetch the data of this tool
            this._models[family] = new app.model.tools.country({
                "id" : country,
                "family" : family
            });

            var _this = this;
            this._models[family].fetch({
                success: function(){
                   if (family == "iepg"){
                        _this._forceFetchDataSubToolLeft = false;
                   }
                   else{
                        _this._forceFetchDataSubToolRight = false;
                   }

                   _this._drawD3Chart(family);
                }
            });
        }
        else{
            //We already have the data, let's draw directly
            this._drawD3Chart(family);
        }
    },

    _fetchDataMap: function(){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        // Fetch the collection from the server
        this._mapCollection = new app.collection.CountryToolMap([],{
            "family" :  ctx.family,
            "variable" : "global",
            "date" : ctx.slider[0].date.getFullYear()
        });
        
        this.listenTo(this._mapCollection,"reset",this._renderMapAsync);

        this._mapCollection.fetch({"reset":true});

    },

     _renderMapAsync: function(){
        this._forceFetchDataMap = false;
        var 
            ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;
            year =  ctx.slider[0].date.getFullYear(),
            family = ctx.family;

        this.mapLayer = app.map.drawChoropleth(this._mapCollection.toJSON(),year,"global",family);
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
                // Do nothing
            }
        }
        else if (ctx.countries.selection.length==1){
            ctx.countries.selection[1] = null;
        }
        else if (ctx.countries.selection.length>2){
            // Cut off extra elements in the selection
            ctx.countries.selection = ctx.countries.selection.slice(0,2);

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

        // Save context
        ctxObj.saveContext();

        // update the latest context
        this.copyGlobalContextToLatestContext();
    },

    _drawD3Chart: function(family){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            model = this._models[family],
            year = ctx.slider[0].date.getFullYear(),
            variables = model.get(year).family,
            $chart = family == "iepg" ? this.$co_left.find(".chart") : this.$co_right.find(".chart"),
            $co = family== "iepg" ? this.$co_iepg : this.$co_iepe,
            pos = family == "iepg" ? "left" : "right",
            width = $chart.width(),
            height = $chart.height(),
            radius = Math.min(width, height) / 2;

        $co.find(".subheader .index .value").html(sprintf("%.2f",variables["global"].value));
        $co.find(".ranking").html(sprintf("<lang>Puesto %dº </lang>", variables["global"].globalranking));

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

        var partition = d3.layout.partition()
            .value(function(d) { return d.size; });

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

        var div = d3.select("#comparison_tool .chart").append("div")   
            .attr("class", "tooltip")               
            .style("opacity", 0);

        var obj = this;

        var tree =  new app.view.tools.utils.variablesTree(variables),
            path = svg.selectAll("path")
              .data(partition.nodes(tree.get()))
            .enter().append("path")
              .attr("d", arc)
              .style("fill", function(d) { return d.color; })
            .on("click", click)
            .on("mouseover", function(d) {     
                div.transition()        
                    .duration(200)      
                    .style("opacity", 1);      
                div.html(obj._htmlToolTip(model.get(year).family[d.name]))  
                    .style("left", (d3.event.pageX) + "px")     
                    .style("top", (d3.event.pageY - 28) + "px");    
                })                  
            .on("mouseout", function(d) {       
                div.transition()        
                    .duration(500)      
                    .style("opacity", 0);   
            });
        

            function click(d) {
                if (d.name == "global" || d.name == "economic_global" ||
                    d.name == "soft_global" || d.name =="military_global")
                {
                    obj._moveChartSection(family,d,true);
                }

          }

        this._d3[family] = {};
        this._d3[family].path = path;
        this._d3[family].tree = tree;
        this._d3[family].arcTween = arcTween;

        this._renderChartLegend(family,"global");
    },

    _moveChartSection: function(family,d,callBrother){

        this._d3[family].path.transition()
                        .duration(750)
                        .attrTween("d", this._d3[family].arcTween(d));
        this._renderChartLegend(family,d.name);

        if (!callBrother){
            return;
        }

        // Let's find d in the other tree.
        var  // brother family
            bfam = family == "iepg" ? "iepe" : "iepe";

        if (!this._d3[bfam]){
            // no brother chart
            return;
        }

        var    // brother tree
            btree = this._d3[bfam].tree,
            // brother data element
            bd = btree.findElementInTree(d.name);
    
         this._moveChartSection(bfam,bd,false);

    },

    _htmlToolTip: function(variable){
        
        var html = "<div>" 
                    +   "<span>" + variable.globalranking + "º " +app.countryToString(variable.code) + "</span>"
                    +   "<span>" + variable.year + "</span>"
                    +   "<div class='clear'></div>"
                    + "</div>"
                    + "<div>" 
                    +   "<span>" + app.variableToString(variable.variable,this.getGlobalContext().data.family) + "</span>"
                    +   "<span>" + sprintf("%0.2f",variable.value) + "</span>"
                    +   "<div class='clear'></div>"
                    +"</div>"

        return html;

    },

    _renderChartLegend: function(family,name){

        $legend = family == "iepg" ? this.$chart_legend_left : this.$chart_legend_right;

        // Just a trick, this will be changed when service will be fixed
        if (name=="iepe") name="iepg";

        $legend.html(this._templateChartLegend({
            data: this._d3[family].tree.findElementInTree(name),
            family: this.getGlobalContext().data.family
        }));
    },

    contextToURL: function(){
        // This method transforms the current context of the tool in a valid URL.
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            filters = app.getFilters().join(",");

        app.router.navigate("comparison/" 
            + ctx.slider[0].date.getFullYear() + "/" // Year
            + ctx.countries.list.join(",") + "/" // Countries list
            + ctx.countries.selection[0]   // Countries selected
            + (filters ? "/" + filters : "") ,{trigger: false});
    },

    URLToContext: function(url){
         var ctxObj = app.context,
            ctx = ctxObj.data;

        // set the slider
        ctx.countries.slider = [{
            "type": "Point",
            "date" : new Date(url.year)
        }];

        ctx.countries.list = url.countries.split(",");
        ctx.countries.selection = [url.country_sel];

        // Do we have filters?
        if (url.filters){
            app.setFilters(url.filters.split(","));
        }

        // let's store the context.
        ctxObj.saveContext();

        // copy to latest context
        this.copyGlobalContextToLatestContext();
    }
});