app.collection.CountryToolMap = Backbone.Collection.extend({
    _family: null,
    _variable : null,
    _date: null,

    initialize: function(models,options) {

        this._family = options && options.family ? options.family : null;
        this._variable = options && options.variable ? options.variable : null;
        this._date =options && options.family ? options.date : null;
    },
    
    url : function() {
        return app.config.API_URL + "/mapdata/" + this._family +  "/" + this._variable +  "/" 
                + this._date + "?filter=" + app.getFilters().join(",");
    },

    parse: function(response){
        return response.results;
    }
});
