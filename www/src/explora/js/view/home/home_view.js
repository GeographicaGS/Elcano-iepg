app.view.Home = Backbone.View.extend({
    _template : _.template($('#home_template').html()),
    initialize: function() {  
        this.on("rendered",this.onRender);
        this.render();
    },
    render: function() {
        this.$el.html(this._template());
        return app.events.trigger("rendered");
    },
    onRender: function() {
        this.$countrypanel.html(new app.view.BarView());
    }
});