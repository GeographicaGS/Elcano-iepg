var app = app || {};
app.router = Backbone.Router.extend({
    langRoutes : {
        "_link home" : {"en":"home","es": "inicio" }
    },
    routes: {
         "": "home"
    },
    initialize: function(options) {
        this.route(this.langRoutes["_link home"][app.lang], "home");
        this.route(this.langRoutes["_link home"][app.lang]+"/", "home");
    },
    home : function(){
        app.showView(new app.view.Home());
    }
});