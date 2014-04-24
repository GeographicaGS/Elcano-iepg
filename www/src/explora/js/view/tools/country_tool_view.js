app.view.tools.CountryPlugin = app.view.tools.Plugin.extend({
	_template : _.template( $('#country_tool_template').html() ),
    type: "country",

    initialize: function(options) {
		this.slider = new app.view.tools.common.SliderSinglePoint({
            "plugin" : this
        });

		this.countries = new app.view.tools.common.Countries({
            "plugin" : this
        });
    },

    _events: {
       
    },

	fetchData: function(){
		// Fetch model from de server
        var self = this;
        this.model.fetch({
            success: function() {
                self.renderAsync();
            }
        });
	},

    renderTool: function(){
		this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
            model: this.model.toJSON()
        }));
    },

    renderMap: function(){
        // draw the map
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    prepareForRender: function(){

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

        this.model = new app.model.tools.country({
            "id" : ctx.countries.selection[0],
            "year" : ctx.slider[0].date.getFullYear(),
            "variable" : ctx.variables[0]
        });
    }
});