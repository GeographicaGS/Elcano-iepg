app.view.Methodology = Backbone.View.extend({
    _template : _.template( $('#methodology_template').html() ),
    
    initialize: function(options) {
        app.events.trigger("menu","about");

        this.collection = new app.collection.CountriesPlain();

        this.listenTo(this.collection,"reset",this.render);

        this.collection.fetch({"reset": true})
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {
        
        this.$el.html(this._template({
            collection : this.collection.toJSON()
        }));
        return this;
    }
});