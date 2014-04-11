app.view.ToolPluginView = Backbone.View.extend({
    ctx: null,

    initialize: function() {
       
    }, 
    
    readGlobalContext: function(){
        // leemos el conexto de la aplicacion
    },

    renderTool: function(){
        // draw the tool. This method must be overwritten
    },

    renderMap: function(){
        // draw the map. This method must be overwritten
    },

    configureSlider: function(){
        //this.slider.render();
    },

    configureCtx: function(){

    },

    render: function(){
//         this.renderTool();
//         this.renderMap();
//         this.configureCtx();
    },
    onClose: function(){
        // Remove events on close
       //this.stopListening();
    }
});






