app.view.tools.QuotesPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#quotes_tool_template').html() ),
    _templateHelp : _.template( $('#quotes_tool_help_template').html() ),

    mapCollection : null,
    toolCollection : null,

    type: "quotes",
    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePoint();
        this.countries = new app.view.tools.common.Countries({
            "variable" : true
        });


        this.toolCollection = new app.collection.Quotes();
        this.mapCollection = new app.collection.QuotesToolMap();
        
    },

    _events: function(){
        return _.extend({},
            app.view.tools.Plugin.prototype._events.apply(this),
            {}
        );
    },

    _setListeners: function(){
        app.view.tools.Plugin.prototype._setListeners.apply(this);

        this.listenTo(this.toolCollection,"reset",this._renderToolAsync);

        this.listenTo(this.mapCollection,"reset",this._renderMapAsync);

        this.stopListening(app.events,"contextchange:countries");
        this.listenTo(app.events,"contextchange:countries",function(){
            //TOREMOVE
            console.log("contextchange:countries at app.view.tools.QuotesPlugin");
           
            var ctxObj = this.getGlobalContext(),
                ctx = ctxObj.data;

            ctxObj.removeInvalidSelected();

            // Let's force a re-render because we need to adapt the context.
            this._forceFetchDataTool = true;
            this.render(); // Implicit call to contextToURL           

        });

        this.listenTo(app.events,"countryclick",function(id_country){
            //TOREMOVE
            console.log("countryclick at app.view.tools.CountryPlugin");
             var ctxObj = this.getGlobalContext(),
                ctx = ctxObj.data,
                selection = ctx.countries.selection
                idx = selection.indexOf(id_country);

            if (idx != -1){
                // It's already drawn, let's remove it
                selection.splice(idx, 1);
                
            }
            else{
               selection.push(id_country);
                
            }


            this._forceFetchDataTool = true;
            this.render();
            
        });
    },

    /* 
        This method adapt the global context
    */
    adaptGlobalContext: function(){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            latestCtxObj = this.getLatestContext(),
            latestCtx = latestCtxObj.data;

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

        // Save context
        ctxObj.saveContext();

        // update the latest context
        this.copyGlobalContextToLatestContext();
    },

     // Transform the current context in a valid URL
    contextToURL: function(){
        
        // It transforms the current context of the tool in a valid URL.
         // This method transforms the current context of the tool in a valid URL.
        //country/:id_country/:id_variable/:year
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            family = ctx.family,
            countries = ctx.countries.list.length>0 ? ctx.countries.list.join(",") : "null",
            countries_sel = ctx.countries.selection.length>0 ? ctx.countries.selection.join(",") : "null",
            variable = ctx.variables[0],
            year_ref = ctx.slider[0].date.getFullYear(),
            filters = app.getFilters().length ? "/" + app.getFilters().join(",") : "";
            url = "quotes/" + family + "/" + variable + "/" + countries + "/" + countries_sel + "/" + year_ref + filters;

        app.router.navigate(url, {trigger: false});
    },

    URLToContext: function(url){

        var ctxObj = app.context,
            ctx = ctxObj.data;
            
        ctx.family = url.family;
        ctx.variables = [url.variable];
        ctx.countries.list = url.countries != "null" ? url.countries.split(",") : [];
        ctx.countries.selection = url.countries_sel!= "null" ? url.countries_sel.split(",") : [];
        ctx.countries.slider = [{
            "type": "Point",
            "date" : new Date(url.year_ref)
        }];

        // Do we have filters?
        if (url.filters){
            app.setFilters(url.filters.split(","));
        }

        // let's store the context.
        ctxObj.saveContext();

        this.copyGlobalContextToLatestContext();

    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    resizeMe: function(){
        app.view.tools.Plugin.prototype.resizeMe.apply(this);
        this._renderToolAsync();
    },

    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.QuotesPlugin");

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        if (!ctx.countries.list.length){
            // it happens when remove the latest element from the filter
            this.$el.html(this._template({
                ctx: ctx,
                uitype: "nocountry",
            }));
        }
        else{
            // Get the data from server if _forceFetchDataTool is set to true.
            if (this._forceFetchDataTool){
                this._fetchDataTool();
            }
            else{
                this._renderToolAsync();
            }
        }

        if (this._forceFetchDataMap){
            this._fetchDataMap();
        }
        else{
            this._renderMapAsync();
        }

    },

    _fetchDataTool: function(){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;
        
        this.toolCollection._family = ctx.family;
        this.toolCollection._variable = ctx.variables[0];
        this.toolCollection._countries = ctx.countries.list;

        // Implicit call to renderToolAsync
        this.toolCollection.fetch({"reset":true});

    },

    _fetchDataMap: function(){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        // Fetch the collection from the server
        this.mapCollection._family = ctx.family;
        this.mapCollection._variable = ctx.variables[0];
        this.mapCollection._date = ctx.slider[0].date.getFullYear();

         // Implicit call to renderToolMap
        this.mapCollection.fetch({"reset":true});
    },

    _renderToolAsync: function(){

        this._forceFetchDataTool = false;

        var ctx = this.getGlobalContext().data
            year =  this.getGlobalContext().data.slider[0].date.getFullYear(),
            d3data = this._collectionToD3Data(),
            uitype = null;

        if (!ctx.countries.list.length){
            uitype = "nocountry"
        }
        else if (!Object.keys(d3data.data).length){
            //
            uitype = "nodata";
        }
        else{
            uitype = "data"
        }

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
            uitype: uitype,
        }));

        this.$chart = this.$(".chart");

        if (Object.keys(d3data.data).length){
            // No data
             this._drawD3Chart(d3data);
        }

    },

    _renderMapAsync: function(){
        this._forceFetchDataMap = false;

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;
            year =  ctx.slider[0].date.getFullYear(),
            variable = ctx.variables[0],
            family = ctx.family;

        this.mapLayer = app.map.drawChoropleth(this.mapCollection.toJSON(),year,variable,family,"%");
    },

    _collectionToD3Data: function(){
        var col = this.toolCollection.toJSON(),
            resp = {
                "data" : {} ,
                "min_year" : Number.MAX_VALUE,
                "max_year" : Number.MIN_VALUE
            };

        _.each(col,function(c){
            var year = c.year;

            _.each(c.values,function(v){
                if (v.value){
                    if (!resp.data.hasOwnProperty(v.country)){
                        resp.data[v.country] = [];    
                    }

                    if (year < resp.min_year){
                        resp.min_year = year;
                    }

                    if (year > resp.max_year){
                        resp.max_year = year;
                    }

                    resp.data[v.country].push({
                        "year" : year,
                        "value" : v.value,
                        "country" : v.country

                    });    
                }
            });
        });

        return resp;

    },

    _drawD3Chart: function(resp){
        var _this = this,
            ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        var margin = {top: 40, right: 50, bottom: 50, left: 70},
            width = this.$chart.width() - margin.left - margin.right,
            height = this.$chart.height() - margin.top - margin.bottom,
            data = resp.data;

        // let's add a year at each side to simulate a padding in the chart
        var yearDomain = [resp.min_year-1, resp.max_year+1];

        var x = d3.scale.linear()
            .domain(yearDomain)
            .range([0,width]);

        var y = d3.scale.linear()
            .range([height, 0]);

        var xAxis = d3.svg.axis()
            .scale(x)
            .tickPadding(6)
            .tickValues(_.map(app.config.SLIDER, function(d){ return d.getFullYear(); }))
            .tickFormat(d3.format('d'))
            .orient("bottom");

        var yAxis = d3.svg.axis()
            .scale(y)
            .tickSize(-width,6)
            .tickPadding(10)
            //.outerTickSize(0)
            .tickFormat(function(d) { return app.formatNumber(d) + " %"; })
            .orient("left");

        var line = d3.svg.line()
            .x(function(d) { return x(d.year); })
            .y(function(d) { return y(d.value); });

        var svg = d3.select(".chart").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height",  height + margin.top + margin.bottom)
          .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
       
        // Get the max 
        var max = Number.MIN_VALUE;
        _.each(data,function(c){
            var tmp_max = d3.max(c, function(d) { return d.value; });
            if (tmp_max>max)
                max = tmp_max;
        });
    
        y.domain([0,max]);

        // Draw axis
        svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis);

        svg.append("g")
          .attr("class", "y axis")
          .call(yAxis);

        // Draw year ref
        var year = ctx.slider[0].date.getFullYear(),
            data_line_ref = [0,max],
            line_ref = d3.svg.line()
                .x(function(d) { return x(year);})
                .y(function(d) { return y(d);});

        svg.append("path")
              .datum(data_line_ref)
              .attr("class", "line_ref")
              .attr("d", line_ref);

        //highlight the current year
        var idx = _.map(app.config.SLIDER, function(d){ return d.getFullYear(); }).indexOf(year);
        $($(".chart .x.axis .tick")[idx]).attr("selected",true);

        // Div for Tooltip
        var div = d3.select("#quotes_tool .chart").append("div")   
            .attr("class", "tooltip")               
            .style("opacity", 0);

        for (country in data){
            var c = data[country];

            var el = svg.append("path")
              .datum(c)
              .attr("class", "line")
              .attr("d", line);

            // Add line labels
            var textMinMargin = { "left" : 23 , "top" : 4} ,
                textMaxMargin = { "left" : 7 , "top" : 4} ,
                textMinPos = {
                    left: x(c[0].year) - textMinMargin.left,
                    top: y(c[0].value) + textMinMargin.top
                },
                textMaxPos = {
                    left: x(c[c.length-1].year) + textMaxMargin.left,
                    top: y(c[c.length-1].value) + textMaxMargin.top 
                };

            var textMin = svg.append("g")
              .attr("transform", "translate("+ textMinPos.left +"," + textMinPos.top + ")")
              .attr("class","co_line_label")
              .append("text")
                .text(app.countryCodeToStr(country));

            var textMax = svg.append("g")
              .attr("transform", "translate("+ textMaxPos.left +"," + textMaxPos.top + ")")
              .attr("class","co_line_label")
              .append("text")
                .text(app.countryCodeToStr(country));

            // Draw splines
            var circle = svg.selectAll("circle")
                .data(c, function(d) { return d.value; });

              circle.enter().append("circle")
                    .attr("r", 1e-6)
                    .attr("selected", function(d) { 
                        return ctx.countries.selection.indexOf(country)!=-1; 
                    })
                    .on("mousedown", function(d) { console.log(d)})
                .transition()
                    .duration(750)
                    .ease("elastic")
                    .attr("r", 3.5);

            circle.attr("cx", function(d) { return x(d.year); })
                .attr("cy", function(d) { return y(d.value); });

            // Configure tooltip
            circle.on("mouseover", function(d) {     
               div.transition()        
                    .duration(200)      
                    .style("opacity", 1);      
                div.html(_this._htmlToolTip(d,d3.event.pageX))  
                    .style("left", (d3.event.pageX) + "px")     
                    .style("top", (d3.event.pageY - 28) + "px");    
                })                   
            .on("mouseout", function(d) {       
                div.transition()        
                    .duration(500)      
                    .style("opacity", 0); 
            });

            if (ctx.countries.selection.indexOf(country)!=-1){
                el.attr("selected",true);
                textMin.attr("selected",true);
                textMax.attr("selected",true);
            }
            
        }
    },

    _htmlToolTip: function(el){
        
        var ctx = this.getGlobalContext().data,
            variable = ctx.variables[0],
            family = ctx.family;

        // Let's find wich axis tick is the closest one
        var html = "<div>" 
                    +   "<span>" + app.countryToString(el.country) + "</span>"
                    +   "<span>" + el.year + "</span>"
                    +   "<div class='clear'></div>"
                    + "</div>"
                    + "<div>" 
                    +   "<span>" + app.variableToString(variable,family) + "</span>"
                    +   "<span>" + app.formatNumber(el.value) + " %</span>"
                    +   "<div class='clear'></div>"
                    +"</div>"

        return html;
    }

});