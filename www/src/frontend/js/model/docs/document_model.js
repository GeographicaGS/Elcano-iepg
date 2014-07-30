app.model.Document = Backbone.Model.extend({

    url: function(){
        return this.urlRoot() + "/" + this.get("id") + "/" + app.lang;
    },

    urlRoot: function() {
        return app.config.API_URL + "/document";
    },
    
    parse : function(response,options){
        return response;
    }
});