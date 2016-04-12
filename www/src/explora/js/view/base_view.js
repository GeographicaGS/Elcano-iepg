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

        this.$country_panel = this.$("#country_panel");
        this.originCountryPanel = this.$country_panel.css("right").replace("px","")*1;

        this.$ctrl_filter = this.$("#ctrl_filter");
        this.originCtrlFilter = this.$ctrl_filter.css("right").replace("px","")*1;

        this.$ctrl_map_zoom = this.$("#ctrl_map_zoom");

        // Load default tools
        var localTools =  localStorage.getItem("tools");

        if (localTools){
            localTools = JSON.parse(localTools);
            listTools = localTools.tools;
            if (listTools.length > 0 )
            {
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
            html += "<li " + sel + " tool='" + this.tools[i].type+ "' title='"+app.toolTypeToString(this.tools[i].type) +"'>" + 
                        "<a href='" + app.getJSURL("tool/" + this.tools[i].type) + "' jslink ></a>" + 
                    "</li>";
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

    closeAllTools: function(){
        for (var i=0;i<this.tools.length;i++){
            this.tools[i].close();
        }
        this.currentTool = null;
        this.tools = [];
        this.saveToolStatus();
        this.render();

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

            if (app.isTouchDevice()){
                ml = this.$tool.width() * -1;

                this.$tool.find("#tool_data").fadeOut(300);
                this.$tool.fadeOut(300);
                //this.$country_panel.fadeOut(300);
                //this.$ctrl_filter.fadeOut(300);
 
            }
            else{

                ml = this.$tool.width() * -1;
                this.$tool.find("#tool_data").width( $(window).width() -  this.originLeft - 20).height();
                this.$tool.animate({"left": ml});
                //this.$country_panel.animate({"right": (this.$country_panel.width() + this.originCountryPanel)*-1 });
                //this.$ctrl_filter.animate({"right": (this.$ctrl_filter.width() + this.originCtrlFilter)*-1 });
            }

            this.$control_panel.fadeOut(300);
            this.$ctrl_map_zoom.fadeIn(300);
           
        }

        else{
            $e.addClass("open");


            if (app.isTouchDevice()){
                this.$tool.find("#tool_data").fadeIn(300);
                this.$tool.fadeIn(300);
                //this.$country_panel.fadeIn(300);
                //this.$ctrl_filter.fadeIn(300);
 
            }
            else{
               
                var self = this;
                this.$tool.animate({"left": this.originLeft},function(){
                    $(this).find("#tool_data").css('width', 'auto');
                });

                //this.$country_panel.animate({"right":this.originCountryPanel});
                //this.$ctrl_filter.animate({"right":this.originCtrlFilter});
                
            }

            this.$control_panel.fadeIn(300);
            this.$ctrl_map_zoom.fadeOut(300);

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
        this.currentTool.forceFetchDataOnNextRender();
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