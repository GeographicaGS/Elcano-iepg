app.view.Privacity = Backbone.View.extend({
    _template : _.template( $('#privacity_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","");
        this.render();
    },
  
    render: function() {
        
        this.$el.html(this._template());
        return this;
    }
    
});