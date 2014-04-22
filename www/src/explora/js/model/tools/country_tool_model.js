app.model.tools.country = Backbone.Model.extend({

    url: function(){
        return this.urlRoot() + "/" + this.get("id") + "/" + this.get("year") +  "/" + this.get("variable") + "/" +  app.lang;
    },

    urlRoot: function() {
        return app.config.API_URL + "/country";
    },
    
    parse : function(response,options){
        return response;
    }
});