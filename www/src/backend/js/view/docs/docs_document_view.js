app.view.docs.DocumentView = Backbone.View.extend({
    _template : _.template( $('#docs_document_template').html() ),
    
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