app.model.Highlight = Backbone.Model.extend({
    validation: function (){
        return {
            title_es: {
                maxLength : 25,

                required: true
            },
            title_en : {
                maxLength : 25,
                required: true
            },

            text_es : {
                maxLength : 45,
                required: true
            },
            text_en : {
                maxLength : 45,
                required: true
            },
            link_es: {
                maxLength : 500,
                required: false,
                pattern : "url"
            },
            link_en : {
                maxLength : 500,
                required: false,
                pattern : "url"
            },

            credit_img_es: {
                maxLength : 50,
                required: false,
                pattern : "url"
            },
            credit_img_en : {
                maxLength : 50,
                required: false,
                pattern : "url"
            },

            image_hash_es: function(value) {
                if(!value || !value.length) {
                    return "<lang>Field required</lang>";
                }
            },

            image_hash_en: function(value) {
                if(!value || !value.length) {
                    return "<lang>Field required</lang>";
                }
            }



        }      
    },
    urlRoot: function() {
        return app.config.API_URL + "/highlight";
    },
    parse : function(response,options){

        return response;
    }
});