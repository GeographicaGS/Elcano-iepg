var map;

app.view.Base = Backbone.View.extend({
    el: "#base",
    tools :[],
    currentTool : null,
    _toolSelectorView : null,
    _map : null,
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
                var tool = this.getInstanceViewByType(listTools[i]);
                //var bringToFront = listTools[i] == localTools.selected ? true : false;
                this.addTool(tool,false);
            }
        }
        else{
            // if no information in local store load the country tool
            tool = new app.view.tools.CountryPlugin();
            this.addTool(tool,false);
        }

    },

    events: {
        "click #ctrl_tool" : "toggleTools",
        //"click #control_panel a" : "goToVisible",
        "click .header .close": "removeCurrentTool",
        "click #add_tool a": "showAddToolView",
        "click #ctrl_filter" : "showAddFilterSelectorView"
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
    
    getMap: function(){
        return this._map;
    },

    getTools: function(){
        return this.tools;
    },

    getToolByType: function(type){
        for (var i=0;i<this.tools.length;i++){
            if (this.tools[i].type == type){
                return this.tools[i];
            }
        }
        return null;
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
                this.currentTool.bringToFront();
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
                $(this).find("#tool_data").css('width', 'auto');
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

        // save the tool status in localstore
        this.saveToolStatus();
    },

    getInstanceViewByType: function(type){
        switch(type)
        {
            case "country":
                return new app.view.tools.CountryPlugin();
            case "ranking":
                return new app.view.tools.RankingPlugin();
            case "contributions":
                return new app.view.tools.ContributionsPlugin();
            case "quotes":
                return new app.view.tools.QuotesPlugin();     
            case "comparison":
                return new app.view.tools.ComparisonPlugin();            
        }

    },
    
    bringToolToFrontByType: function(type){
        var tool = this._searchToolByType(type);
        if (!tool){
            // The user has requested a tool but it's not loaded. Let's load it.
            tool = this.getInstanceViewByType(type);
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

    loadDefaultTool: function(){
        var localTools =  localStorage.getItem("tools");

        if (localTools){
            localTools = JSON.parse(localTools);
            
           
            var tool = this.getToolByType(localTools.selected);
            if (!tool){
                tool = this.getToolByType(localTools.tools[0]);
            }
            
            this.bringToolToFront(tool);        
            
        }
        else{
            // Not expected
        }
    },

    loadCountryTool: function(url){
        var tool = this._searchToolByType("country");

        if (!tool){
            // tool not already loaded
            tool = new app.view.tools.CountryPlugin();
            // This method transform the current url in a context 
            tool.URLToContext(url);
            // Add the tool
            this.addTool(tool,true);
        }
        else{
            // This method transform the current url in a context
            tool.URLToContext(url);
            // move tool to front
            this.bringToolToFront(tool);   
        }
    },

    loadRankingTool: function(url){
         var tool = this._searchToolByType("ranking");

        if (!tool){
            // tool not already loaded
            tool = new app.view.tools.RankingPlugin();
            // This method transform the current url in a context 
            tool.URLToContext(url);
            // Add the tool
            this.addTool(tool,true);
        }
        else{
            // This method transform the current url in a context
            tool.URLToContext(url);
            // move tool to front
            this.bringToolToFront(tool);   
        }
    },

    loadContributionsTool: function(url){
         var tool = this._searchToolByType("contributions");

        if (!tool){
            // tool not already loaded
            tool = new app.view.tools.ContributionsPlugin();
            // This method transform the current url in a context 
            tool.URLToContext(url);
            // Add the tool
            this.addTool(tool,true);
        }
        else{
            // This method transform the current url in a context
            tool.URLToContext(url);

            // move tool to front
            this.bringToolToFront(tool);   
        }
    },

    loadQuotesTool: function(url){
        var tool = this._searchToolByType("quotes");

        if (!tool){
            // tool not already loaded
            tool = new app.view.tools.QuotesPlugin();
            // This method transform the current url in a context 
            tool.URLToContext(url);
            // Add the tool
            this.addTool(tool,true);
        }
        else{
            // This method transform the current url in a context
            tool.URLToContext(url);

            // move tool to front
            this.bringToolToFront(tool);   
        }
    },

    loadComparisonTool: function(url){
         var tool = this._searchToolByType("comparison");

        if (!tool){
            // tool not already loaded
            tool = new app.view.tools.ComparisonPlugin();
            // This method transform the current url in a context 
            tool.URLToContext(url);
            // Add the tool
            this.addTool(tool,true);
        }
        else{
            // This method transform the current url in a context
            tool.URLToContext(url);

            // move tool to front
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
    },

    showAddToolView: function(e){
        e.preventDefault();
        if (this._toolSelectorView){
            this._toolSelectorView.close();
        }

        this._toolSelectorView = new app.view.ToolSelector(); 
        
    },

    showAddFilterSelectorView: function(e){
        e.preventDefault();
        if (this._filterSelectorView){
            this._filterSelectorView.close();
        }

        this._filterSelectorView = new app.view.FilterSelector(); 
    }
    
});