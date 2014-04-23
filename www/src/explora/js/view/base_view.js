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

    },

    events: {
        "click #ctrl_tool" : "toggleTools",
        //"click #control_panel a" : "goToVisible",
        "click .header_tool .close": "removeCurrentTool"
    },

    render: function() {
        if (this.currentTool){
            this.currentTool.render();    
        }
            
        var html = "";
        for (var i=0;i<this.tools.length;i++){
            html += "<li><a href='" + app.getJSURL("tool/" + this.tools[i].type) + "' jslink>" + (i+1) + "</a></li>";
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
         // Just for security
        if (!tool) return;

        this.tools.push(tool);
        if (bringToFront){
            this.currentTool = tool;
        }
        this.render();
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

    // goToVisible: function(e){
    //     e.preventDefault();
    //     var $e = $(e.target),
    //         idx = $e.attr("idx-tool");

    //     this.bringToFront(this.tools[idx]);
    // },


    bringToFront: function(tool){
        // Just for security
        if (!tool) return;

        if (this.currentTool){
            this.currentTool.hideTool();
        }
        this.currentTool = tool;
        this.render();
    },

    bringToolToFront: function(type){
        var tool = this._searchToolByType(type);
        if (!tool){
            // The user has requested a tool but it's not loaded. Let's load it.
            switch(type)
            {
                case "country":
                    tool = new app.view.tools.CountryPlugin();
                    break;
                case "ranking":
                    tool = new app.view.tools.RankingPlugin();
                    break;
            }

            this.addTool(tool,true);
        }
        else{
            this.bringToFront(tool);    
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
            tool = new app.view.tools.CountryPlugin();

        // is the current country in the global context? 
        if (ctx.data.countries.indexOf(id_country)==-1){
            // This country is not in the global context. Let's add it
            ctx.data.countries.slice(0,0,id_country);
        }
        else{

        }

        // let's store the context.
        ctx.saveContext();
    }
});