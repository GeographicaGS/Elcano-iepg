app.view.tools.CountryPlugin = app.view.tools.Plugin.extend({
	_template : _.template( $('#country_tool_template').html() ),
    type: "country",

    initialize: function(options) {
		this.slider = new app.view.tools.common.SliderSinglePoint({
            "plugin" : this
        });

		this.countries = new app.view.tools.common.Countries();

    },

    _events: {
       
    },

    _setListeners: function(){
        app.view.tools.Plugin.prototype._setListeners.apply(this);

        this.listenTo(app.events,"countryclick",function(id_country){
            //TOREMOVE
            console.log("countryclick at app.view.tools.CountryPlugin");

            var ctx = this.getGlobalContext();
            ctx.data.countries.selection = [id_country];
            ctx.saveContext();
            // The context has changed, let's store the changes in localStore
            this.getGlobalContext().saveContext();
            // Render again the countries with the new context
            this.render();
        });
    },


    /* Fetch data for the current country*/
	fetchData: function(){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;
            
        this.model = new app.model.tools.country({
            "id" : ctx.countries.selection[0],
            "year" : ctx.slider[0].date.getFullYear(),
            "variable" : ctx.variables[0]
        });

		// Fetch model from de server
        var self = this;
        this.model.fetch({
            success: function() {
                self.renderAsync();
            }
        });
	},

    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.CountryPlugin");
		
        var year =  this.getGlobalContext().data.slider[0].date.getFullYear();

        year = 2013;

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
            model: this.model.toJSON()[year],
        }));

        this.$chart = this.$(".chart");

        this._drawD3Chart();
    },

    renderMap: function(){
        //TODO
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    /* 
        This method adapt the glob
    */
    adaptGlobalContext: function(){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            latestCtxObj = this.getLatestContext(),
            latestCtx = latestCtxObj.data;

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
                ctx.countries.selection = [ctx.countries.list[0]];
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

        // update the latest context
        this.copyGlobalContextToLatestContext();
    },

    setURL: function(){
        // This method transforms the current context of the tool in a valid URL.
        //country/:id_country/:id_variable/:year
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            country = ctx.countries.selection[0],
            variable = ctx.variables[0],
            year = ctx.slider[0].date.getFullYear();


         app.router.navigate("country/" + country + "/" + variable + "/" + year, {trigger: false});
    },

    _drawD3Chart: function(){
        var width = this.$chart.width(),
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
            .attr("transform", "translate(" + width / 2 + "," + (height / 2 + 10) + ")");

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

        
        // d3.json("/flare.json", function(error, root) {
          
        // });

        var root = this._buildModelTree(),
            path = svg.selectAll("path")
              .data(partition.nodes(root))
            .enter().append("path")
              .attr("d", arc)
              .style("fill", function(d) { return color((d.children ? d : d.parent).name); })
              .on("click", click);

          function click(d) {
            path.transition()
              .duration(750)
              .attrTween("d", arcTween(d));
          }

    },

    _buildModelTree: function(year){

        var variables = this.model.get(year).iepg_variables;
        return {
            "name": "iepg",
            "children" : [{
                "name" : "economic_presence",
                "children": [{
                    "name" : "energy",
                    "size" : variables.energy.value
                },
                {
                    "name" : "primary_goods",
                    "size" : variables.primary_goods.value
                },
                {
                    "name" : "manufactures",
                    "size" : variables.manufactures.value
                },
                 {
                    "name" : "services",
                    "size" : variables.services.value
                },
                 {
                    "name" : "investments",
                    "size" : variables.investments.value
                }
                ]
            },{
                "name" : "military_presence",
                "children": [{
                        "name" : "troops",
                        "size" : variables.troops.value
                    },{
                        "name" : "military_equipment",
                        "size" : variables.military_equipment.value
                    }]
            },{
                "name" : "soft_presence",
                "children": [{
                        "name" : "migrations",
                        "size" : variables.migrations.value
                    },{
                        "name" : "tourism",
                        "size" : variables.tourism.value
                    },{
                        "name" : "sports",
                        "size" : variables.sports.value
                    },{
                        "name" : "culture",
                        "size" : variables.culture.value
                    },{
                        "name" : "information",
                        "size" : variables.information.value
                    },{
                        "name" : "technology",
                        "size" : variables.technology.value
                    },{
                        "name" : "science",
                        "size" : variables.science.value
                    },{
                        "name" : "education",
                        "size" : variables.education.value
                    },{
                        "name" : "cooperation",
                        "size" : variables.cooperation.value
                    }]
            }

            ]
        }
    },

    _drawD3Chart2: function(){

        var width = this.$chart.width(),
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
            .attr("transform", "translate(" + width / 2 + "," + (height / 2 + 10) + ")");

        var partition = d3.layout.partition()
            .value(function(d) { return d.size; });

        var arc = d3.svg.arc()
            .startAngle(function(d) { return Math.max(0, Math.min(2 * Math.PI, x(d.x))); })
            .endAngle(function(d) { return Math.max(0, Math.min(2 * Math.PI, x(d.x + d.dx))); })
            .innerRadius(function(d) { return Math.max(0, y(d.y)); })
            .outerRadius(function(d) { return Math.max(0, y(d.y + d.dy)); });

        d3.json("/flare.json", function(error, root) {
          var path = svg.selectAll("path")
              .data(partition.nodes(root))
            .enter().append("path")
              .attr("d", arc)
              .style("fill", function(d) { return color((d.children ? d : d.parent).name); })
              .on("click", click);

          function click(d) {
            path.transition()
              .duration(750)
              .attrTween("d", arcTween(d));
          }
        });

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
    }
    
});