app.view.docs.DocumentView = Backbone.View.extend({
    _template : _.template( $('#docs_document_template').html() ),
    _modelFetched : false,
    initialize: function() {
        app.events.trigger("menu","docs");
        // Fetch model from de server
        var self = this;
        this.model.fetch({
            success: function() {
                self._modelFetched = true;
                self.render();
              }
        });
        
    },
    
    onClose: function(){
        // Remove events on close
    },
    
    events : {
        "click .btn-public" : "togglePublish",
        "click #delete" : "delete",
    },

    togglePublish : function(e){
        var self = this;
        $.getJSON(app.config.API_URL + "/document/" + this.model.get("id") + "/toggle_publish",function(){
            if (self.model.get("published")){
                self.model.set("published",false);
                self.$(".publish_ctrl").show();
                self.$(".unpublish_ctrl").hide();
            }
            else{
                self.model.set("published",true);
                self.$(".publish_ctrl").hide();
                self.$(".unpublish_ctrl").show();
            }
        });
        
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
        if (!this._modelFetched){
            return this;
        }

        
        this.$el.html(this._template({
            model: this.model.toJSON()
        }));
        return this;
    }
});