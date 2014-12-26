app.collection.GlobalIndex = Backbone.Collection.extend({
    _family : null,
    _countries : null,
    
    initialize: function(models,options) {
        this._family = options && options.family ? options.family : null;
        this._countries = options && options.countries ? options.countries : null;
   
    },
    
    url : function() {
        return app.config.API_URL + "/globalindex/" + this._family + "/global/" + this._countries.join(",") + "/" + app.lang;
    },

    parse: function(response){
        return response.results;
    }
});
