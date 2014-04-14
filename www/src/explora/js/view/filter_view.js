app.view.Filter = Backbone.View.extend({
    _template : _.template( $('#filter_template').html() ),

    initialize: function() {
        this.collection = new app.collection.Filter();

        this.listenTo(this.collection, "reset",function(){
            this.render();
        });

        this.collection.fetch({reset: true});
    }, 
    
    render: function(){
        this.$el.html(this._template({
            filters: this.collection.toJSON(),
            selection: app.filters
        }));

    },

    save: function(){
        // TODO modify selected filters in app.filters

    },
    
    onClose: function(){
       // Remove events on close
       this.stopListening();
    }
});






