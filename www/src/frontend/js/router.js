var app = app || {};

app.router = Backbone.Router.extend({
    
    langRoutes : {
        "_link home" : {"en":"home","es": "inicio" },
        "_link about": {"en": "about","es" : "acerca_de" },
        "_link docs": {"en": "documents","es" : "documentos" },

    },

    /* define the route and function maps for this router */
    routes: {
            "" : "home",

            //"project/:id": "showProject",
            /* Sample usage: http://example.com/#about */
            "*other"    : "defaultRoute"
            /* This is a default route that also uses a *splat. Consider the
            default route a wildcard for URLs that are either not matched or where
            the user has incorrectly typed in a route path manually */
        
    },

    initialize: function(options) {
        this.route(this.langRoutes["_link home"][app.lang], "home");
        this.route(this.langRoutes["_link about"][app.lang], "about");
        this.route(this.langRoutes["_link docs"][app.lang], "docs");
        this.route(this.langRoutes["_link docs"][app.lang] + "/:id", "doc");
    
        //return obj
    },
    
    home: function(){
        app.showView(new app.view.Home());
    },
    about : function(){
        app.showView(new app.view.About());
    },

    docs: function(){
        app.showView(new app.view.DocsList());   
    },

    doc: function(id){
        app.showView(new app.view.Document({"id": id}));
    }
    
});