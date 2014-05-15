app.model.Document = Backbone.Model.extend({
	_titleRequiredGroup : [ "title_es","title_en"],
	_themeRequiredGroup : [ "theme_es","theme_en"],
	_descriptionRequiredGroup : [ "description_es","description_en"],
	validation: function (){
		return {
			title_es: {
				maxLength : 150,
				required: true,
				//requiredGroup: this._titleRequiredGroup
			},
			title_en : {
				maxLength : 150,
				required: true,
				//requiredGroup: this._titleRequiredGroup
			},

			theme_es: {
				required: true,
				//requiredGroup: this._themeRequiredGroup
			},
			theme_en : {
				required: true,
				//requiredGroup: this._themeRequiredGroup
			},
			description_es: {
				required: true,
				//requiredGroup: this._descriptionRequiredGroup
			},
			description_en : {
				required: true,
				//requiredGroup: this._descriptionRequiredGroup
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
			authors: function(value) {
				var col = value.filterEmpties(),
					$error = $("p[name='authors'");
				if(!col || !col.length) {
					$error.html("El documento no tiene autores");
					return "<lang>Field required</lang>";
				}

				for (var i=0;i< col.length;i++){
					if (col.at(i).get("twitter_user")){
						//Twitter validation
						if (col.at(i).get("twitter_user").length<3 || col.at(i).get("twitter_user")[0]!="@"){
							$error.html("El documento tiene autores con twitter inválidos");
							return "Hay autores con twitter inválidos";
						}
					} 
					else{
						if (!col.at(i).get("position_en") || !col.at(i).get("position_en") || !col.at(i).get("name")){
							$error.html("El documento tiene autores con datos incompletos");
							return "Hay autores que no tienen algún campo completado";
						}
					}
					
				}
				 
		    }
	}},
	urlRoot: function() {
        return app.config.API_URL + "/document";
    },
    parse : function(response,options){

    	if ( options.saved ) return response;

    	response.labels_es  =  new Backbone.Collection(app.renameID(response.labels_es,"id_label","id"));
    	response.labels_en  =  new Backbone.Collection(app.renameID(response.labels_en,"id_label","id"));
    	response.pdfs_es  =  new Backbone.Collection(app.renameID(response.pdfs_es,"id_pdf","id"));
    	response.pdfs_en  =  new Backbone.Collection(app.renameID(response.pdfs_en,"id_pdf","id"));
    	response.authors =  new app.collection.Authors(app.renameID(response.authors,"id_author","id"));

        

    	return response;
    }
});