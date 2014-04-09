var app = app || {};

app.router = Backbone.Router.extend({
    
    langRoutes : {
        
    },

    /* define the route and function maps for this router */
    routes: {
        "" : "home"   
    },
    initialize: function(options) { 
        this.route(this.langRoutes["_link home"][app.lang], "home");
    },
    home: function(){
        app.showView(new app.view.Home());
    },
    
});