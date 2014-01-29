/*
Leaflet building, testing and linting scripts.

To use, install Node, then run the following commands in the project root:

    npm install -g jake
    npm install

To check the code for errors and build Leaflet from source, run "jake".
To run the tests, run "jake test".

*/

var build = require("./build/build.js");
var translate = require("./build/translate.js");
var resource = require("./build/resource.js");
var utils = require("./build/utils.js")

utils.createDirIfNotExist(utils.tmp);


function buildCSS(env){	
	build.buildCSS(env,buildUnderScoreTemplate);
}

function buildUnderScoreTemplate(env){	
	build.buildTemplate(env,complete);
}

desc("Combine and compress source files for the backend");
task("build-backend", {async: true}, function () {
	console.log("--------------------------------------");
	console.log("---------- BUILDING BACKEND ----------");
	console.log("--------------------------------------");
	utils.createDirIfNotExist(utils.tmp + "/backend");	
	build.buildJS('backend',buildCSS);
});

desc("Combine and compress source files for the frontend");
task("build-frontend", {async: true}, function () {
	console.log("\n--------------------------------------");
	console.log("---------- BUILDING FRONTEND ---------");
	console.log("--------------------------------------");
	utils.createDirIfNotExist(utils.tmp + "/frontend");	
	build.buildJS('frontend',buildCSS);
});

desc("Build frontend and backend");
task("build",["build-backend","build-frontend"]);

desc("Translate backend")
task("translate-backend", {async: true}, function () {
	console.log("\n----------------------------------------");
	console.log("---------- Translating BACKEND ---------");
	console.log("----------------------------------------");
	translate.translate("backend",complete);
});

desc("Translate frontend")
task("translate-frontend", {async: true}, function () {
	console.log("\n-----------------------------------------");
	console.log("---------- Translating FRONTEND ---------");
	console.log("-----------------------------------------");
	translate.translate("frontend",complete);
});

desc("Translate")
task("translate",["translate-backend","translate-frontend"])

desc("Generate resources backend")
task("resource-backend", {async: true}, function () {
	console.log("\n-----------------------------------------------");
	console.log("---------- BUILDING BACKEND RESOURCES ---------");
	console.log("-----------------------------------------------");
	resource.create("backend",complete,false);
});
desc("Generate resources frontend")
task("resource-frontend", {async: true}, function () {
	console.log("\n------------------------------------------------");
	console.log("---------- BUILDING FRONTEND RESOURCES ---------");
	console.log("------------------------------------------------");
	resource.create("frontend",complete,false);
});

desc("Generate resources")
task("resource", ["resource-backend","resource-frontend"]);


desc("Generate resources backend debug")
task("resource-backend-debug", {async: true}, function () {
	console.log("\n-----------------------------------------------");
	console.log("---------- BUILDING BACKEND RESOURCES ---------");
	console.log("-----------------------------------------------");
	resource.create("backend",complete,true);
});
desc("Generate resources frontend debug")
task("resource-frontend-debug", {async: true}, function () {
	console.log("\n------------------------------------------------");
	console.log("---------- BUILDING FRONTEND RESOURCES ---------");
	console.log("------------------------------------------------");
	resource.create("frontend",complete,true);
});

desc("Generate resources")
task("resource-debug", ["resource-backend-debug","resource-frontend-debug"]);


desc("Production builder")
task("default", ["build","translate","resource"],function(){
	console.log("\n\nBUILD COMPLETE SUCCESSFULLY\n\n");
});

desc("Debug builder")
task("debug", ["build","translate","resource-debug"],function(){
	console.log("\n\nDEBUG BUILD COMPLETE SUCCESSFULLY\n\n");
});


jake.addListener("complete", function () {
  process.exit();
});
