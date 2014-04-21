app.view.tools.common.Countries = Backbone.View.extend({
    el: "#country_panel",
    _template : _.template( $('#country_bar_template').html() ),
    render: function(){
        this.$el.html(this._template());
    },
    onClose: function(){
        // Remove events on close
        this.stopListening(); 
    }   
}); 