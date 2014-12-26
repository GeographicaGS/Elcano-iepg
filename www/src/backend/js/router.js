var app = app || {};

app.router = Backbone.Router.extend({
    
    /* define the route and function maps for this router */
    routes: {
        "" : "highlightList",
        "user" : "user",
        
        "logout" : "logout",
        
        // Documents section
        "docs": "listDocs",
        "docs/add" : "addDocument",
        "docs/edit/:id" : "editDocument",
        "docs/:id" : "viewDocument",

        // Highlight section
        "highlights" : "highlightList",
        "highlights/add" : "addHighlight",
        "highlights/edit/:id" : "editHighlight",
        "highlights/:id" : "highlightDetail",

        // news" : "news",
        "news" : "newsList",
        "news/add" : "addNews",
        "news/edit/:id" : "editNews",
        "news/:id" : "newsDetail",

        "calc" : "calc",

        //"project/:id": "showProject",
        /* Sample usage: http://example.com/#about */
        "*other"    : "defaultRoute"
        /* This is a default route that also uses a *splat. Consider the
        default route a wildcard for URLs that are either not matched or where
        the user has incorrectly typed in a route path manually */
       
    },
    
    user: function(){
        app.showView(new app.view.UserView({
            model: app.getUser()
        }));
    },
    
    news: function(){
        app.showView(new app.view.NewsView());
    },
    
    logout : function(){
        app.logout();
    },
    
    listDocs: function(){
        app.showView(new app.view.docs.ListView());
    },
    
    viewDocument: function(id){
        app.showView(new app.view.docs.DocumentView({
            model : new app.model.Document({"id": id})
        }));
    },
    
    addDocument: function(){
        app.showView(new app.view.docs.FormView());
    },
    
    editDocument: function(id){
        app.showView(new app.view.docs.FormView({"id":id}));
    },
    
    defaultRoute: function(other){
        console.log('Invalid. You attempted to reach:' + other);
    },

    highlightList: function(){
        app.showView(new app.view.highlights.ListView());
    },

    highlightDetail: function(id){
        app.showView(new app.view.highlights.DetailView({
            model : new app.model.Highlight({"id": id})
        }));
    },

    addHighlight: function(){
        app.showView(new app.view.highlights.FormView());
    },
    
    editHighlight: function(id){
        app.showView(new app.view.highlights.FormView({
            "id":id
        }));
    },

    /*
           "news" : "newsList",
        "news/add" : "addNews",
        "news/edit/:id" : "editNews",
        "news/:id" : "newsDetail",

    */
    newsList: function(){
        app.showView(new app.view.news.ListView());
    },

    addNews: function(){
        app.showView(new app.view.news.FormView());
    },

    editNews: function(id){
        app.showView(new app.view.news.FormView({
            "id" : id 
        }));
    },

    newsDetail: function(id){
        app.showView(new app.view.news.DetailView({
            model : new app.model.New({"id": id})
        }));
    },

    calc: function(){
         app.showView(new app.view.calc.CalcFormView());
    }
});