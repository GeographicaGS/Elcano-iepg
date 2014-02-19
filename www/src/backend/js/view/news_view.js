app.view.NewsView = Backbone.View.extend({
    _template : _.template( $('#news_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","news");
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