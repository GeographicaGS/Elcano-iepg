var app = app || {};

app.router = Backbone.Router.extend({
    
    /* define the route and function maps for this router */
    routes: {
        
        "user" : "user",
        "news" : "news",
        "home" : "home",
        "logout" : "logout",       
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
    
    home: function(){
        app.showView(new app.view.HomeView());
    },
    
    logout : function(){
        app.logout();
    },
    
    defaultRoute: function(other){
        console.log('Invalid. You attempted to reach:' + other);
    }
});