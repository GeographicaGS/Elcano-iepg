app.view.Home = Backbone.View.extend({
    _template : _.template( $('#home_template').html() ),
    
    initialize: function() {  
        app.events.trigger("home");
        this.render();
        var self = this;
    },
    render: function() {
        this.$el.html(this._template());
        return this;
    }
});