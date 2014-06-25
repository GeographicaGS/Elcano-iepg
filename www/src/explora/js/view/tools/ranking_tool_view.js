app.view.tools.RankingPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#ranking_tool_template').html() ),
    type: "ranking",
    _dataMap : null,

    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePointReference();
        this.countries = new app.view.tools.common.Countries();
    },

    _events: function(){
        return _.extend({},
            app.view.tools.Plugin.prototype._events.apply(this),
            {
               "click a[block-analyze]": "changeBlockAnalysis"
           }
        );
    },

    _setListeners: function(){
        app.view.tools.Plugin.prototype._setListeners.apply(this);

        this.listenTo(app.events,"countryclick",function(id_country){
            //TOREMOVE
            console.log("countryclick at app.view.tools.CountryPlugin");

            var ctx = this.getGlobalContext();
            ctx.data.countries.selection = [id_country];
    
            // Render again the tool with the new context
            this._forceFetchDataTool = true;
            this.render(); // implicit save the context
        });

        this.stopListening(app.events,"slider:singlepointclick");
        this.listenTo(app.events,"slider:singlepointclick",function(year){
            //TOREMOVE
            console.log("slider:singlepointclick at app.view.tools.CountryPlugin");

            var ctx = this.getGlobalContext();
            ctx.getFirstSliderElement("Point").date = new Date(year)

            // Render again the tool with the new context
            this._forceFetchDataTool = true;
            this.render(); // implicit save the context
        });

        this.listenTo(app.events,"slider:singlepointreferenceclick",function(year){
            //TOREMOVE
            console.log("slider:singlepointclick at app.view.tools.CountryPlugin");

            var ctx = this.getGlobalContext();
            ctx.getFirstSliderElement("PointReference").date = new Date(year);

            // Render again the tool with the new context
            this._forceFetchDataTool = true;
            this.render(); // implicit save the context
        });

    },

    /* Fetch data for the current country*/
    _fetchDataTool: function(){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        this.collection = new app.collection.RankingTool({},{

            "year" : ctxObj.getFirstSliderElement("Point").date.getFullYear(),
            "yearRef" : ctxObj.getFirstSliderElement("PointReference").date.getFullYear(),
            "variable" : ctx.variables[0],
            "family" : ctx.family,
            "block_analize" : ctx.block_analize,
            "entities" : ctx.countries.list
        });

        this.listenTo(this.collection,"reset",this._renderToolAsync);

        this.collection.fetch({"reset":true});
        
    },

    _waitAllCollectionFetch: function(){
        this._nCollectionFetches--;
        if (!this._nCollectionFetches){
            this._renderToolAsync();
        }
    },

    _renderToolAsync: function(){

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
            collection: this.collection.toJSON(),
        }));

        this.$chart = this.$(".chart");

        this.$(".co_chart").height(this.$(".body").height()- this.$("h5").outerHeight(true)- 20);

        this._drawD3Chart();

        this._forceFetchDataTool = false;

        this._dataMap = new app.view.map({
            "container": "data_map",
            "zoom" : 1,
            "tooltip" : this.$("#ranking_map_tooltip")
        }).initialize();

         var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            year = ctx.slider[0].date.getFullYear(),
            variable = ctx.variables[0],
            family = ctx.family;

        var mapArray = [],
            colJSON = this.collection.toJSON();

        for (var i=0;i<colJSON.length;i++){
            mapArray.push({
                "code" : colJSON[i].code,
                "value" : colJSON[i].currentRanking,
            })
        }

        this._dataMap.drawChoropleth(mapArray,year,variable,family);

        this.mapLayer = app.map.drawChoropleth(mapArray,year,variable,family);
    },

    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.RankingPlugin");

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        if (false && !ctx.countries.selection.length){
            // it happens when remove the latest element from the filter
            this.$el.html(this._template({
                ctx: this.getGlobalContext().data,
                collection: null,
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
    },

    contextToURL: function(){
        // This method transforms the current context of the tool in a valid URL.
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            filters = app.getFilters().join(",");

        app.router.navigate("ranking/" 
            + ctx.family + "/"  // Family
            + ctx.variables[0] + "/"  // Variable
            + ctx.slider[0].date.getFullYear() + "/" // Year
            + ctx.slider[1].date.getFullYear() + "/" // Reference year 
            + ctx.countries.list.join(",") + "/" // Countries list
            + ctx.countries.selection[0]  + "/" // Country selected
            + (ctx.block_analize ? 1 : 0)
            + (filters ? "/" + filters : "") ,{trigger: false});
    },

    URLToContext: function(url){
         var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;
           
        // Overwrite the family
        ctx.family = url.family;
        // Overwrite the variable
        ctx.variables = [url.variable];

        // set the slider
        ctx.countries.slider = [{
            "type": "Point",
            "date" : new Date(url.year)
        },
        {
            "type": "PointReference",
            "date" : new Date(url.year_ref)
        }];

        ctx.countries.list = url.countries.split(",");
        ctx.countries.selection = [url.country_sel];

        ctx.block_analize = url.block_analize==0 ? false : true;

        // Do we have filters?
        if (url.filters){
            app.setFilters(url.filters.split(","));
        }

        // let's store the context.
        ctxObj.saveContext();

        // copy to latest context
        this.copyGlobalContextToLatestContext();
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    _drawD3Chart: function(){
         var data = _.filter(this.collection.toJSON(), function(d){ return d.code; }),
            max = data[0].currentValue > data[0].referenceValue 
                    ?  data[0].currentValue 
                    : data[0].referenceValue,
            margin = {top: 60, right: 20, bottom: 30, left: 140},
            width = this.$chart.width() - margin.left - margin.right,
            barHeight = 20,
            totalCountryHeight = barHeight * 2 + 10 /*padding*/,
            height = data.length * totalCountryHeight - margin.top - margin.bottom,
            yAxisWidth = 100,
            visibleHeight = this.$chart.height(),
            ctxObj = this.getGlobalContext(),
            year = ctxObj.getFirstSliderElement("Point").date.getFullYear(),
            yearRef = ctxObj.getFirstSliderElement("PointReference").date.getFullYear();

        var x = d3.scale.linear()
            .range([0, width])
            .domain([0, max]);

        var y = d3.scale.linear()
            .range([0, height])
            .domain([1, data.length]);

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("top")
            .tickSize(-height);

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left")
            .tickSize(-width)
            .ticks(data.length);

        var zoom = d3.behavior.zoom()
            .y(y)
            .on("zoom", zoomed);

        var svg = d3.select(".chart").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
          .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0,0)")
          .call(xAxis)

        .selectAll("text")
            .attr("y", 0)
            .attr("x", 9)
            .attr("dy", ".35em")
            .attr("transform", "rotate(-90)")
            .style("text-anchor", "start");
      
        // Add another SVG, need to simulate an overflow hidden
        var canvas = svg.append("svg")
                .attr("class", "co_bar")
                .attr("width", width  + yAxisWidth)
                .attr("height", visibleHeight)
                .attr("x", "-" + yAxisWidth)
                .call(zoom);

        // Let's add a rect to have all the graphic space draggable
        var rect = canvas.append("rect")
                .attr("width", width + yAxisWidth )
                .attr("height", visibleHeight)
                .attr("fill","none");

        // This is the element where apply then transformation
        canvas = canvas.append("g");

        // Let's add the data
        var subset = canvas.selectAll(".bar").data(data);

        var div = d3.select("body").append("div")   
        .attr("class", "tooltip")               
        .style("opacity", 0);

        var obj = this;

        // Variable bars
        canvas.selectAll(".bar").data(data).enter().append("rect")
          .attr("class", "bar")
          .attr("x", yAxisWidth)
          .attr("width", function(d) { return x(d.currentValue); })
          .attr("y", function(d) { return y(data.indexOf(d) + 1); })
          .attr("height", barHeight)
          .on("mouseover", function(d) {     
                div.transition()        
                    .duration(200)      
                    .style("opacity", 1);      
                div.html(obj._htmlChartToolTip({
                    "pos" : d.currentRanking,
                    "code" : d.code,
                    "value" : d.currentValue,
                    "year" : year,
                    
                }))  
                    .style("left", (d3.event.pageX) + "px")     
                    .style("top", (d3.event.pageY - 28) + "px");    
                })                  
            .on("mouseout", function(d) {       
                div.transition()        
                    .duration(500)      
                    .style("opacity", 0);   
            });

        // References bars
        subset.enter().append("rect")
            .attr("class", "bar ref")
            .attr("x", yAxisWidth)
            .attr("width", function(d) { return x(d.referenceValue); })
            .attr("y", function(d) { return y(data.indexOf(d) + 1) + barHeight + 1; })
            .attr("height", barHeight)
            .on("mouseover", function(d) {   

                div.transition()        
                    .duration(200)      
                    .style("opacity", 1);      
                div.html(obj._htmlChartToolTip({
                    "pos" : d.referenceRanking,
                    "code" : d.code,
                    "value" : d.referenceValue,
                    "year" : yearRef,
                }))  
                    .style("left", (d3.event.pageX) + "px")     
                    .style("top", (d3.event.pageY - 28) + "px");    
            })                  
            .on("mouseout", function(d) {       
                div.transition()        
                    .duration(500)      
                    .style("opacity", 0);   
            });

        // Y axis
        var co_label = subset.enter().append("g")
            .attr("class","co_label")
            .attr("x",0)
            .attr("y",0)
            .attr("transform",function(d) { 
                var h = (data.indexOf(d) + 0) * (totalCountryHeight );
                    h += 10;
                return "translate(0," + h + ")"; 
            });
       
        co_label.append("image")
            .attr("x",0)
            .attr("y",0)
            .attr("width",25)
            .attr("height",25)
            .attr("xlink:href",function(d){
                return  "/img/flags/ranking/" + d.code + ".svg"
            });

         co_label.append("text")
            .attr("x",40)
            .attr("y", 17)
            .text(function(d){ return app.countryCodeToStr(d.code) });

        co_label.append("text")
            .attr("class","number")
            .attr("x",yAxisWidth - 30)
            .attr("y", 17)
            .attr("width",40)
            .text(function(d){ return data.indexOf(d) + 1});


        function zoomed() {
            //console.log("scrolling");
            var newy = zoom.translate()[1],
                maxHeight =  height - visibleHeight + 150;
            if (newy>0){
                //console.log(newy);
                newy = 0;
                zoom.translate([0,newy]);
            }
            else if ((newy*-1) > maxHeight){
                newy = maxHeight*-1;
                zoom.translate([0,newy]);
            }
            
            //console.log(newy);
            canvas.attr("transform", "translate(0," + newy + ")");

        }    

        var scroll_inc = (totalCountryHeight) * 5;

        d3.select("#scroll_up").on("click", function(){
            var newzoom = zoom.translate()[1] + scroll_inc;
            zoom.translate([0,newzoom]);
            zoomed();
        });

        d3.select("#scroll_down").on("click", function(){   
            var newzoom = zoom.translate()[1] - scroll_inc;
            zoom.translate([0,newzoom]);
            zoomed();
        });
    },

    _htmlChartToolTip: function(d){
        var ctx = this.getGlobalContext().data,
            variable = ctx.variables[0],
            family = ctx.family;

            html = "<div>" 
                    +   "<span>" + d.pos + "º " +app.countryToString(d.code) + "</span>"
                    +   "<span>" + d.year + "</span>"
                    +   "<div class='clear'></div>"
                    + "</div>"
                    + "<div>" 
                    +   "<span>" + app.variableToString(variable,family) + "</span>"
                    +   "<span>" + sprintf("%0.2f",d.value) + "</span>"
                    +   "<div class='clear'></div>"
                    +"</div>";

        return html;

    },

    clearMap: function(){
        app.map.removeChoropleth();
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
        * This tool only could have more than one country selected. The options are:
        *   1) The selection is empty
        *       1.1) If The latestContext has a selection all the countries (which are present in the list of countries) will be copied.
        *       1.2) If The latestContext doesn't have a selection, the first on the list will be the selected.
        *   2) The selection has elements. We do nothing
        */
        
        if (!ctx.countries.selection.length){
            // The selection is empty
           
            if (latestCtx.selection>0 ){
                //If the latestContext has a selection all the countries (which are present in the list of countries) will be copied.
                for(var i=0;i<latestCtx.countries.list.length;i++){
                    // Is the selected country in context list?
                    if (ctx.countries.list.indexOf(latestCtx.countries.selection[i]) != -1){
                        ctx.countries.selection.push(latestCtx.countries.selection[i]);    
                    }
                }
                
            }
            else{
                // the first on the list will be the selected
                ctx.countries.selection = ctx.countries.list.length ? [ctx.countries.list[0]] : [];
            }
        }
        else{
            // Do nothing
        }

        // This tool works with a slider composed by a single point and a reference point. 
        var firstPoint = ctxObj.getFirstSliderElement("Point"),
            firstPointRef = ctxObj.getFirstSliderElement("PointReference");;

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

        // Have we a point reference in the context?
        if (!firstPointRef){
            // search the firstPointRef on the latest context
            var firstPointRef = latestCtxObj.getFirstSliderElement("PointReference");
            if (!firstPointRef){
                // set the middle point for the reference
                firstPointRef = {
                    "type" : "PointReference",
                    "date" : app.config.SLIDER[Math.floor(app.config.SLIDER.length/2)]
                };
            }
        }

        ctx.slider = [firstPoint,firstPointRef];

        if (!ctx.family){
            if (latestCtx.family){
                ctx.family = latestCtx.family;
            }
            else{
                ctx.family = "iepg";
            }
        }

        if (!ctx.block_analize){
            if (latestCtx.block_analize){
                ctx.block_analize = latestCtx.block_analize;
            }
            else{
                ctx.block_analize = 0;
            }
        }

        // Save context
        ctxObj.saveContext();

        // update the latest context
        this.copyGlobalContextToLatestContext();
    },


    scrollChartDown: function(e){
        e.preventDefault();
        console.log("Scroll down");
        var _this = this;
        _this.zoom.y(100);
              _this.zoomed();
        
    },

    scrollChartUp: function(e){
        e.preventDefault();
        console.log("Scroll up");
    },

    changeBlockAnalysis: function(e){
        var $e= $(e.target);
        e.preventDefault();

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        ctx.block_analize = $e.attr("block-analyze") == "true" ? false : true;

          // Save context
        ctxObj.saveContext();

        // update the latest context
        this.copyGlobalContextToLatestContext();

        this._forceFetchDataTool = true;
        this.render();

    }
});