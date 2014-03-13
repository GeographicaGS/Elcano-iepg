var app = app || {};

app.collection.Document = Backbone.Collection.extend({
    model: Backbone.Model,
    offset : 0,
    search : "",
    orderbyfield : "title",
    orderbyorder : "asc",
    
    initialize: function(models, options) {

    },
    url : function() {
        return app.config.API_URL + "/document" + "?offset=" + this.offset +"&search=" + this.search 
                + "&orderbyfield=" + this.orderbyfield + "&orderbyorder=" + this.orderbyorder;
    },
    parse: function(response){
        this.listSize = response.results.listSize;
        return response.results.documentList;
    }
});
