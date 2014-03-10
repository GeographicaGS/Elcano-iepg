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
			"backend/js/lib/bootstrap/bootstrap.min.js"
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
			
			// --------------------
			// --- Collections  ---
			// --------------------
			"backend/js/collection/label_collection.js",			
			"backend/js/collection/document_collection.js",
			// --------------------
			// ------  Views ------
			// --------------------
			// Docs Views
			"backend/js/view/docs/docs_list_view.js",
			"backend/js/view/docs/docs_document_view.js",
			"backend/js/view/docs/docs_form_view.js",
			// User view
			"backend/js/view/user_view.js",
			"backend/js/view/home_view.js",
			"backend/js/view/news_view.js",
			
			
			
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
			"backend/html/css/layout.css",
			"backend/css/render.css",
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
			
			// --------------------
			// --- Collections  ---
			// --------------------
			
			// --------------------
			// ------  Views ------
			// --------------------
			"frontend/js/view/home_view.js",
			"frontend/js/view/about_view.js",

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
		src : []
	},
	Core: {
		src: [
			"frontend/css/reset.css",
			"frontend/css/base.css",
			"frontend/css/styles.css",
			"frontend/css/home.css"
		]
	}
};

if (typeof exports !== 'undefined') {
	exports.deps = deps;
}

