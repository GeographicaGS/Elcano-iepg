app.view.UserView = Backbone.View.extend({
    _template : _.template( $('#user_template').html() ),
    
    initialize: function() {
        this.model.fetch();
        this.listenTo(this.model,"change",function(){
            this.render();
        });
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {
        if (this.model.get("id")) {
            this.$el.html(this._template(this.model.toJSON()));
        }
        
        return this;
    }
});