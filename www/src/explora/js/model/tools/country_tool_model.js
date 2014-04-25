app.model.tools.country = Backbone.Model.extend({

    url: function(){
        return this.urlRoot() + "/" + app.lang +  "/" + this.get("id") + "?filter=ES,US";
    },

    urlRoot: function() {
        return app.config.API_URL + "/countrysheet";
    },
    
    parse : function(response,options){
        return response.results;
    }
});