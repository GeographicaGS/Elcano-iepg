app.view.tools.Plugin = Backbone.View.extend({
    // Local context, it stores the global context used in the last render of the tool
    _latestCtx: null,
    el: "#tool_data",
    type: null,

    initialize: function() {
        this.slider = new app.view.tools.common.Slider();
        this.countries = new app.view.tools.common.Countries();
    }, 
    
   
    // Don't use Backbone events property.
    // The reason for that is that we've several tools in memory at the same time, all the tools share the same DOM element.
    // Events are apply on render and disable on hideTool
    _events: {
        
    },

    /* 
        Set listener of the tool in this method.
        Here will place the listeners that all plugin shares.
        To add more listener, extend this method and call the parent (app.view.tools.Plugin.prototype._setListeners.apply(this);)
    */
    _setListeners: function(){
        this.listenTo(app.events,"contextchange:countries",function(){
            //TOREMOVE
            console.log("contextchange:countries at app.view.tools.Plugin");
            // The context has changed, let's store the changes in localStore
            this.getGlobalContext().saveContext();
            // Render again
            this.render();
        });

    },


    // Here methods which should be overwritten by the child class.
    setURL: function(){
        // This method should be overwritten. 
        // It transforms the current context of the tool in a valid URL.
    },

    /*
        This method must be overriden. It adapts the global context for the tool.
        The global context will be analyzed and it will be update with the required properties of each tool.
        That required properties will be recover from the localContext if exist, if not these properties will have the default values.
    */
    adaptGlobalContext: function(){
        
    },

    /* 
        Recover data from a server. It always should call to renderAsync when the data is received.
        RenderMap and RenderTool are called by RenderAsync, but it should be called only when data is received.
     */
    fetchData: function(){
        // This method must be overwritten.
        this.renderAsync();
    },

    /* Render the tool, here the code to render the tool data. Lots of work here, so should have the data before call this method */
    renderTool: function(){
        // Draw the tool. This method must be overwritten
        this.$el.html("Generic tool");        
    },

    /* Render the map, here the code to render the map data. Lots of work here, so should have the data before call this method */
    renderMap: function(){
        // draw the map. This method must be overwritten
    },

    // End methods to overwrite

    getGlobalContext: function(){
        // Read the global context
        return app.context;
    },

    getLatestContext: function(){
        // Read the local context, try first in memory if not go to local store
        if (!this._latestCtx){
            this._latestCtx = new app.view.tools.context(this.type);
            this._latestCtx.restoreSavedContext();
        }

        return this._latestCtx;
    },

    /* This method copy the global context to the latest context of the tool*/ 
    copyGlobalContextToLatestContext: function(){
        this._latestCtx.data = $.extend(true, {}, this.getGlobalContext().data);  
        // save context in local store   
        this._latestCtx.saveContext();

    },  

    /* This method save all context in localstore */
    saveAllContexts : function(){
        this.getGlobalContext().saveContext();
        this.copyGlobalContextToLatestContext();
    },

    /* 
        Put a tool in foreground.
        This is the entry point to render a tool, it prepares the listeners
    */ 
    bringToFront: function(){
        this._setListeners();
        this.delegateEvents(this._events); 
        this.slider.bringToFront();
        this.countries.bringToFront();
        this.render();
    },

    /* 
        This method move a tool to background.
        It disable all the listeners.
    */ 
    bringToBack: function(){
        this.undelegateEvents();
        this.slider.bringToBack();
        this.countries.bringToBack();
        this.stopListening();
        this.clearMap();
    },

    /* NEVER CALL RENDER directly, Use bringToFront.
        DONT' OVERWRITTE THIS METHOD
    */ 
    render: function(){  
        this.adaptGlobalContext();
        this.setURL();
        this.$el.show().html("Loading");

        this.renderTool();
        this.renderMap();

        this.slider.render();
        this.countries.render();
    },

    onClose: function(){
       //call when close the view
    },

    /* Close the tool, leverage all the resources */ 
    close: function(){
        this.stopListening();

        this.$el.html("").hide();

        if (this.onClose){
            this.onClose();
        }

        this.slider.close();
        this.countries.close();
        this.clearMap();
    },

    /* Refresh the tool. A new data request is performed. This will redraw Map and Tool. */
    refresh: function(){
        this.fetchData();
    },

    clearMap: function(){
        
    }



});






