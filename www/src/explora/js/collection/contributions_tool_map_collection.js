app.collection.ContributionsToolMap = Backbone.Collection.extend({
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
        // Hack to avoid blank map
        var srvname = this._variable == "global" ? "" : "_relative_contribution";

        return app.config.API_URL + "/mapdata/" + this._family +  srvname + "/" 
                + this._variable + "/" 
                + this._date + "/" + this._mode +"?filter=" + app.getFilters().join(",");
    },

    parse: function(response){
        return _.filter(response.results,function(r){ return r.value !== null});
    }
});
