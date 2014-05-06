app.view.VariableSelector = Backbone.View.extend({
    _template : _.template( $('#variable_selector_template').html() ),

    initialize: function(options){

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
        "click [variable]" : "clickVariable"
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    
        $(window).off('resize');
    },

    render: function(){
        console.log("Render app.view.VariableSelector");

        this.$el.html(this._template({
            ctx: app.context.data,
        }));

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
        console.log($(e.target).attr("variable"));
    }


    

});