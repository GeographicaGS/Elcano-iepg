app.view.CardToolPluginView = app.view.ToolPluginView.extend({
	
data : {
	"name":"España",
	"mode":"card",
	"presence_year":"2011",
	"presence":"152.3",
	"presence_index":"11º",
	"pib":"1.388.789.000.000",
	"pib_index":"14º",
	"population":"46.196.276",
	"population_year":"2012",
	"population_index":"27º",
	"desc":"Lorem ipsum"
},

	initialize: function(){
		// this.slider = new app.view.common.SliderSinglePoint();
		console.log('adadasd');
	}, 
	renderTool: function(){  
	//	console.log("entra");
		// return app.view.ToolPluginView.prototype.render.call();
	},
	renderMap: function(){  
		// draw the map 
	},
	onClose: function(){
		//this.stopListening();
	}
});
