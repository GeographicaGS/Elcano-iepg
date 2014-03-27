
app.collection.HighlightPublish = Backbone.Collection.extend({
    model: Backbone.Model,
    initialize: function(models, options) {

    },
    url : function() {
        return app.config.API_URL + "/highlight/publishedcatalog"
              
    },
    parse: function(response){
        return response.results;
    }
});
