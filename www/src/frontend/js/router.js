var app = app || {};

app.router = Backbone.Router.extend({
    
    langRoutes : {
        "_link home" : {"en":"home","es": "inicio" },
        "_link about": {"en": "about","es" : "acerca_de" },
        "_link docs": {"en": "documents","es" : "documentos" },
        "_link doc": {"en": "document","es" : "documento" },
        "_link contact": {"en": "contact","es" : "contacto" },
        "_link news": {"en": "news","es" : "noticias" },
        "_link about infr": {"en": "structure","es" : "estructura" },
        "_link about meth": {"en": "methodologic","es" : "metodologia" }
    },

    /* define the route and function maps for this router */
    routes: {
            "" : "home",
            "notfound" : "notfound",
            "faq" : "faq",
            "error" : "error",
            "explora" : "explora",
            "legal" : "legal",
            "privacity" : "privacity",
            //"project/:id": "showProject",
            /* Sample usage: http://example.com/#about */
            "*other"    : "defaultRoute"
            /* This is a default route that also uses a *splat. Consider the
            default route a wildcard for URLs that are either not matched or where
            the user has incorrectly typed in a route path manually */
        
    },

    initialize: function(options) {
        this.route(this.langRoutes["_link home"][app.lang], "home");
        this.route(this.langRoutes["_link home"][app.lang]+"/", "home");
        this.route(this.langRoutes["_link about"][app.lang], "about");
        this.route(this.langRoutes["_link docs"][app.lang]+"(/:filter)(/:author)", "docs");
        this.route(this.langRoutes["_link docs"][app.lang]+"/", "docs");
        this.route(this.langRoutes["_link doc"][app.lang]+"/:id", "doc");
        this.route(this.langRoutes["_link contact"][app.lang], "contact");
        this.route(this.langRoutes["_link news"][app.lang]+"(/:filter)", "news");
        this.route(this.langRoutes["_link news"][app.lang]+"/", "news");
        this.route(this.langRoutes["_link about infr"][app.lang], "aboutInfr");
        this.route(this.langRoutes["_link about meth"][app.lang], "aboutMeth");
    },
    
    home: function(){
        app.showView(new app.view.Home());
    },

    about : function(){
        app.showView(new app.view.About({
            "section" : "ppal"
        }));
    },

    aboutInfr : function(){
        app.showView(new app.view.About({
            "section" : "infr"
        }));
    },

    aboutMeth : function(){
        app.showView(new app.view.About({
            "section" : "meth"
        }));
    },

    docs: function(filter,author){
        if (filter=="null" || !filter){
            filter = null;
        }

        if (!author){
            author = null;
        }

        app.showView(new app.view.DocsList({
            "filter" : filter,
            "author": author,
        }));
    },

    doc: function(id){
        app.showView(new app.view.Document({"id": id}));
    },

    defaultRoute: function(){
        app.showView(new app.view.NotFound());
    },

    notfound: function(){
        app.showView(new app.view.NotFound());
    },

    error: function(){
        app.showView(new app.view.Error());
    },

    contact: function(){
        app.showView(new app.view.Contact());
    },

    news: function(filter,author){
        if (filter=="null" || !filter){
            filter = null;
        }

       
        app.showView(new app.view.NewsList({
            "filter" : filter
        }));
    },

    faq: function(){
        app.showView(new app.view.FAQ());
    },

    explora: function(){
        window.open(
          app.config.EXPLORA_URL,
          "_blank" // <- This is what makes it open in a new window.
        );
        this.navigate("/");
    },

    privacity: function(){
        app.showView(new app.view.Privacity());
    },

    legal: function(){
        app.showView(new app.view.Legal());
    }

    
});