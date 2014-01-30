var app = app || {};

app.router = Backbone.Router.extend({
    
    /* define the route and function maps for this router */
    routes: {
        "" : "showProjects",
        "projects" : "showProjects",
        "project/:id": "showProject",
        /* Sample usage: http://example.com/#about */
        "*other"    : "defaultRoute"
        /* This is a default route that also uses a *splat. Consider the
        default route a wildcard for URLs that are either not matched or where
        the user has incorrectly typed in a route path manually */
       
    },

    showProjects: function(){
       app.showProjects();
    },
    showProject: function(id){
        app.showProject(id);
    },
    defaultRoute: function(other){
        console.log('Invalid. You attempted to reach:' + other);
    }
});