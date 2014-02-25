app.view.docs.ListView = Backbone.View.extend({
    _template : _.template( $('#docs_list_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","docs");
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