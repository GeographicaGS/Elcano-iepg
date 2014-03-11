var app = app || {};

app.collection.LatestNews = Backbone.Collection.extend({
    model: Backbone.Model,
    section : null,
    initialize: function(models, options) {

    },
    url : function() {
        var section = this.section ? "&section=" + this.section : "";
        return app.config.API_URL + "/home/newstuff" + "?lang=" + app.lang + section;
    },
    parse: function(response){
        return response.results;
    }

    
});
