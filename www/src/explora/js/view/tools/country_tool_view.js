app.view.tools.CountryPlugin = app.view.tools.Plugin.extend({
	_template : _.template( $('#country_tool_template').html() ),

    initialize: function() {
		this.slider = new app.view.tools.common.SliderSinglePoint({
			"plugin": this
		});

		this.countries = new app.view.tools.common.Countries();

		this.model = new app.model.tools.country({
			"id" : "ESP",
			"year" : new Date(this.getGlobalContext().slider.current).getFullYear()
		});

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
            ctx: this.getGlobalContext(),
            model: this.model.toJSON(),
        }));
    },

    renderMap: function(){
        // draw the map
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    }
});