app.view.tools.CountryPlugin = app.view.tools.Plugin.extend({
	_template : _.template( $('#country_tool_template').html() ),
    _templateHelp : _.template( $('#country_tool_help_template').html() ),
    //_templateChartLegend : _.template( $('#country_tool_chart_legend_template').html() ),
    type: "country",

    initialize: function(options) {
		this.slider = new app.view.tools.common.SliderSinglePoint();
		this.countries = new app.view.tools.common.Countries({
            "variable" : false
        });

        this._sunburstDataModel = new Backbone.Model({
            "tree": null,
            "family" : null
        });

        this._sunburstDataView = new app.view.tools.SunburstDataView({
            "model": this._sunburstDataModel
        });
    },

    _events: function(){
        return _.extend({},
            app.view.tools.Plugin.prototype._events.apply(this),
            {
               "mouseenter .infoover": function(e){
                    this.$(".content_infoover").fadeIn(300);
               },
               "mouseout .infoover": function(e){
                    this.$(".content_infoover").fadeOut(300);
               },
               "click .co_comment_wrapper a.readmore": "_expandComment"
           }
        );
    },

    _setListeners: function(){
        app.view.tools.Plugin.prototype._setListeners.apply(this);

        //redefine the contextchange:countries to not re-render each time a country is added
        this.stopListening(app.events,"contextchange:countries");
        this.listenTo(app.events,"contextchange:countries",function(){
            //TOREMOVE
            console.log("contextchange:countries at app.view.tools.CountryPlugin");
            // The context has changed will be store by a call to contextToURL. 
            if (!app.context.data.countries.selection.length){
                // Let's force a re-render because we need to adapt the context.
                this.forceFetchDataOnNextRender();
                this.render(); // Implicit call to contextToURL
            }
            else{
                // No need of re-render, Let's refresh the list of countries
                this.countries.render();
                this.contextToURL();
            }
        });

        this.listenTo(app.events,"countryclick",function(id_country){
            //TOREMOVE
            console.log("countryclick at app.view.tools.CountryPlugin");

            var ctx = this.getGlobalContext();
            ctx.data.countries.selection = [id_country];
            
            this.forceFetchDataOnNextRender();
            this.render(); // Implicit call to contextToURL
        });

        this.listenTo(app.events,'sunburst:moveto',this._moveChartSectionByName);
    },

    /* Fetch data for the current country*/
	_fetchDataTool: function(){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;
        
        this.model = new app.model.tools.country({
            "id" : ctx.countries.selection[0],
            "family" : ctx.family
        });

        // Fetch model from de server
        var self = this;
        this.model.fetch({
            success: function() {
               self._renderToolAsync();
            }
        });
	},

    _fetchDataMap: function(){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        // Fetch the collection from the server
        this.mapCollection = new app.collection.CountryToolMap([],{
            "family" :  ctx.family,
            "variable" : ctx.variables[0],
            "date" : ctx.slider[0].date.getUTCFullYear(),
            "mode" : !ctx.countries.selection.length ? 0 :
                    ctx.countries.selection[0].length == 2 ? 0 :
                    ctx.countries.selection[0] == "XBEU" ? 1 : 2
        });
        
        this.listenTo(this.mapCollection,"reset",this._renderMapAsync);

        this.mapCollection.fetch({"reset":true});

    },

    _renderToolAsync: function(){

        this._forceFetchDataTool = false;

        var year =  this.getGlobalContext().data.slider[0].date.getUTCFullYear();

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
            model: this.model.toJSON()[year],
        }));

        this.$chart = this.$(".chart");

        this._drawD3Chart(year);
        
    },

    resizeMe: function(){
        app.view.tools.Plugin.prototype.resizeMe.apply(this);
        this._renderToolAsync();
    },

    _renderMapAsync: function(){
        this._forceFetchDataMap = false;
        var 
            ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;
            year =  ctx.slider[0].date.getUTCFullYear(),
            family = ctx.family,
            variable = ctx.variables[0];

        this.mapLayer = app.map.drawChoropleth(this.mapCollection.toJSON(),year,variable,family);

    },

    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.CountryPlugin");

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        if (!ctx.countries.selection.length){
            // it happens when remove the latest element from the filter
            this.$el.html(this._template({
                ctx: this.getGlobalContext().data,
                model: null,
            }));
        }
        else{
            // Get the data from server if _forceFetchDataTool is set to true. If _forceFetchDataTool is set to false data is not requested to server
            if (this._forceFetchDataTool){
                this._fetchDataTool();
            }
            else{
                this._renderToolAsync();
            }
        }

        this.renderMap();
    },

    renderMap: function(){
        if (this._forceFetchDataMap){

            this._fetchDataMap();
        }
        else{
            this._renderMapAsync();
        }
    },

    clearMap: function(){
        app.map.removeChoropleth();
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();

        if (this._sunburstDataView) this._sunburstDataView.close();
    },

    /* 
        This method adapt the global context
    */
    adaptGlobalContext: function(){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            latestCtxObj = this.getLatestContext(),
            latestCtx = latestCtxObj.data;

        
        ctxObj.removeNullCountriesSelection();
        /*
        * This tool only has a country selected. The options are:
        *   1) The selection is empty
        *       1.1) If The latestContext has a selection and the country selected is on the list of countries, this will be taken.
        *       1.2) If The latestContext doesn't have a selection, the first on the list will be the selected.
        *   2) The selection has elements. All except the first one will be removed.
        */
        
        if (!ctx.countries.selection.length){
            // The selection is empty
           
            if (latestCtx.selection>0 && ctx.countries.list.indexOf(latestCtx.selection[0])!=-1){
                // If The latestContext has a selection and the country selected is on the list of countries
                ctx.countries.selection = [latestCtx.selection[0]];
            }
            else{
                // the first on the list will be the selected
                ctx.countries.selection = ctx.countries.list.length ? [ctx.countries.list[0]] : [];
            }
        }
        else{
            // All except the first one will be removed.
            ctx.countries.selection = [ctx.countries.selection[0]];
        }


        // This tool works with a single point slider. 
        var firstPoint = ctxObj.getFirstSliderElement("Point");

        if (firstPoint){
            // Get the first point and remove the others from the context.
            ctx.slider = [firstPoint];
        }
        else{
            // search the firstPoint on the latest context
            var firstPoint = latestCtxObj.getFirstSliderElement("Point");
            if (firstPoint){
                // Get the first point from the latest context and remove the others
                ctx.slider = [firstPoint];
            }
            else{
                // set the last year
                ctx.slider = [{
                    "type" : "Point",
                    "date" : app.config.SLIDER[app.config.SLIDER.length-1]
                }];
            }
        }

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

    contextToURL: function(){
        // This method transforms the current context of the tool in a valid URL.
        //country/:id_country/:id_variable/:year
    
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,  
            family = ctx.family,          
            countries = ctx.countries.list.length>0 ? ctx.countries.list.join(",") : "null",
            country_sel = ctx.countries.selection.length>0 ? ctx.countries.selection[0] : "null",
            variable = ctx.variables[0],
            year = ctx.slider[0].date.getUTCFullYear(),
            filters = app.getFilters().length ? "/" + app.getFilters().join(",") : "";
            url = "country/" + family + "/" + variable + "/" + countries + "/" + country_sel + "/" + year + filters;

        app.router.navigate(url, {trigger: false});
        
    },

    URLToContext: function(url){

        var ctxObj = app.context,
            ctx = ctxObj.data;
            
        ctx.family = url.family;
        ctx.variables = [url.variable];
        
        ctx.countries.list = url.countries != "null" ? url.countries.split(",") : [];
        ctx.countries.selection = url.country_sel!= "null" ? [url.country_sel] : [];

        ctx.countries.slider = [{
            "type": "Point",
            "date" : new Date(url.year)
        }];

        // Do we have filters?
        if (url.filters){
            app.setFilters(url.filters.split(","));
        }

        // let's store the context.
        ctxObj.saveContext();

        this.copyGlobalContextToLatestContext();

    },

    _drawD3Chart: function(year){
        var ctxObj = app.context,
            ctx = ctxObj.data,
            family = ctx.family,
            width = this.$chart.width(),
            height = this.$chart.height(),
            radius = Math.min(width, height) / 2;

        var x = d3.scale.linear()
            .range([0, 2 * Math.PI]);

        var y = d3.scale.sqrt()
            .range([0, radius]);

        var color = d3.scale.category20c();

        var svg = d3.select(".chart").append("svg")
            .attr("width", width)
            .attr("height", height)
          .append("g")
            .attr("transform", "translate(" + width / 2 + "," + (height / 2 ) + ")")
            .attr("class", "variable");

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

        var div = d3.select("#country_tool .tooltip"),
            obj = this;

        this.tree = new app.view.tools.utils.variablesTree(this.model.get(year).family,family);

        this._sunburstDataModel.set({
            "tree" : this.tree,
            "family" : this.getGlobalContext().data.family
        });

        this.$(".chart_legend").html(this._sunburstDataView.$el);

        var path = svg.selectAll("path")
              .data(partition.nodes(this.tree.get()))
            .enter().append("path")
              .attr("d", arc)
              .style("fill", function(d) { return d.color; })
            .on("click", click)
            .on("mouseover", function(d) {     
                div.transition()        
                    .duration(200)      
                    .style("opacity", 1);      
                div.html(obj._htmlToolTip(d.name))  
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

            if (d.name == "global" || d.name == "economic_global" ||
                d.name == "soft_global" || d.name =="military_global"){
                //obj._moveChartSection(d,750);
                app.events.trigger('sunburst:moveto',d.name,750);
            }
            else{
                obj._changeVariable(d.name);
            }
        }

        this._d3 = {};
        this._d3.path = path;
        this._d3.arcTween = arcTween;

        if (ctx.variables[0] == "global"){
            app.events.trigger('sunburst:moveto',ctx.variables[0]);
        }
        else {

            var data_variable;
            if (ctx.variables[0] == "economic_global" ||
                    ctx.variables[0] == "soft_global" || ctx.variables[0] =="military_global"){
                
                data_variable = ctx.variables[0];
            }
            else{
                data_variable = this.tree.findParentInTreeByName(ctx.variables[0]);
            }
            app.events.trigger('sunburst:moveto',data_variable);
        }      
    },


    _changeVariable: function(name){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        ctx.variables = [name];
        this.contextToURL();

        
        this.mapCollection._variable = name;
        this.mapCollection.fetch({"reset":true});    

    },

    _moveChartSectionByName: function(varname,time){

        this._changeVariable(varname);

        var _this = this;
        d3.select("path[data-variable='" + varname  + "']").each(function(d, i) {
            _this._moveChartSection(d,time ? time : 0);
        }); 
    },

    _moveChartSection: function(d,speed){

        this._d3.path.transition()
                         .duration(speed)
                         .attrTween("d", this._d3.arcTween(d));

        //this._renderChartLegend(d.name);
    },

    _htmlToolTip: function(tvariable){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            family = ctx.family,
            year =  this.getGlobalContext().data.slider[0].date.getUTCFullYear(),
            variable = tvariable == "iepg" || tvariable ==  "iepe" ? this.model.get(year).family.global 
                        : this.model.get(year).family[tvariable],
            ranking = variable.globalranking ? variable.globalranking : variable.relativeranking;

            html = "<div>" 
                    +   "<span>" + ranking + app.ordchr(ranking) + " "  +app.countryToString(variable.code) + "</span>"
                    +   "<span>" + year + "</span>"
                    +   "<div class='clear'></div>"
                    + "</div>"
                    + "<div>" 
                    +   "<span>" + app.variableToString(variable.variable,family) + "</span>"
                    +   "<span>" + app.formatNumber(variable.value) + "</span>"
                    +   "<div class='clear'></div>"
                    +"</div>"

        return html;

    },

    _expandComment: function(e){
        e.preventDefault();

        this.$('.comment_wrapper').removeClass('short');
        $(e.target).remove();
    },

    onBringToFront: function(){
        if (this._sunburstDataView)
            this._sunburstDataView.gofront();
    },

    onBringToBack: function(){
        if (this._sunburstDataView)
            this._sunburstDataView.goback();   
    }
    
});