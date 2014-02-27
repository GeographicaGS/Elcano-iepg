app.view.docs.ListView = Backbone.View.extend({
    _template : _.template( $('#docs_list_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","docs");
        this.collection = new app.collection.Document();
        this.collection.fetch({"reset" : true});
        this.listenTo(this.collection,"reset", function(){
            this.render();    
        });
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    render: function() {
        this.$el.html(this._template({
            collection : this.collection.toJSON(),
            listSize : this.collection.listSize
        }));
        return this;
    }

});