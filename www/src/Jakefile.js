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

desc("Combine and compress source files for explora");
task("build-explora", {async: true}, function () {
	console.log("\n--------------------------------------");
	console.log("---------- BUILDING EXPLORA ---------");
	console.log("--------------------------------------");
	utils.createDirIfNotExist(utils.tmp + "/explora");	
	build.buildJS('explora',buildCSS);
});

desc("Build frontend, backend and explora");
task("build",["build-backend","build-frontend","build-explora"]);

desc("Translate backend")
task("translate-backend", {async: true}, function () {
	console.log("\n----------------------------------------");
	console.log("---------- Translating BACKEND ---------");
	console.log("----------------------------------------");
	translate.translate("backend",complete,false);
});

desc("Translate frontend")
task("translate-frontend", {async: true}, function () {
	console.log("\n-----------------------------------------");
	console.log("---------- Translating FRONTEND ---------");
	console.log("-----------------------------------------");
	translate.translate("frontend",complete,false);
});

desc("Translate explora")
task("translate-explora", {async: true}, function () {
	console.log("\n-----------------------------------------");
	console.log("---------- Translating EXPLORA ---------");
	console.log("-----------------------------------------");
	translate.translate("explora",complete,false);
});

desc("Translate")
task("translate",["translate-backend","translate-frontend","translate-explora"]);


desc("Translate backend-debug")
task("translate-backend-debug", {async: true}, function () {
	console.log("\n----------------------------------------");
	console.log("---------- Translating BACKEND ---------");
	console.log("----------------------------------------");
	translate.translate("backend",complete,true);
});

desc("Translate frontend-debug")
task("translate-frontend-debug", {async: true}, function () {
	console.log("\n-----------------------------------------");
	console.log("---------- Translating FRONTEND ---------");
	console.log("-----------------------------------------");
	translate.translate("frontend",complete,true);
});

desc("Translate explora-debug")
task("translate-explora-debug", {async: true}, function () {
	console.log("\n-----------------------------------------");
	console.log("---------- Translating EXPLORA ---------");
	console.log("-----------------------------------------");
	translate.translate("explora",complete,true);
});

desc("Translate")
task("translate-debug",["translate-backend-debug","translate-frontend-debug","translate-explora-debug"])

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

desc("Generate resources explora")
task("resource-explora", {async: true}, function () {
	console.log("\n------------------------------------------------");
	console.log("---------- BUILDING EXPLORA RESOURCES ---------");
	console.log("------------------------------------------------");
	resource.create("explora",complete,false);
});

desc("Generate resources")
task("resource", ["resource-backend","resource-frontend","resource-explora"]);


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

desc("Generate resources explora debug")
task("resource-explora-debug", {async: true}, function () {
	console.log("\n------------------------------------------------");
	console.log("---------- BUILDING EXPLORA RESOURCES ---------");
	console.log("------------------------------------------------");
	resource.create("explora",complete,true);
});

desc("Generate resources")
task("resource-debug", ["resource-backend-debug","resource-frontend-debug","resource-explora-debug"]);


desc("Production builder")
task("default", ["build","translate","resource"],function(){
	console.log("\n\nBUILD COMPLETE SUCCESSFULLY\n\n");
});

desc("Debug builder")
task("debug", ["build","translate-debug","resource-debug"],function(){
	console.log("\n\nDEBUG BUILD COMPLETE SUCCESSFULLY\n\n");
});

desc("Build backend")
task("build-backend-alone",["build-backend","translate-backend","resource-backend"],function(){
	console.log("\n\nBUILD BACKEND COMPLETE SUCCESSFULLY\n\n");
});

desc("Build backend DEBUG")
task("build-backend-alone-debug",["build-backend","translate-backend-debug","resource-backend-debug"],function(){
	console.log("\n\nDEBUG BUILD BACKEND COMPLETE SUCCESSFULLY\n\n");
});

desc("Build frontend")
task("build-frontend-alone",["build-frontend","translate-frontend","resource-frontend"],function(){
	console.log("\n\nBUILD FRONTEND COMPLETE SUCCESSFULLY\n\n");
});

desc("Build frontend DEBUG")
task("build-frontend-alone-debug",["build-frontend","translate-frontend-debug","resource-frontend-debug"],function(){
	console.log("\n\nDEBUG BUILD FRONTEND COMPLETE SUCCESSFULLY\n\n");
});

desc("Build explora")
task("build-explora-alone",["build-explora","translate-explora","resource-explora"],function(){
	console.log("\n\nBUILD EXPLORA COMPLETE SUCCESSFULLY\n\n");
});

desc("Build explora DEBUG")
task("build-explora-alone-debug",["build-explora","translate-explora-debug","resource-explora-debug"],function(){
	console.log("\n\nDEBUG BUILD EXPLORA COMPLETE SUCCESSFULLY\n\n");
});

jake.addListener("complete", function () {
  process.exit();
});
