app.view.tools.common.Countries = Backbone.View.extend({
    el: "#country_panel",
    _template : _.template( $('#country_bar_template').html() ),

    render: function(){
        this.$el.show().html(this._template());
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