app.router = Backbone.Router.extend({
    langRoutes : {
        // "_link home" : {"en":"home","es": "inicio" }
    },

    routes: {
        "": "root",
        "notfound" : "notfound",
        "error" : "error",
        "tool/:type" : "bringToolToFront",
        "country/:family/:variable/:countries/:country_sel/:year(/:filters)" : "country",
        "ranking/:family/:variable/:year/:year_ref/:countries/:country_sel/:block_analize(/:filters)" : "ranking",
        "contributions/:family/:variable/:year/:countries/:countries_sel(/:filters)" : "contributions",
        "quotes/:family/:variable/:countries/:countries_sel/:year_ref(/:filters)" : "quotes",
        "comparison/:variable/:year/:countries/:country_sel(/:filters)" : "comparison",
        "toolSelector" : "toolSelector",
        
        "home/*url": "external",

        "*other"    : "notfound"
            /* This is a default route that also uses a *splat. Consider the
            default route a wildcard for URLs that are either not matched or where
            the user has incorrectly typed in a route path manually */
    },

    initialize: function(options) {
        // this.route(this.langRoutes["_link home"][app.lang], "home");
        // this.route(this.langRoutes["_link home"][app.lang]+"/", "home");

        // Bind 'route' event to send Google Analytics info
        Backbone.history.on("route", this.sendPageview);
    },

    root: function(){
        app.baseView.loadDefaultTool();
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

    country: function(family,variable,countries,country_sel,year,filters){
        app.baseView.loadCountryTool({
            "family" : family,
            "variable" : variable,
            "countries" : countries,
            "country_sel": country_sel,
            "year" : year,
            "filters" : filters
        });
    },

    ranking: function(family,variable,year,year_ref,countries,country_sel,block_analize,filters){
        app.baseView.loadRankingTool({
            "family" : family,
            "variable": variable,
            "year" : year,
            "year_ref": year_ref,
            "countries": countries,
            "country_sel" : country_sel,
            "filters": filters,
            "block_analize" : block_analize
        });
    },

    contributions : function(family,variable,year,countries,countries_sel,filters){
        app.baseView.loadContributionsTool({
            "family" : family,
            "variable" : variable,
            "year" : year,
            "countries": countries,
            "countries_sel" : countries_sel,
            "filters": filters
        });
    },

    quotes: function(family,variable,countries,countries_sel,year_ref,filters){
        app.baseView.loadQuotesTool({
            "family" : family,
            "variable" : variable,
            "countries": countries,
            "countries_sel" : countries_sel,
            "year_ref": year_ref,
            "filters": filters
        });
    },

    comparison : function(variable,year,countries,countries_sel,filters){
        app.baseView.loadComparisonTool({
            "variable" : variable,
            "year" : year,
            "countries" : countries,
            "countries_sel" : countries_sel,
            "filters": filters
        });
    },

    external: function(url){
        window.location.href = app.config.FRONT_URL + "/" + url;
        this.navigate("/");
    },

    sendPageview: function(){
        var url;
        url = Backbone.history.root + Backbone.history.getFragment()
        ga('send', 'pageview', url);
    },

    toolSelector: function(){
        $("#add_tool a").trigger("click")
    }
});