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
			// Config file
			"backend/js/config.js",
			// models
			"backend/js/model/user_model.js",
			// views
			"backend/js/view/user_view.js",
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
			"backend/css/layout.css",
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
			"frontend/js/lib/jquery-dateFormat.min.js",
			"frontend/js/lib/bootstrap/bootstrap.min.js"
		],
		desc: "Third party library"
	}
	,Core: {
		src: [
			// Config file
			"frontend/js/config.js",
			
		],
		desc: "Core library."
	}
};

deps.Frontend.CSS = {
	ThirdParty:{
		src : [			
			"frontend/js/lib/bootstrap/bootstrap.min.css"
		]
	},
	Core: {
		src: [
			"frontend/css/layout.css",
			"frontend/css/render.css",
		]
	}
};

if (typeof exports !== 'undefined') {
	exports.deps = deps;
}
