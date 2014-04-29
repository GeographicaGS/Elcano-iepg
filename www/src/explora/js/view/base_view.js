app.view.Base = Backbone.View.extend({
    el: "#base",
    tools :[],
    currentTool : null,
    initialize: function() {  

        this.$tool = $("#tool");
        // Let's save the original left, this will be modified by animations in toggleTools
        this.originLeft =  this.$tool.offset().left;

        this.$control_panel = this.$("#control_panel");
        this.$panelTools = this.$control_panel.find("ul");

        // Load default tools
        var localTools =  localStorage.getItem("tools");

        if (localTools){
            localTools = JSON.parse(localTools);
            listTools = localTools.tools;
            for (var i=0;i<listTools.length;i++){
                var tool = this._getInstanceViewByType(listTools[i]);
                var bringToFront = listTools[i] == localTools.selected ? true : false;
                this.addTool(tool,bringToFront);
            }
        }
        else{
            // if no information in local store load the country tool
            tool = new app.view.tools.CountryPlugin();
            this.addTool(tool,true);

            tool = new app.view.tools.RankingPlugin();
            this.addTool(tool,true);
        }
    },

    events: {
        "click #ctrl_tool" : "toggleTools",
        //"click #control_panel a" : "goToVisible",
        "click .header_tool .close": "removeCurrentTool"
    },

    render: function() {
        // TOREMOVE
        console.log("Render app.view.Base");
        var html = "";
        for (var i=0;i<this.tools.length;i++){
            var sel = this.currentTool == this.tools[i] ? "selected" : "";
            html += "<li " + sel + "><a href='" + app.getJSURL("tool/" + this.tools[i].type) + "' jslink>" + (i+1) + "</a></li>";
        }

        this.$panelTools.html(html);

        // refresh the tools panel
        return this;
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
        for (var i=0;i<this.tools.length;i++){
            this.tools[i].close();
        }
    },
    
    addTool: function(tool,bringToFront){
        console.log("Add tool "+ tool.type);
         // Just for security
        if (!tool) return;

        // Never add a tool twice
        if (this.tools.indexOf(tool) == -1){
            this.tools.push(tool);    
        }

        if (bringToFront){
            this.currentTool = tool;
            this.currentTool.bringToFront();
        }

        this.render();

        // save the tool status in localstore
        this.saveToolStatus();
        
        return this;
    },

    removeCurrentTool: function(e){
        e.preventDefault();
        this.removeTool(this.currentTool);
    },

    removeTool: function(tool){

        if (!tool){
            // Just for security
            return;
        }

        tool.close();

        var index = this.tools.indexOf(tool);
        if (index > -1) {
            this.tools.splice(index, 1);
        }

        if (this.currentTool==tool ){
            // We've remove the view on the viewport.
            // Let's try to load the first view
            if (this.tools.length>0){
                this.currentTool = this.tools[0];
                this.render();    
            }
            else{
                // The latest tool has been removed. 
                this.currentTool = null;
                this.render();
            }
        }

        // save the tool status in localstore
        this.saveToolStatus();
    },

    toggleTools: function(e){

        var $e = $(e.target),
            ml;

        if ($e.hasClass("open")){
            // hide tool panel
            $e.removeClass("open");
            ml = this.$tool.width() * -1;

            this.$tool.find("#tool_data").width( $(window).width() -  this.originLeft - 20).height();

            this.$tool.animate({"left": ml});
            this.$control_panel.fadeOut(300);
        }

        else{
            $e.addClass("open");
            
            this.$control_panel.fadeIn(300);
            var self = this;
            this.$tool.animate({"left": this.originLeft},function(){
                console.log("complete");
                $(this).find("#tool_data").css('width', 'auto')
            });
        }

        return this;
    },

    bringToolToFront: function(tool){
        // Just for security
        if (!tool) return;

        if (this.currentTool){
            // move to back the current tool
            this.currentTool.bringToBack();
        }
        this.currentTool = tool;
        this.currentTool.bringToFront();

        // let's call render to update the menu
        this.render();
    },

    _getInstanceViewByType: function(type){
        switch(type)
        {
            case "country":
                return new app.view.tools.CountryPlugin();
            case "ranking":
                return new app.view.tools.RankingPlugin();
        }

    },
    bringToolToFrontByType: function(type){
        var tool = this._searchToolByType(type);
        if (!tool){
            // The user has requested a tool but it's not loaded. Let's load it.
            tool = this._getInstanceViewByType(type);
            this.addTool(tool,true);
        }
        else{
            this.bringToolToFront(tool);    
        }

        
        return this;
    },

    _searchToolByType: function(type){
        for (var i=0;i<this.tools.length;i++){
            if (this.tools[i].type == type){
                return this.tools[i];
            }
        }

        return null;
    },

    loadCountryTool: function(id_country,id_variable,year){
        var ctx = app.context,
            // First check if the tool is already loaded
            tool = this._searchToolByType("country");

        
        // is the current country in the global context? 
        if (ctx.data.countries.list.indexOf(id_country)==-1){
            // This country is not in the global context. Let's add it
            ctx.data.countries.list.push(id_country);
        }

        if (ctx.data.countries.selection.length!=1 || ctx.data.countries.selection[0] !=id_country){
            // This country is not selected in the current context
            ctx.data.countries.selection = [id_country];
        }

        ctx.data.variables[0] = id_variable;
        ctx.data.countries.slider = [{
            "type": "Point",
            "date" : new Date(year + "01-01")
        }];

        // let's store the context.
        ctx.saveContext();

        if (!tool){
            // tool not already loaded
            tool = new app.view.tools.CountryPlugin();
            this.addTool(tool,true);
        }
        else{
            this.bringToolToFront(tool);   
        }
    },

    // This method will be called when a tool is added or removed
    saveToolStatus: function(){
        localStorage.setItem("tools",
            JSON.stringify({
                "tools" : _.map(this.tools, function(t){ return t.type; }),
                "selected" : this.currentTool ? this.currentTool.type : "" 
            })   
        );
    }
});