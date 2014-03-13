app.view.docs.DocumentView = Backbone.View.extend({
    _template : _.template( $('#docs_document_template').html() ),

    initialize: function() {
        app.events.trigger("menu","docs");
        // Fetch model from de server
        var self = this;
        this.model.fetch({
            success: function() {
                self.render();
              }
        });
        
    },
    
    onClose: function(){
        // Remove events on close
    },
    
    events : {
        "click #publish" : "publish",
        "click #delete" : "delete",
    },

    publish : function(e){
        console.log("Publish");
    },

    delete: function(e){
        
        if (confirm("<lang>Are you sure?</lang>")){
            this.model.destroy({
                success: function(){
                    app.router.navigate("docs",{trigger: true});
                }
            })
        };
    },  
    render: function() {
        this.$el.html(this._template({
            model: this.model.toJSON()
        }));
        return this;
    }
});