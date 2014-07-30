app.collection.New = Backbone.Collection.extend({
    model: Backbone.Model,
    page : 0,
    search : "",

    initialize: function(models, options) {

    },

    url : function() {
        return app.config.API_URL + "/new" + "?page=" + this.page +"&search=" + this.search ;
    },

    parse: function(response){
        this.listSize = response.results.listSize;
        return response.results.data;
    }
});
