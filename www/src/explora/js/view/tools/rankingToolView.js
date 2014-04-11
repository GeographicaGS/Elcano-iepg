app.view.RankingToolPluginView = app.view.ToolPluginView.extend({
    initialize: function() {
     //   this.slider = new app.view.common.SliderSinglePoint();
    },

    renderTool: function(){
		//return app.view.ToolPluginView.prototype.render.call();
    },

    renderMap: function(){
        // draw the map
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    }
});