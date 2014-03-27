app.model.Countries = Backbone.Model.extend({
    model: Backbone.Model,
    initialize: function( options) {
        this.year = options.year;
    },
    url : function() {
        return app.config.API_URL + "/home/countries" + "?lang=" + app.lang + "&year=" + this.year;
    }    
});
