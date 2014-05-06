app.model.New = Backbone.Model.extend({
    _titleRequiredGroup : [ "title_es","title_en"],
    _textRequiredGroup : [ "text_es","text_en"],
    validation: function (){
        return {
            title_es: {
                maxLength : 150,
                requiredGroup: this._titleRequiredGroup
            },
            title_en : {
                maxLength : 150,
                requiredGroup: this._titleRequiredGroup
            },

            text_es: {
                requiredGroup: this._textRequiredGroup
            },
            text_en : {
                requiredGroup: this._textRequiredGroup
            },
           
            url_es: {
                maxLength : 500,
                required: false,
                pattern : "url"
            },
            url_en : {
                maxLength : 500,
                required: false,
                pattern : "url"
            }
        }
    },
    urlRoot: function() {
        return app.config.API_URL + "/new";
    },
    parse : function(response,options){
        response.labels_es  =  new Backbone.Collection(response.labels_es);
        response.labels_en  =  new Backbone.Collection(response.labels_en);
        return response;
    }
});