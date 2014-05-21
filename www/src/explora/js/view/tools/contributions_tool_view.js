app.view.tools.ContributionsPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#contributions_tool_template').html() ),
    // Force fetch data of the left tool. Get the data for the first country
    _forceFetchDataSubToolLeft: false,
    // Force fetch data of the right tool. Get the data for the second country
    _forceFetchDataSubToolRight: false,

    models : { "es" : null, "en" : null },

    type: "contributions",
    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePoint();
        this.countries = new app.view.tools.common.Countries({
            "variable" : false
        });
    },

    setURL: function(){
        app.router.navigate("tool/contributions",{trigger: false});
    },

    _setListeners: function(){
        app.view.tools.Plugin.prototype._setListeners.apply(this);

        this.listenTo(app.events,"slider:singlepointclick",function(year){
            var ctx = this.getGlobalContext();
            ctx.data.slider = [{
                "date" : new Date(year),
                "type" : "Point"
            }];
            ctx.saveContext();
            // The context has changed, let's store the changes in localStore
            this.getGlobalContext().saveContext();
            // Render again the tool without fetch data
            this.render(false);
        });
    },

    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.ContributionsPlugin");

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;
            year = ctx.slider[0].date.getFullYear()

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
        }));

        this.$co_left = this.$("#co_chart_left");
        this.$co_right = this.$("#co_chart_right");

        this.$chart_left = this.$co_left.find(".chart");
        this.$chart_right = this.$co_right.find(".chart");

        this.$chart_left.html("");
        this.$chart_right.html("");

        // Get the data from server if _forceFetchDataTool is set to true. If _forceFetchDataTool is set to false data is not requested to server
        if (this._forceFetchDataTool){
            this._forceFetchDataSubToolLeft = true;
            this._forceFetchDataSubToolRight = true;
        }
        
        this._renderSubTool("left");
        this._renderSubTool("right");

        this.renderMap();
    },

    _renderSubTool:function(pos){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            selection = ctx.countries.selection,
            // get correct force fecth variable
            forceFetch = pos == "left" ? this._forceFetchDataSubToolLeft : this._forceFetchDataSubToolRight,
            // Index 0 is for left position, index 1 is for right position
            country = pos == "left" ? (selection.length > 0 ? selection[0] : null) :  
                                        (selection.length > 1 ? selection[1] : null),

            // Links to DOM Elements
            $co_chart = pos == "left" ? this.$co_left : this.$co_right,
            $country_sel = $co_chart.find(".country_sel"),
            $country_nosel = $co_chart.find(".country_nosel"),
            $country_name = $co_chart.find(".name");
            
            if (country){
                // Set the country name
                $country_name.html(app.countryToString(country));
                // Hide the nosel div
                $country_nosel.hide();
                // Show the sel div
                $country_sel.show();

                if (forceFetch){
                    // Fetch the data of this tool
                    this.models[pos] = new app.model.tools.country({
                        "id" : country,
                        "family" : ctx.family
                    });

                    var _this = this;
                    this.models[pos].fetch({
                        success: function(){
                           _this._drawD3Chart(pos,country,_this.models[pos]);
                        }
                    });

                }
                else{
                    //We already have the data, let's draw directly
                    this._drawD3Chart(pos,country,this.models[pos]);
                }
            }
            else{
                // Hide the selection div
                $country_sel.hide();
                // Show de no selection div. Just to inform user of drag.
                $country_nosel.show();
            }

    },

    renderMap: function(){
        // draw the map
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


    _drawD3Chart: function(pos,country,model){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            year = ctx.slider[0].date.getFullYear(),
            variables = model.get(year).iepg_variables,
            $chart = pos == "left" ? this.$co_left : this.$co_right,
            width = $chart.width(),
            height = $chart.height(),
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

        var div = d3.select("body").append("div")   
        .attr("class", "tooltip")               
        .style("opacity", 0);

        var obj = this;

        var root = this._buildModelTree(variables),
            path = svg.selectAll("path")
              .data(partition.nodes(root))
            .enter().append("path")
              .attr("d", arc)
              .style("fill", function(d) { return d.color; })
            .on("click", click)
            .on("mouseover", function(d) {     
                div.transition()        
                    .duration(200)      
                    .style("opacity", 1);      
                div.html(obj._htmlToolTip(model.get(year).iepg_variables[d.name]))  
                    .style("left", (d3.event.pageX) + "px")     
                    .style("top", (d3.event.pageY - 28) + "px");    
                })                  
            .on("mouseout", function(d) {       
                div.transition()        
                    .duration(500)      
                    .style("opacity", 0);   
            });
        

            function click(d) {
                if (d.name == "iepg" || d.name == "economic_presence" ||
                    d.name == "soft_presence" || d.name =="military_presence")
                {
                    path.transition()
                        .duration(750)
                        .attrTween("d", arcTween(d));
                    //obj._renderChartLegend(year,d.name);
                }
          }
    },

    _htmlToolTip: function(variable){
        
        var html = "<div>" 
                    +   "<span>" + variable.ranking + "º " +app.countryToString(variable.code) + "</span>"
                    +   "<span>" + variable.year + "</span>"
                    +   "<div class='clear'></div>"
                    + "</div>"
                    + "<div>" 
                    +   "<span>" + variable.variable + "</span>"
                    +   "<span>" + sprintf("%0.2f",variable.value) + "</span>"
                    +   "<div class='clear'></div>"
                    +"</div>"

        return html;

    },

    _buildModelTree: function(variables){

        return {
            "name" : "iepg",
            "color" : "#fdc300",
            "size" : variables.iepg.value,
            "children" : [{
                "name" : "economic_presence",
                "color" : "#2b85d0",
                "size" : variables.economic_presence.value,
                "children": [{
                    "name" : "energy",
                    "size" : variables.energy.value,
                    "color" : "#4191d5"
                },
                {
                    "name" : "primary_goods",
                    "size" : variables.primary_goods.value,
                    "color" : "#559dd9"
                },
                {
                    "name" : "manufactures",
                    "size" : variables.manufactures.value,
                    "color" : "#6baade"
                },
                 {
                    "name" : "services",
                    "size" : variables.services.value,
                    "color" : "#80b6e3"
                },
                {
                    "name" : "investments",
                    "size" : variables.investments.value,
                    "color" : "#95c2e7"
                }
                ]
            },{
                "name" : "military_presence",
                "color" : "#669900",
                "size" : variables.military_presence.value,
                "children": [{
                        "name" : "troops",
                        "size" : variables.troops.value,
                        "color" : "#76a318"
                    },{
                        "name" : "military_equipment",
                        "size" : variables.military_equipment.value,
                        "color" : "#85ad33"

                    }]
            },{
                "name" : "soft_presence",
                "color" : "#ff9000",
                "size" : variables.soft_presence.value,
                "children": [{
                        "name" : "migrations",
                        "size" : variables.migrations.value,
                        "color" : "#ff960d",
                    },{
                        "name" : "tourism",
                        "size" : variables.tourism.value,
                        "color" : "#ff9b1a"
                    },{
                        "name" : "sports",
                        "size" : variables.sports.value,
                        "color" : "#ffa126"
                    },{
                        "name" : "culture",
                        "size" : variables.culture.value,
                        "color": "#ffa633"
                    },{
                        "name" : "information",
                        "size" : variables.information.value,
                        "color" : "#ffac40"
                    },{
                        "name" : "technology",
                        "size" : variables.technology.value,
                        "color" : "#ffb24d"
                     },{
                        "name" : "science",
                        "size" : variables.science.value,
                        "color" : "#ffb759"
                    },{
                        "name" : "education",
                        "size" : variables.education.value,
                        "color" : "#ffbc66"
                    },{
                        "name" : "cooperation",
                        "size" : variables.cooperation.value,
                        "color" : "#ffc273"
                    }]
            }

            ]
        }
    },

    _extractNodeFromTree: function(year,name){
        var nodes = this. _buildModelTree(year);
        if (name == "iepg"){
            return nodes;
        }
        else{
            nodes = nodes.children;
        }
       
        // find the node in the childrens
        for(var i=0;i<nodes.length;i++){
            if (nodes[i].name == name){
                return nodes[i];
            }
        }

        return null;
    },

    // _renderChartLegend: function(year,name){

    //     this.$chart_legend.html(this._templateChartLegend({
    //         data: this._extractNodeFromTree(year,name)
    //     }));

    // }
});