app.collection.Quotes = Backbone.Collection.extend({
    _family: null,
    _variable : null,
    _countries : null,

    initialize: function(models,options) {
    	this._family = options && options.family ? options.family : null;
        this._variable = options && options.variable ? options.variable : null;	
        this._countries = options && options.countries ? options.countries : null;	
    },
    
    url : function() {
        return app.config.API_URL + "/quotes/" + this._family +  "/" + this._variable 
        		+ "/" + this._countries.join(",") + "/" + app.lang +  "?filter=" + app.getFilters().join(",");
    },

    parse: function(response){
        return response.results;
    }
});
