
app.collection.Label = Backbone.Collection.extend({
    model: Backbone.Model,
    url : function() {
        return app.config.API_URL + "/document/label/"+ app.lang;
    },
    parse: function(response){
        app.renameID(response.results,"id_label_"+app.lang,"id");
        return response.results;
    }
    
});
