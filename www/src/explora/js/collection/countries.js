app.collection.Countries = Backbone.Collection.extend({
    initialize: function(models) {

    },
    
    url : function() {
        return app.config.API_URL + "/countries_toremove/" + app.lang;
    },

    parse: function(response){
        return response.results;
    }
});
