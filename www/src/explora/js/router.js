app.router = Backbone.Router.extend({
    langRoutes : {
        // "_link home" : {"en":"home","es": "inicio" }
    },

    routes: {
        "": "root",
        "notfound" : "notfound",
        "error" : "error",
        "tool/:type" : "bringToolToFront",
        "country/:family/:countries/:country_sel/:year(/:filters)" : "country",
        "ranking/:family/:variable/:year/:year_ref/:countries/:country_sel(/:filters)" : "ranking",
        "*other"    : "notfound"
            /* This is a default route that also uses a *splat. Consider the
            default route a wildcard for URLs that are either not matched or where
            the user has incorrectly typed in a route path manually */
    },

    initialize: function(options) {
        // this.route(this.langRoutes["_link home"][app.lang], "home");
        // this.route(this.langRoutes["_link home"][app.lang]+"/", "home");
    },

    root: function(){

    },

    bringToolToFront: function(type,dos){
        app.baseView.bringToolToFrontByType(type);
    },

    notfound : function(){
        app.showViewInExtraPanel(new app.view.NotFound()); 
    },

    error: function(){
        app.showViewInExtraPanel(new app.view.Error());
        app.clearData();
    },

    country: function(family,countries,country_sel,year,filters){
        app.baseView.loadCountryTool({
            "family" : family,
            "countries" : countries,
            "country_sel": country_sel,
            "year" : year,
            "filters" : filters
        });
    },

    ranking: function(family,variable,year,year_ref,countries,country_sel,filters){
        app.baseView.loadRankingTool({
            "family" : family,
            "variable": variable,
            "year" : year,
            "year_ref": year_ref,
            "countries": countries,
            "country_sel" : country_sel,
            "filters": filters
        });
    }
});