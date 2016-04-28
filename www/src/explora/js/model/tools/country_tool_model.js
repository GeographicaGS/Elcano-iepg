app.model.tools.country = Backbone.Model.extend({

	
    url: function(){
        var s = this.urlRoot() + "/" + app.lang +  "/" + this.get("family") + "/" + this.get("id") + "?filter=" + app.getFilters().join(","); 
        return s;
    },

    urlRoot: function() {
        return app.config.API_URL + "/countrysheet";
    },
    
    parse : function(response,options){
        return response.results;
    }
});