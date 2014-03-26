app.collection.News = Backbone.Collection.extend({
    model: Backbone.Model,
    search: null,
    filter : null,
    page: 0,

    initialize: function(models, options) {

    },

    url : function() {
        var search = this.search ? "&search=" + this.search : "";
        var filter = this.filter ? "&filterbylabel=" + this.filter.join(",") : "";
        return app.config.API_URL + "/new" + "?lang=" + app.lang + "&page=" + this.page + search + filter;
    },

    parse: function(response){
        this.listSize = response.results.listSize;
        return response.results.data;
    }
    
});
