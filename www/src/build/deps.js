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
			"frontend/js/view/legal_view.js",
			"frontend/js/view/privacity_view.js",

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


deps.Explora = {};
deps.Explora.JS = {
	ThirdParty:{
		src: [
			"explora/js/lib/jquery-2.0.3.min.js",
			"explora/js/lib/underscore-min.js",
			"explora/js/lib/backbone-min.js",
			"explora/js/lib/d3.v3.min.js",
			"explora/js/lib/fancybox/source/jquery.fancybox.pack.js",
			"explora/js/lib/sprintf.min.js",
			"explora/js/lib/leaflet-0.7.2.js",
			"explora/js/lib/countries.geojson",
			
		],
		desc: "Third party library"
	}
	,Core: {
		src: [
		
			// Namespace
			"explora/js/namespace.js",
			// Config file
			"explora/js/config.js",

			// --------------------
			// ------  Models ------
			// --------------------
			"explora/js/model/tools/country_tool_model.js",

			
			// --------------------
			// --- Collections  ---
			// --------------------
			"explora/js/collection/countries.js",
			"explora/js/collection/filter.js",
			"explora/js/collection/country_tool_map.js",
			
			// --------------------
			// ------  Views ------
			// --------------------
			"explora/js/view/base_view.js",
			
			// Tools views -- Commmon
			"explora/js/view/tools/tool_view.js", 
			"explora/js/view/tools/common/countries_view.js",
			"explora/js/view/tools/common/slider_view.js",
			"explora/js/view/tools/common/slider_singlepoint_view.js",

			// Tools views
			"explora/js/view/tools/country_tool_view.js",
			"explora/js/view/tools/ranking_tool_view.js",
			"explora/js/view/tools/contributions_tool_view.js",
			"explora/js/view/tools/quotes_tool_view.js",

			// Tools context object
			"explora/js/view/tools/context.js",

			"explora/js/view/country_selector_view.js",
			"explora/js/view/tool_selector_view.js",
			"explora/js/view/filter_view.js",
			"explora/js/view/notfound_view.js",
			"explora/js/view/error_view.js",

			//map
			"explora/js/map.js",
			// router
			"explora/js/router.js",
			// app
			"explora/js/app.js",
		],
		desc: "Core library."
	}
};

deps.Explora.CSS = {
	ThirdParty:{
		src : [
			"explora/js/lib/fancybox/source/jquery.fancybox.css",

		]
	},
	Core: {
		src: [
			"explora/js/lib/leaflet-0.7.2.css",
			"explora/css/reset.css",
			"explora/css/base.css",
			"explora/css/styles.css",
			"explora/css/tool.css",
		]
	}
};

if (typeof exports !== 'undefined') {
	exports.deps = deps;
}

