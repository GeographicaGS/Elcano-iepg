app.collection.Countries = Backbone.Collection.extend({
    initialize: function(models) {

    },

    url : function() {
        return app.config.API_URL + "/countryfilter/" + app.lang;
    },

    parse: function(response){
        return response.results;
    },

    applyGlobalFilter: function(){
        var filters = app.getFilters();
        if (!filters.length){
            return this;
        }

        var filtered = this.filter(function(c) {
            return filters.indexOf(c.get("id"))== -1;
        });

        return new app.collection.Countries(filtered);
    }

});
