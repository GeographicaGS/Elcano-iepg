app.view.Document = Backbone.View.extend({
    _template : _.template( $('#docs_detail_template').html() ),
    
    initialize: function(options) {
        app.events.trigger("menu","docs");
        this.model = new app.model.Document({"id": options.id});
        var self = this;
        this.model.fetch({
            success: function(){
                self.render();
            }
        });
        this.$el.html(app.loadingHTML());
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {
        this.$el.html(this._template({
            model: this.model.toJSON()
        }));
        return this;
    }
});