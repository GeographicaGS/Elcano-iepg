var app = app || {};

app.collection.Label = Backbone.Collection.extend({
    model: app.model.Label,
    lang : null,
    initialize: function(models, lang) {
        this.lang = lang;
    },
    url : function() {
        return app.config.API_URL + "/label/" + this.lang;
    },
    parse: function(response){
        return response.results;
    }
});
