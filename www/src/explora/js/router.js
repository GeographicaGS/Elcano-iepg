app.router = Backbone.Router.extend({
    langRoutes : {
        // "_link home" : {"en":"home","es": "inicio" }
    },
    routes: {
        "": "base",
        "notfound" : "notfound",
        "error" : "error",
        "*other"    : "notfound"
            /* This is a default route that also uses a *splat. Consider the
            default route a wildcard for URLs that are either not matched or where
            the user has incorrectly typed in a route path manually */
    },
    initialize: function(options) {
        // this.route(this.langRoutes["_link home"][app.lang], "home");
        // this.route(this.langRoutes["_link home"][app.lang]+"/", "home");
    },
    base : function(){
        app.baseView = new app.view.Base();
    },
    notfound : function(){
        app.showViewInExtraPanel(new app.view.NotFound()); 
    },
    error: function(){
        app.showViewInExtraPanel(new app.view.Error());
    }
});