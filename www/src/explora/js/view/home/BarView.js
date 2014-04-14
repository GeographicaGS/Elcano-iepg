app.view.BarView = Backbone.View.extend({
	_template : _.template($('#bar_template').html()),
	localCtx: {"countries":[{"name":"España", "symbol":"ESP"}] },
	initialize: function(){
		//getLocalCtx();
	    //this.$countrypanel = $("#country_panel");
	    return this.render();
	},
	render: function(){
		return this._template;
		// localCtx.countries.forEach(function(country){
		// 	renderCountry(country);
		// });
	},
	renderCountry: function(){
		
	},
	onClose: function(){
		this.stopListening();
	},
	addCountry: function(){
		
	}
});