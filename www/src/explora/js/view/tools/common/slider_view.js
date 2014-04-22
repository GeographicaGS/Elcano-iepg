app.view.tools.common.Slider = Backbone.View.extend({
    el: "#slider",
    dataGlobalCtx: null,
    dataLocalCtx: null,
    
    initialize: function(options){
        this.plugin = options.plugin;
        this.dataGlobalCtx = this.plugin.getGlobalContext().slider;
        this.dataLocalCtx = this.plugin.getLocalContext().slider;
    },

	render: function(){

    },

    onClose: function(){
        // Remove events on close
        this.stopListening(); 
    } 	
}); 