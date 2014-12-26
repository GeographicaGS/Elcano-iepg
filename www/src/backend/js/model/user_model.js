app.model.User = Backbone.Model.extend({
    defaults:{
        id: null
    },  
    initialize: function(attrs, options) {
        
    },
    urlRoot: function() {
        return app.config.API_URL + "/user";
    }
  
});