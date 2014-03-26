app.collection.Document = Backbone.Collection.extend({
    model: Backbone.Model,
    page : 0,
    search : "",
    orderbyfield : "title",
    orderbyorder : "asc",
    
    initialize: function(models, options) {

    },
    url : function() {
        return app.config.API_URL + "/document" + "?page=" + this.page +"&search=" + this.search 
                + "&orderbyfield=" + this.orderbyfield + "&orderbyorder=" + this.orderbyorder;
    },
    parse: function(response){
        this.listSize = response.results.listSize;
        return response.results.data;
    }
});
