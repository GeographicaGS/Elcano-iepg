app.collection.HighlightUnpublish = Backbone.Collection.extend({
    model: Backbone.Model,
    page : 0,
    search : "",
    
    initialize: function(models, options) {

    },

    url : function() {
        return app.config.API_URL + "/highlight/unpublishedcatalog" + "?page=" + this.page +"&search=" + this.search;
    },

    parse: function(response){
        return response.results;
    }
});
