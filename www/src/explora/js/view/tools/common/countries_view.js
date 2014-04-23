app.view.tools.common.Countries = Backbone.View.extend({
    el: "#country_panel",
    _template : _.template( $('#country_bar_template').html() ),

    initialize: function(options){
        this.plugin = options.plugin;
    },
    
    render: function(){
        this.$el.show().html(this._template({
            ctx: this.plugin.getGlobalContext().data,
        }));
    },

    onClose: function(){
    
    },

    close: function(){
        this.stopListening();

        this.$el.html("").hide();
  
        if (this.onClose){
            this.onClose();
        }
    },
}); 