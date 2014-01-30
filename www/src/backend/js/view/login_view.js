app.view.LoginView = Backbone.View.extend({
    _template : _.template( $('#login_template').html() ),  
    initialize: function() {
        
    },
    
    onClose: function(){
        // Remove events on closeº
    },
    
    // The DOM events specific to an item.
    events: {
      
    },
 
    render: function() {
        this.$el.html(this._template());
        return this;
    }
});