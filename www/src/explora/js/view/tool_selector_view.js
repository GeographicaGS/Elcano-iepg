app.view.ToolSelector = Backbone.View.extend({
    _template : _.template( $('#tool_selector_template').html() ),
    // Stack to stored the selection stack
    _toolsSelectedStack : null,
    initialize: function(options){

        var self = this;

        var opts = app.fancyboxOpts();
        opts["afterLoad"] = function () {
            self.render();
        }

        $.fancybox(this.$el, opts);

        this._toolsSelectedStack = [];

        // Add tools to the stack.
        for (var i=0;i<app.baseView.getTools().length;i++){
            var tool = app.baseView.getTools()[i];
            // Don't add the current tool, this will be added at the top
            if (app.baseView.currentTool != tool){
                this._toolsSelectedStack.push(tool.type)
            }
        }

        // at the current tool at the top of the stack
        if (app.baseView.currentTool){
            this._toolsSelectedStack.push(app.baseView.currentTool.type);    
        }

        $(window).on('resize', function(){
            self.render();
        });

        //this.render();
    },

    events : {
        "click #save": "save",
        "click #cancel": "cancel",
        "click a[tool]" : "clickTool"
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    
        $(window).off('resize');
    },

    render: function(){
        console.log("Render app.view.ToolSelector");

        this.$el.html(this._template({
            ctx: app.context.data,
        }));
  
        this.$n_selected = this.$("#n_selected");
        this.refreshCounterElements();
        return this;
    },

    cancel: function(){
        $.fancybox.close();
        app.events.trigger("closepopup",this);
    },

    save: function(){
        $.fancybox.close();
        
        // var ctx =  app.context;
        // ctx.data.countries.list = $.map(this.$(".co_selectable_tools a[selected]"),function(e) { return $(e).attr("tool") });
        // ctx.removeInvalidSelected();

        app.events.trigger("closepopup",this);

        var tools_sel = $.map(this.$(".co_selectable_tools a[selected]"),function(e) { return $(e).attr("tool") }),
            tools_nosel = $.map(this.$(".co_selectable_tools a:not([selected])"),function(e) { return $(e).attr("tool") }),
            // the current tool is the tool at the top of the stack
            currentTool = this._toolsSelectedStack.length > 0 ?  this._toolsSelectedStack[this._toolsSelectedStack.length -1] : null;  

        // remove no selected tools which are loaded
        for (var i=0;i<tools_nosel.length;i++){
            var tool = app.baseView.getToolByType(tools_nosel[i]);
            if (tool){
                app.baseView.removeTool(tool);
            }
        }

        // add sel tool which are no loaded
        for (var i=0;i<tools_sel.length;i++){
            var tool = app.baseView.getToolByType(tools_sel[i]);
            if (!tool){
                tool = app.baseView.getInstanceViewByType(tools_sel[i]);
                app.baseView.addTool(tool);
            }
        }

        // move to front the current tool
        if (currentTool){
            app.baseView.bringToolToFront(app.baseView.getToolByType(currentTool));
        }

    },

    refreshCounterElements: function(){
        var n = this.$(".co_selectable_tools a[selected]").length;

        var html = "";

        if (n === 0){
            html = "<lang>No hay herramientas seleccionadas</lang>";
        }
        else if (n==1){
            html ="<lang>1 herramienta seleccionada</lang>";
        }
        else{
            html = sprintf("<lang>%d herramientas seleccionadas</lang>",n);   
        }
        
        this.$n_selected.html(html);

    },

    _removeToolFromStack: function(tool){
        var index = this._toolsSelectedStack.indexOf(tool);
        if (index > -1) {
            this._toolsSelectedStack.splice(index, 1);
        }
    },

    _addToolToTopStack: function(tool){
        // If exists let's remove the tool from stack 
        this._removeToolFromStack(tool);
        this._toolsSelectedStack.push(tool);
    },

    clickTool: function(e){
        e.preventDefault();
        var $e = $(e.target).closest("a"),
            sel = $e.attr("selected"),
            tool = $e.attr("tool");

        if (sel !== undefined && sel!="undefined"){
            // Unselect element
            $e.removeAttr("selected");
            this._removeToolFromStack(tool);
        } 
        else{
            $e.attr("selected",true);
            this._addToolToTopStack(tool);

        }

        this.refreshCounterElements();
    }


    

});