app.model.Document = Backbone.Model.extend({
	_titleRequiredGroup : [ "title_es","title_en"],
	_themeRequiredGroup : [ "theme_es","theme_en"],
	_descriptionRequiredGroup : [ "theme_es","theme_en"],
	validation: function (){
		return {
			title_es: {
				requiredGroup: this._titleRequiredGroup
			},
			title_en : {
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
				required: false,
				pattern : "url"
			},
			link_en : {
				required: false,
				pattern : "url"
			},
			authors: function(value) {
				if(!value || !value.length) {
					return "<lang>Field required</lang>";
				}
		    }
			
			

	}},
	urlRoot: function() {
        return app.config.API_URL + "/document";
    }
	
  	
});