app.collection.Slider = Backbone.Collection.extend({
    model: Backbone.Model,

    
    initialize: function(models, options) {
        
    },
    url : function() {
       
        return app.config.API_URL + "/home/slider/" + app.lang ;
    },

    parse: function(response){
        // app.renameID(response.results,"link_"+app.lang,"link");
        // app.renameID(response.results,"text_"+app.lang,"text");
        // app.renameID(response.results,"title_"+app.lang,"title");
        // app.renameID(response.results,"credit_img_"+app.lang,"credit_img");

        return response.results;
    }

    
});
