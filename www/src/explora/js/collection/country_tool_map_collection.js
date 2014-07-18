app.collection.CountryToolMap = Backbone.Collection.extend({
    _family: null,
    _variable : null,
    _date: null,

    initialize: function(models,options) {

        this._family = options && options.family ? options.family : null;
        this._variable = options && options.variable ? options.variable : null;
        this._date = options && options.family ? options.date : null;
        this._mode = options && options.mode ? options.mode : 0;
    },
    
    url : function() {
        return app.config.API_URL + "/mapdata/" + this._family +  "/" + this._variable +  "/" 
                + this._date + "/" + this._mode +"?filter=" + app.getFilters().join(",");
    },

    parse: function(response){
        return response.results;
    }
});
