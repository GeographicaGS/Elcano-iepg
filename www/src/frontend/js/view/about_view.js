app.view.About = Backbone.View.extend({
    _template : _.template( $('#about_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","about");
        this.render();
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {
        
        this.$el.html(this._template());
        return this;
    }
});