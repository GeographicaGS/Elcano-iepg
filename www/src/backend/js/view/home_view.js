app.view.HomeView = Backbone.View.extend({
    _template : _.template( $('#home_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","home");
        this.render();
    },
    
    onClose: function(){
        // Remove events on close
    },
    
    render: function() {
        this.$el.html(this._template());
        return this;
    }
});