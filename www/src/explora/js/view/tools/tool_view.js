app.view.tools.Plugin = Backbone.View.extend({
    ctx: null,
    el: "#tool_data",

    initialize: function() {
        this.slider = new app.view.tools.common.Slider();
        this.countries = new app.view.tools.common.Countries();
    }, 
    
    fetchData: function(){
        // This method must be overwritten.
        this.renderAsync();
    },

    // Don't use Backbone events property.
    // The reason for that is that we've several tools in memory at the same time, all the tools share the same DOM element.
    // Events are apply on render and disable on hideTool
    _events: {
        
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

    hideTool: function(){
        this.undelegateEvents();
    },

    renderAsync: function(){
        // render Tool and render Map need data to work. So this will be called asynchronously
        this.renderTool();
        this.renderMap();
    },

    render: function(){  
        this.delegateEvents(this._events); 
        this.$el.show().html("Loading");
        this.fetchData();
        this.slider.render();
        this.countries.render();
    },

    onClose: function(){
       //call when close the view
    },

    close: function(){
        this.stopListening();

        this.$el.html("").hide();

  
        if (this.onClose){
            this.onClose();
        }

        this.slider.close();
        this.countries.close();
    },

    // Refresh the tool. A new data request is performed. This will redraw Map and Tool.
    refresh: function(){
        this.fetchData();
    }
});






