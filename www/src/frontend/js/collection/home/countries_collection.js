app.collection.Countries = Backbone.Collection.extend({
    _year: null,
    section : null,
    initialize: function(models, options) {
    	this._year = options.year;
    },
    url : function() {
        return app.config.API_URL + "/home/countries" + "?lang=" + app.lang + "&year=" + this._year;
    },
    parse: function(response){
        return response.results;
    }

    
});
