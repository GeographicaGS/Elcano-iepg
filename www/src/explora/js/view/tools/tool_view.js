app.view.tools.Plugin = Backbone.View.extend({
    // Local context, it stores the global context used in the last render of the tool
    _latestCtx: null,
    el: "#tool_data",
    type: null,
    _forceFetchDataTool : true,
    _forceFetchDataMap : true,

    initialize: function() {
        this.slider = new app.view.tools.common.Slider();
        this.countries = new app.view.tools.common.Countries();
    }, 
    
   
    // Don't use Backbone events property.
    // The reason for that is that we've several tools in memory at the same time, all the tools share the same DOM element.
    // Events are apply on render and disable on hideTool
    _events: function (){
        return {
            "change #ctrl_family" : "_changeFamily",
            "click a.helpIcon": "launchHelp"
        };
    },

    _changeFamily: function(e){
        var f = $(e.target).val();

        // Let's modify the context with the current family
        var ctx = this.getGlobalContext();
        ctx.data.family = f;
        ctx.saveContext();
        
        // Copy the global context to the latest
        this.copyGlobalContextToLatestContext();

        // Fire the contextchange event
        app.events.trigger("contextchange:family");
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
           
            this._forceFetchDataTool = true;
            this._forceFetchDataMap = true;
            // Render again
            this.render();
        });

        this.listenTo(app.events,"contextchange:family",function(){
            //TOREMOVE
            console.log("contextchange:family at app.view.tools.Plugin");
           
            this._forceFetchDataTool = true;
            this._forceFetchDataMap = true;
            // Render again
            this.render();
        });

        this.listenTo(app.events,"slider:singlepointclick",function(year){
            console.log("slider:singlepointclick at app.view.tools.Plugin");
            var ctx = this.getGlobalContext();
            ctx.data.slider = [{
                "date" : new Date(year),
                "type" : "Point"
            }];

            // Render again the tool 
            this._forceFetchDataTool = false;
            this._forceFetchDataMap = true;

            this.render();
        });

        this.listenTo(app.events,"variable:changed",function(variable){
            var ctx = this.getGlobalContext();
            ctx.data.variables = [variable];

            // Render again the tool 
            this._forceFetchDataTool = true;
            this._forceFetchDataMap = true;

            this.render();
        });

    },


    // Here methods which should be overwritten by the child class.
    contextToURL: function(){
        // This method should be overwritten. 
        // It transforms the current context of the tool in a valid URL.
    },

    URLToContext: function(url){
        // It transforms the current URL in a valid context.
    },

    /*
        This method must be overriden. It adapts the global context for the tool.
        The global context will be analyzed and it will be update with the required properties of each tool.
        That required properties will be recover from the localContext if exist, if not these properties will have the default values.
    */
    adaptGlobalContext: function(){
        
    },

    /* 
        DEPRECATED
        Recover data from a server. It always should call to renderAsync when the data is received.
        RenderMap and RenderTool are called by RenderAsync, but it should be called only when data is received.
     */
    // fetchData: function(){
    //     // This method must be overwritten.
    //     this.renderAsync();
    // },

    /* Render the tool, here the code to render the tool data. Lots of work here, so should have the data before call this method */
    renderTool: function(){
        // Draw the tool. This method must be overwritten
        this.$el.html("Generic tool");      

        return this;  
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
        var latestCtx = this.getLatestContext();
        latestCtx.data = $.extend(true, {}, this.getGlobalContext().data);  
        // save context in local store   
        latestCtx.saveContext();

        return this;

    },  

    /* This method save all context in localstore */
    saveAllContexts : function(){
        this.getGlobalContext().saveContext();
        this.copyGlobalContextToLatestContext();

        return this;
    },

    /* 
        Put a tool in foreground.
        This is the entry point to render a tool, it prepares the listeners
    */ 
    bringToFront: function(){
        this._setListeners();
        this.delegateEvents(this._events()); 
        this.slider.bringToFront();
        this.countries.bringToFront();
        this.render();

        return this;
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

        return this;
    },

    /* 
        Draw the tool
    */ 
    render: function(){  
        this.adaptGlobalContext();
        this.contextToURL();
        this.$el.show().html(app.getLoadingHTML());

        this.slider.render();
        this.countries.render();

        this.renderTool();

       

        return this;
    },

    forceFetchDataOnNextRender: function(){
        this._forceFetchDataTool = true;
        this._forceFetchDataMap = true;

        return this;
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

    /* 
        DEPRECATED USE  forceFetchDataOnNextRender + render
        Refresh the tool. A new data request is performed. This will redraw Map and Tool. */
    // refresh: function(){
    //     this.fetchData();
    // },

    clearMap: function(){
        
    },

    launchHelp: function(e){
        e.preventDefault();

        if (this._templateHelp){
            var opts = app.fancyboxOptsHelper();
    
        
            opts["afterShow"] = function () {
                $("#cancel").click(function(e){
                    e.preventDefault();
                    $.fancybox.close();
                });
            };
            
            $.fancybox(this._templateHelp(), opts);    
        }

        
    }





});






