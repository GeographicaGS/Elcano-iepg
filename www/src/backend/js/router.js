var app = app || {};

app.router = Backbone.Router.extend({
    
    /* define the route and function maps for this router */
    routes: {
        "" : "home",
        "user" : "user",
        "news" : "news",
        "highlight" : "highlight",
        "logout" : "logout",
        // default page of doc section
        "docs": "listDocs",
        
        "docs/add" : "addDocument",
        "docs/edit/:id" : "editDocument",
        "docs/:id" : "viewDocument",
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
    
    highlight: function(){
        app.showView(new app.view.HighlightView());
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
    }
});