app.view.tools.Plugin = Backbone.View.extend({
    ctx: null,
    el: "#tool",

    initialize: function() {
        this.slider = new app.view.tools.common.Slider();
        this.countries = new app.view.tools.common.Countries();
    }, 
    
    fetchData: function(){
        // This method must be overwritten.
        this.renderAsync();
    },

    getGlobalContext: function(){
        // Read the global context
        return app.getGlobalContext();
    },

    getLocalContext: function(){
        // Read the local context
        if (!this.ctx){
            // If the context is not defined, let's get it from local storage.
            this.ctx = _.clone(app.getGlobalContext());
        }
        return this.ctx;
    },

    // This method modifies the global context with the values in the local context.
    // It also stores the new context in localStorage.
    copyToGlobalContext: function(){
        app.context.setContext(this.ctx);
    },  

    renderTool: function(){
        // Draw the tool. This method must be overwritten
        this.$el.html("Generic tool");        
    },

    renderMap: function(){
        // draw the map. This method must be overwritten
    },

    hideCountryBar : function(){
        this.slider.el.hide();
    },

    showCountryBar : function(){
        this.slider.el.show();
    },

    toggleCountryBar: function(){
        if (this.slider.is(":visible")){
            this.hideCountryBar();
        }
        else{
            this.showCountryBar();
        }
    },

    hideTool: function(){

    },

    renderAsync: function(){
        // render Tool and render Map need data to work. So this will be called asynchronously
        this.renderTool();
        this.renderMap();
    },

    render: function(){  
        this.$el.html("Loading");
        this.fetchData();
        this.slider.render();
        this.countries.render();
    },

    onClose: function(){
       // Remove events on close
       this.stopListening();
    },

    // Refresh the tool. A new data request is performed. This will redraw Map and Tool.
    refresh: function(){
        this.fetchData();
    }
});






