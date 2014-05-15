
app.collection.CountriesPlain = Backbone.Collection.extend({
 
    initialize: function(models, options) {

    },
    url : function() {
        return app.config.API_URL + "/home/countrylist/"+ app.lang ;
    },
    parse: function(response){
        return response.results;
    }
    
});
