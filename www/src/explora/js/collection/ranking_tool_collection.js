app.collection.RankingTool = Backbone.Collection.extend({

    _year : null,
    _yearRef : null,
    _family : null,
    _variable : null,
    _entities : null,
    _block_analize : null,

    initialize: function(models,options){
        this._year = options.year;
        this._family = options.family;
        this._variable = options.variable;
        this._entities = options.entities;
        this._yearRef = options.yearRef;
        this._block_analize = options.block_analize ? 1 : 0;
    },

    url: function(){
        return this.urlRoot() + "/" + app.lang +  "/" + this._year  + "/" + this._yearRef + "/" 
                + this._family + "/" + this._variable + "/" + this._block_analize + "?entities=" + this._entities.join(",") 
                + "&filter=" + app.getFilters().join(",");
    },

    urlRoot: function() {
        return app.config.API_URL + "/ranking";
    },
    
    parse : function(response,options){
        return _.filter(response.results, function(item) {
             return item.currentRanking ;
        });
    }
});

