app.view.Document = Backbone.View.extend({
    _template : _.template( $('#docs_detail_template').html() ),
    _templateLatestDocs : _.template( $('#docs_detail_latestdocs_template').html() ),
    
    initialize: function(options) {
        app.events.trigger("menu","docs");
        this.model = new app.model.Document({"id": options.id});
        var self = this;
        this.model.fetch({
            success: function(){
                self._initialize();
                
            }
        });
        this.$el.html(app.loadingHTML());
    },

    _initialize: function(){
        this.latestDocs = new app.collection.LatestNews();
        this.latestDocs.section = "Documents";
        this.listenTo(this.latestDocs,"reset",function(){
            this.renderLatestDocs();
        });

        this.render();
        this.latestDocs.fetch({"reset": true});
    },
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {
        this.$el.html(this._template({
            model: this.model.toJSON()
        }));
        this.$latestDocs = this.$("#latestDocs");

        return this;
    },

    renderLatestDocs: function(){
       this.$latestDocs.html(this._templateLatestDocs({
            latest: this.latestDocs.toJSON()
       }));
       return this;
    }
});