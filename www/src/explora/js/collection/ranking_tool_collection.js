app.collection.RankingTool = Backbone.Collection.extend({

    _year : null,
    _family : null,
    _variable : null,

    initialize: function(models,options){
        this._year = options.year;
        this._family = options.family;
        this._variable = options.variable;
    },

    url: function(){
        return this.urlRoot() + "/" + app.lang +  "/" + this._year  + "/" + this._family
                + "/" + this._variable + "?filter=" + app.getFilters().join(",");
    },

    urlRoot: function() {
        return app.config.API_URL + "/ranking";
    },
    
    parse : function(response,options){
        return response.results;
    }
});

