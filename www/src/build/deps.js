var deps = {}
deps.Backend = {};
deps.Backend.JS = {
	ThirdParty:{
		src: [
			"backend/js/lib/jquery-2.0.3.min.js",
			"backend/js/lib/underscore-min.js",
			"backend/js/lib/backbone-min.js",
			"backend/js/lib/d3.v3.min.js",			
			"backend/js/lib/jquery-dateFormat.min.js",
			"backend/js/lib/bootstrap/bootstrap.min.js",
			"backend/js/lib/jquery-ui-1.10.4.custom.min.js",
			"backend/js/lib/sprintf.min.js",
		],
		desc: "Third party library"
	}
	,Core: {
		src: [
			// Namespace
			"backend/js/namespace.js",
			// Config file
			"backend/js/config.js",
			
			"backend/js/validator.js",
			
			// --------------------
			// ------  Models ------
			// --------------------
			"backend/js/model/user_model.js",
			"backend/js/model/label_model.js",
			"backend/js/model/document_model.js",
			"backend/js/model/highlight_model.js",
			"backend/js/model/new_model.js",
			
			// --------------------
			// --- Collections  ---
			// --------------------
			"backend/js/collection/label_collection.js",			
			"backend/js/collection/document_collection.js",
			"backend/js/collection/highlighs_published_collection.js",
			"backend/js/collection/highlighs_unpublished_collection.js",
			"backend/js/collection/new_collection.js",
			
			// --------------------
			// ------  Views ------
			// --------------------
			// Docs Views
			"backend/js/view/docs/docs_list_view.js",
			"backend/js/view/docs/docs_document_view.js",
			"backend/js/view/docs/docs_form_view.js",
			// User view
			"backend/js/view/user_view.js",

			// Highlights views
			"backend/js/view/highlights/highlights_list_view.js",
			"backend/js/view/highlights/highlights_view.js",
			"backend/js/view/highlights/highlights_form_view.js",

			// News views
			"backend/js/view/news/news_form_view.js",
			"backend/js/view/news/news_list_view.js",
			"backend/js/view/news/news_detail_view.js",

			// router
			"backend/js/router.js",
			// app
			"backend/js/app.js",
		],
		desc: "Core library."
	}
};

deps.Backend.CSS = {
	ThirdParty:{
		src : [			
			"backend/js/lib/bootstrap/bootstrap.min.css"
		]
	},
	Core: {
		src: [
			"backend/css/styles.css"
		]
	}
};

deps.Frontend = {};
deps.Frontend.JS = {
	ThirdParty:{
		src: [
			"frontend/js/lib/jquery-2.0.3.min.js",
			"frontend/js/lib/underscore-min.js",
			"frontend/js/lib/backbone-min.js",
			"frontend/js/lib/d3.v3.min.js",	
			"frontend/js/lib/jquery-ui/jquery-ui-1.10.4.custom.min.js",			
		],
		desc: "Third party library"
	}
	,Core: {
		src: [
			// Namespace
			"frontend/js/namespace.js",
			// Config file
			"frontend/js/config.js",

			// --------------------
			// ------  Models ------
			// --------------------
			"frontend/js/model/docs/document_model.js",
			"frontend/js/model/home/countries_model.js",

			
			// --------------------
			// --- Collections  ---
			// --------------------
			"frontend/js/collection/home/latest_news_collection.js",
			"frontend/js/collection/home/slider_collection.js",
			"frontend/js/collection/docs/docs_collection.js",
			"frontend/js/collection/docs/label_collection.js",
			"frontend/js/collection/news/news_collection.js",
			
			// --------------------
			// ------  Views ------
			// --------------------
			"frontend/js/view/home/latest_news_view.js",
			"frontend/js/view/home/slider_view.js",
			"frontend/js/view/home/home_view.js",
			"frontend/js/view/home/country_popup_view.js",
			"frontend/js/view/docs/docs_list_view.js",
			"frontend/js/view/docs/docs_detail_view.js",

			"frontend/js/view/news/news_list_view.js",

			"frontend/js/view/error_view.js",
			"frontend/js/view/notfound_view.js",
			"frontend/js/view/contact_view.js",
			"frontend/js/view/faq_view.js",

			"frontend/js/view/about/about_view.js",

			// router
			"frontend/js/router.js",
			// app
			"frontend/js/app.js",
		],
		desc: "Core library."
	}
};

deps.Frontend.CSS = {
	ThirdParty:{
		src : [
			
		]
	},
	Core: {
		src: [
			"frontend/css/reset.css",
			"frontend/css/base.css",
			"frontend/css/styles.css",
			"frontend/css/home.css",
			"frontend/css/docs.css"
		]
	}
};

if (typeof exports !== 'undefined') {
	exports.deps = deps;
}

