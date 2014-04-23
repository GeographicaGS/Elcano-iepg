app.view.tools.Plugin = Backbone.View.extend({
    // Local context, it stores the global context used in the last render of the tool
    _latestCtx: null,
    el: "#tool_data",
    type: null,

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
        return app.context;
    },

    getLatestContext: function(){
        // Read the local context
        if (!this._latestCtx){
            this._latestCtx = new app.view.tools.context();
            // If the context is not defined, let's get it from local storage.
            this._latestCtx.data = localStorage.getItem("latest_context_" + this.type);

            if (!this._latestCtx.data){
                this.copyGlobalContextToLatestContext();
            }
        }

        return this._latestCtx;
    },

    prepareForRender: function(){
        // This method must be overriden. It prepares the tool for render.
        // The global context will be analyzed and it will be update with the required properties of each tool.
        // That required properties will be recover from the localContext if exist, if not these properties will have the default values.
    },


    copyGlobalContextToLatestContext: function(){
        //     app.context.setContext(this.ctx);
        //this._latestCtx.data = _.clone(this.getGlobalContext().data);
        this._latestCtx.data = $.extend(true, {}, this.getGlobalContext().data);
         
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
        this.prepareForRender();
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






