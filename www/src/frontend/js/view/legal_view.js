app.view.Legal = Backbone.View.extend({
    _template : _.template( $('#legal_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","");
        this.render();
    },
  
    render: function() {
        
        this.$el.html(this._template());
        return this;
    }
    
});