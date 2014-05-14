app.view.Methodology = Backbone.View.extend({
    _template : _.template( $('#methodology_template').html() ),
    
    initialize: function(options) {
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