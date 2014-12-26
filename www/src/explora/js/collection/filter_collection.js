app.collection.Filter = Backbone.Collection.extend({
    lang : null,
    initialize: function(models, lang) {
        this.lang = lang;
    },
    url : function() {
        return app.config.API_URL + "/filter/" + this.lang;
    },
    parse: function(response){
        return response.results;
    }
});
