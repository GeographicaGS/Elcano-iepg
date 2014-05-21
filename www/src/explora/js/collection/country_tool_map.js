app.collection.CountryToolMap = Backbone.Collection.extend({
    _family: null,
    _variable : null,
    _date: null,

    initialize: function(models,options) {
        this._family = options.family;
        this._variable = options.variable;
        this._date = options.date;
    },
    
    url : function() {
        return app.config.API_URL + "/mapdata/" + this._family +  "/" + this._variable +  "/" 
                + this._date + "?filter=" + app.getFilters().join(",");
    },

    parse: function(response){
        return response.results;
    }
});
