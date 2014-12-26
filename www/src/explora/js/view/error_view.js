app.view.Error = Backbone.View.extend({
    _template : _.template( $('#error_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","");
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