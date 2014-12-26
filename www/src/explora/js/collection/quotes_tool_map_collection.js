app.collection.QuotesToolMap = Backbone.Collection.extend({
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
        return app.config.API_URL + "/mapdata/" + this._family +  "_quota/" + this._variable +  (this._variable == "global" ? "_global" : "") + "/" 
                + this._date + "/" + this._mode +"?filter=" + app.getFilters().join(",");
    },

    parse: function(response){
        return _.filter(response.results,function(r){ return r.value !== null});
    }
});
