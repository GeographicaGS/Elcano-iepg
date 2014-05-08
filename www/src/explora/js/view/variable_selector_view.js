app.view.VariableSelector = Backbone.View.extend({
    _template : _.template( $('#variable_selector_template').html() ),
    _variable : null,
    initialize: function(options){

        this._variable = app.context.data.variables[0];


        var self = this;

        var opts = app.fancyboxOpts();
        opts["afterLoad"] = function () {
            self.render();
        }

        $.fancybox(this.$el, opts);

        $(window).on('resize', function(){
            self.render();
        });



        //this.render();
    },

    events : {
        "click #save": "save",
        "click #cancel": "cancel",
        "click [variable]" : "clickVariable",
        "mouseenter [variable]" : "mouseenterVariable",
        "mouseleave [variable]" : "mouseleaveVariable",
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    
        $(window).off('resize');
    },


    _renderVariableInfo: function(v){
        this.$(".desc").hide();
        this.$("h4").html(app.variableToString(v));
        this.$("#" + v + "_text").show();
    },

    render: function(){
        console.log("Render app.view.VariableSelector");

        this.$el.html(this._template({
            ctx: app.context.data,
        }));

        this._renderVariableInfo(this._variable);
        this.$(".img[variable='" + this._variable +"']").attr("selected",true);
        
        return this;
    },

    cancel: function(){
        $.fancybox.close();
        app.events.trigger("closepopup",this);
    },

    save: function(){
        $.fancybox.close();

        app.events.trigger("closepopup",this);
  
    },

    clickVariable: function(e){
        e.preventDefault();
        var $e = $(e.target),
            variable = $e.attr("variable");

        this._variable = variable;

        this._renderVariableInfo(variable);

        this.$(".img").attr("selected",false);

        $e.attr("selected",true);

    },

    mouseenterVariable: function(e){
        var $e = $(e.target),
            variable = $e.attr("variable");

        this._renderVariableInfo(variable);
    },

    mouseleaveVariable: function(e){
        this._renderVariableInfo(this._variable);
    }

});