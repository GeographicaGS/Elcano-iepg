app.view.highlights.DetailView = Backbone.View.extend({
    _template : _.template( $('#highlights_detail_template').html() ),
    
    initialize: function(options) {
        app.events.trigger("menu","highlights");
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
        "click .btn-public" : "togglePublish",
        "click #delete" : "delete",
    },

    render: function() {
        
        this.$el.html(this._template({
            model : this.model.toJSON()
        }));
        return this;
    },

    togglePublish : function(e){
        var self = this;
        $.ajax({
            url: app.config.API_URL + "/highlight/togglepublish/" + this.model.get("id"),
            type: "PUT",
            success: function(){
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
            }
        });
        
    },

    delete: function(e){
        
        if (confirm("<lang>Are you sure?</lang>")){
            this.model.destroy({
                success: function(){
                    app.router.navigate("highlights",{trigger: true});
                }
            })
        };
    },  
});