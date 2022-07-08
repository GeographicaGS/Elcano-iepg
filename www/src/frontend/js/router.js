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
        "_link about meth": {"en": "methodologic","es" : "metodologia" },
        "_link download": {"en": "download","es" : "descarga" },
        "_link feed": {"en": "https://www.realinstitutoelcano.org/en/feed/", "es" : "https://www.realinstitutoelcano.org/feed/" }
    },

    /* define the route and function maps for this router */
    routes: {
            "" : "home",
            "notfound" : "notfound",
            "faq" : "faq",
            "error" : "error",
            "explora" : "explora",
            "legal" : "legal",
            "privacy" : "privacity",
            //"project/:id": "showProject",
            /* Sample usage: http://example.com/#about */
            "*other"    : "defaultRoute"
            /* This is a default route that also uses a *splat. Consider the
            default route a wildcard for URLs that are either not matched or where
            the user has incorrectly typed in a route path manually */

    },

    initialize: function(options) {
        // Bind 'route' event to send Google Analytics info
        Backbone.history.on("route", this.sendPageview);

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
        this.route(this.langRoutes["_link download"][app.lang], "download");
        this.route(this.langRoutes["_link feed"][app.lang], "feed");
    },

    home: function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global</lang>");
        app.showView(new app.view.Home());
    },

    about : function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Acerca de</lang>");
        app.showView(new app.view.About({
            "section" : "ppal"
        }));
    },

    aboutInfr : function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Estructura</lang>");
        app.showView(new app.view.Structure());
    },

    aboutMeth : function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Metodología</lang>");
        app.showView(new app.view.Methodology());
    },

    docs: function(filter,author){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Documentos</lang>");

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
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Documentos</lang>");
        app.showView(new app.view.Document({"id": id}));
    },

    defaultRoute: function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - No encontrado</lang>");
        app.showView(new app.view.NotFound());
    },

    notfound: function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - No encontrado</lang>");
        app.showView(new app.view.NotFound());
    },

    error: function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Error interno</lang>");
        app.showView(new app.view.Error());
    },

    contact: function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Contacto</lang>");
        app.showView(new app.view.Contact());
    },

    news: function(filter,author){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Noticias</lang>");
        if (filter=="null" || !filter){
            filter = null;
        }


        app.showView(new app.view.NewsList({
            "filter" : filter
        }));
    },

    faq: function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Preguntas frecuentes</lang>");
        app.showView(new app.view.FAQ());
    },

    explora: function(){
        window.location.href = app.config.EXPLORA_URL + "/" + app.lang;
        this.navigate("/");
    },

    privacity: function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Política de privacidad</lang>");
        app.showView(new app.view.Privacity());
    },

    legal: function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Aviso legal</lang>");
        app.showView(new app.view.Legal());
    },

    download: function(){
        $(document).prop("title", "<lang>Índice Elcano de Presencia Global - Datos</lang>");
    	app.showView(new app.view.Download());
    },

    sendPageview: function(){
        var url;
        url = Backbone.history.root + Backbone.history.getFragment()
        ga('send', 'pageview', url);
    }


});
