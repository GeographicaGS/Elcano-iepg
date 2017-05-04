app.view.tools.RankingPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#ranking_tool_template').html() ),
    _templateNodataUE : _.template( $('#ranking_tool_error_ue_template').html() ),
    _templateHelp : _.template( $('#ranking_tool_help_template').html() ),
    type: "ranking",
    _dataMap : null,
    _refYear : true,

    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePointReference();
        this.countries = new app.view.tools.common.Countries();
    },

    _events: function(){
        return _.extend({},
            app.view.tools.Plugin.prototype._events.apply(this),
            {
               "click a[block-analyze]": "changeBlockAnalysis",
               "click .toggler": "_toggleRef"
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

            this._zoomToSelected();

            this.countries.render();

            this.saveAllContexts();

            this.contextToURL();

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

    _toggleRef: function(e){
        var $e = $(e.target)
        this._refYear = !$e.hasClass('enable');
        if (this._refYear){
            this.$('.chart').removeClass('noref');
            $e.addClass('enable');
        }
        else{
            this.$('.chart').addClass('noref');
            $e.removeClass('enable');
        }
    },

    /* Fetch data for the current country*/
    _fetchDataTool: function(){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        this.collection = new app.collection.RankingTool({},{

            "year" : ctxObj.getFirstSliderElement("Point").date.getUTCFullYear(),
            "yearRef" : ctxObj.getFirstSliderElement("PointReference").date.getUTCFullYear(),
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

    _renderBaseTemplate: function(drawerror){
        if (!drawerror) drawerror = false;

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
            drawerror : drawerror
        }));

        if (!drawerror){
            this._dataMap = new app.view.map({
                "container": "data_map",
                "zoom" : 1,
                "tooltip" : this.$("#ranking_map_tooltip")
            }).initialize();

            var family = this.getGlobalContext().data.family;
            if (family){
                if (family == 'iepg'){
                    this._dataMap.moveToWorld();
                }
                else if (family == 'iepe'){
                    //###48.224673, 12.304688
                    this._dataMap.moveToEurope();
                }
            }

            this.$chart = this.$(".chart");

            var h = this.$(".body").height()- this.$(".chart_header").outerHeight(true) - 18;
            this.$(".co_chart").height(h);

            this.$(".co_chart").css("top",this.$(".chart_header").outerHeight(true) + "px");
        }
        
    },

    _renderToolAsync: function(){

        this._forceFetchDataTool = false;

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            year = ctx.slider[0].date.getUTCFullYear(),
            variable = ctx.variables[0],
            family = ctx.family
            colJSON = this.collection.toJSON(),
            mapArray = [];

    
        this._renderBaseTemplate(colJSON.length==0);
       
        if (colJSON.length>0){

            this._drawD3Chart();

            for (var i=0;i<colJSON.length;i++){
           
                mapArray.push({
                    "code" : colJSON[i].code,
                    "value" : colJSON[i].currentRanking,
                });
            }

            this._dataMap.drawChoropleth(mapArray,year,variable,family,"º",true,null,true);

            this.mapLayer = app.map.drawChoropleth(mapArray,year,variable,family,"º",true,"Ranking ",true);
        }
        
    },

    resizeMe: function(){
        app.view.tools.Plugin.prototype.resizeMe.apply(this);
        this._renderToolAsync();
    },

    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.RankingPlugin");

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            year = ctx.slider[0].date.getUTCFullYear() ;

        // Remove previous map
        app.map.removeChoropleth();

        if (ctx.block_analize == 1 // country +UE
            && year<2005 // UE was included in the study at year 2005
            ){

            this._renderBaseTemplate(false);
            this.$chart.html(this._templateNodataUE({}));
            this.$("#scroll_up,#scroll_down,#ranking_chart_tooltip").remove();
            
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
            family = ctx.family,          
            countries = ctx.countries.list.length>0 ? ctx.countries.list.join(",") : "null",
            country_sel = ctx.countries.selection.length>0 ? ctx.countries.selection[0] : "null",
            variable = ctx.variables[0],
            year = ctx.slider[0].date.getUTCFullYear(),
            year_ref = ctx.slider[1].date.getUTCFullYear(),
            filters = app.getFilters().length ? "/" + app.getFilters().join(",") : "";
            url = "ranking/" + family + "/" + variable + "/" + year + "/" + year_ref + "/" + countries + "/" + country_sel + "/" + ctx.block_analize + filters;

        app.router.navigate(url,{trigger: false});
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

  
        ctx.countries.list = url.countries != "null" ? url.countries.split(",") : [];
        ctx.countries.selection = url.country_sel!= "null" ? [url.country_sel]: [];

        ctx.block_analize = url.block_analize ? url.block_analize : 0;

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
            max = !data[0].referenceValue || 
                    data[0].currentValue > data[0].referenceValue 
                    ?  data[0].currentValue 
                    : data[0].referenceValue,
            margin = {top: 60, right: 0, bottom: 30, left: 160},
            width = this.$chart.width() - margin.left - margin.right,
            barHeight = 20,
            totalCountryHeight = barHeight * 2 + 10 /*padding*/,
            height = (data.length+1) * totalCountryHeight - margin.top - margin.bottom - 10,
            yAxisWidth = 160,
            visibleHeight = this.$chart.height(),
            ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            year = ctxObj.getFirstSliderElement("Point").date.getUTCFullYear(),
            yearRef = ctxObj.getFirstSliderElement("PointReference").date.getUTCFullYear(),
            // get color variable
            colorVariable = app.view.tools.utils.variablesColors[
                ctx.variables[0] == "global" ?  ctx.family : ctx.variables[0]
            ];

        var x = d3.scale.linear()
            .range([0, width])
            .domain([0, max]);

        var y = d3.scale.linear()
            .range([0, height])
            .domain([1, data.length]);

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("top")
            .tickSize(-height)
            .tickFormat(function(d) { return app.formatNumber(d,0); });

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left")
            .tickSize(-width)
            .ticks(data.length);

        var zoom = d3.behavior.zoom()
            .y(y)
            .on("zoom", zoomed);

        if (height < this.$chart.height()){
            height  = this.$chart.height() - margin.top - margin.bottom;
        }

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

        var div = d3.select("#ranking_chart_tooltip") ;
      
        var obj = this;

        canvas.append("rect")
            .attr("width", this.$chart.width() )
            .attr("height", barHeight*2)
            .attr("id","selection_mark")
            .attr("style","fill:#a2a2ac;opacity:0.2")
            .attr("x", 0)
            .attr("y", 0);

        function barmousehover(d) {   
            div.transition()        
                .duration(200)      
                .style("opacity", 1);      
            
            div.html(obj._htmlChartToolTip(_.extend(d,{"year": year,"yearRef": yearRef})))  
            .style("left", (d3.event.pageX) + "px")     
            .style("top", (d3.event.pageY - 28) + "px");    
        }

        function barmouseout(d) {   
            div.transition()        
                    .duration(500)      
                    .style("opacity", 0);    
        }

        // Variable bars
        canvas.selectAll(".bar").data(data).enter().append("rect")
            .attr("class", "bar")
            .attr("x", yAxisWidth)
            .attr("width", function(d) { return x(d.currentValue); })
            .attr("style","fill:"+colorVariable)
            .attr("y", function(d) { return y(data.indexOf(d) + 1); })
            .attr("country",function(d){ return d.code;})
            .attr("height", barHeight)
            .on("mouseover", barmousehover)                  
            .on("mouseout", barmouseout);

        // References bars
        subset.enter().append("rect")
            .attr("class", "bar ref")
            .attr("x", yAxisWidth)
            .attr("width", function(d) { return x(d.referenceValue); })
            .attr("y", function(d) { return y(data.indexOf(d) + 1) + barHeight + 1; })
            .attr("height", barHeight)
            .on("mouseover", barmousehover)                  
            .on("mouseout", barmouseout);


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

        co_label.append("foreignObject")
            .attr("width", 100)
            .attr("height", 40)
            .attr("x",40)
          .append("xhtml:body")
            .html(function(d){
                return "<span class='labelcountry' title='" + app.countryToString(d.code) + "'>" + app.countryToShortString(d.code) + "</span>"
            });

        co_label.append("text")
            .attr("class","number")
            .attr("x",yAxisWidth - 20)
            .attr("y", 17)
            .attr("width",40)
            .text(function(d){ return d.currentRanking });


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

        this._d3Zoom = {};
        this._d3Zoom.zoom = zoom;
        this._d3Zoom.canvas = canvas;

        this._zoomToSelected();
    },

    _zoomToSelected: function(){

        var ctx = this.getGlobalContext(),
            id_country = ctx.data.countries.selection[0],
            el = d3.select("rect[country='"+id_country + "']");

        if (!el.empty()){
            var newzoom =  d3.select("rect[country='"+id_country + "']").attr("y")*1
                gap = this.$(".co_chart").height() / 2 - 50,
                newzoom_d3 = (newzoom - gap)*-1;

            if (newzoom_d3>0){
                newzoom_d3 = 0;
            }

            this._d3Zoom.zoom.translate([0,newzoom_d3]);
            this._d3Zoom.canvas.attr("transform", "translate(0," + (newzoom_d3) + ")");

            d3.select("#selection_mark").attr("y",newzoom);
        }
            

    },

    _htmlChartToolTip: function(d){
        var ctx = this.getGlobalContext().data,
            variable = ctx.variables[0],
            family = ctx.family;

            html = "<div class='block'>" 
                        + "<div class='line1'>" 
                        +   "<span class='title1'>" + d.currentRanking + app.ordchr(d.currentRanking) + " " +app.countryToString(d.code) + "</span>"
                        +   "<span class='value1'>" + d.year + "</span>"
                        + "</div>"
                        + "<div class='line2'>" 
                        +   "<span class='title2 uppercase'>" + app.variableToString(variable,family) + "</span>"
                        +   "<span class='value2'>" + app.formatNumber(d.currentValue) + "</span>"
                        +"</div>"
                    + "</div>";

        if (this._refYear){

            html += "<div class='block ref'>" 
                        + "<div class='line1'>" 
                        +   "<span class='title1'>" + d.referenceRanking + app.ordchr(d.referenceRanking) + " " +app.countryToString(d.code) + "</span>"
                        +   "<span class='value1'>" + d.yearRef + "</span>"
                        + "</div>"
                        + "<div class='line2'>" 
                        +   "<span class='title2 uppercase'>" + app.variableToString(variable,family) + "</span>"
                        +   "<span class='value2'>" + app.formatNumber(d.referenceValue) + "</span>"
                        +"</div>"
                    + "</div>";
        }

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
            ctx.countries.selection = ctx.countries.selection.slice(0,1);
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


    // scrollChartDown: function(e){
    //     e.preventDefault();
    //     console.log("Scroll down");
    //     var _this = this;
    //     _this.zoom.y(100);
    //           _this.zoomed();
        
    // },

    // scrollChartUp: function(e){
    //     e.preventDefault();
    //     console.log("Scroll up");
    // },

    changeBlockAnalysis: function(e){
        var $e= $(e.target).closest("a");
        e.preventDefault();

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        ctx.block_analize = $e.attr("block-analyze");

        // Save context
        this.saveAllContexts();

        this._forceFetchDataTool = true;
        this.render();

    }
});