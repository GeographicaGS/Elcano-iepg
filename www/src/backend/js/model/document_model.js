app.model.Document = Backbone.Model.extend({
	_titleRequiredGroup : [ "title_es","title_en"],
	_themeRequiredGroup : [ "theme_es","theme_en"],
	_descriptionRequiredGroup : [ "description_es","description_en"],
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

			theme_es: {
				requiredGroup: this._themeRequiredGroup
			},
			theme_en : {
				requiredGroup: this._themeRequiredGroup
			},
			description_es: {
				requiredGroup: this._descriptionRequiredGroup
			},
			description_en : {
				requiredGroup: this._descriptionRequiredGroup
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
				var col = value.filterEmpties();
				if(!col || !col.length) {
					return "<lang>Field required</lang>";
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