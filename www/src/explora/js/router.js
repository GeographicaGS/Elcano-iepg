app.router = Backbone.Router.extend({
    langRoutes : {
        // "_link home" : {"en":"home","es": "inicio" }
    },

    routes: {
        "": "base",
        "notfound" : "notfound",
        "error" : "error",
        "tool/:type" : "bringToolToFront",
        "country/:id_country/:id_variable/:year" : "country",
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
        // Do nothing
        app.baseView.addTool(new app.view.tools.CountryPlugin(),true);
        app.baseView.addTool(new app.view.tools.RankingPlugin(),false);
    },

    bringToolToFront: function(type){
        app.baseView.bringToolToFrontByType(type);
    },

    notfound : function(){
        app.showViewInExtraPanel(new app.view.NotFound()); 
    },

    error: function(){
        app.showViewInExtraPanel(new app.view.Error());
    },

    country: function(id_country,id_variable,year){
        app.baseView.loadCountryTool(id_country,id_variable,year);
    }

});