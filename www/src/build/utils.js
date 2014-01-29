var fs = require('fs'),
	tmp = "build/tmp",
	deps = require("./deps.js").deps;

function combineFiles (files) {
	var content = '';
	for (var i = 0, len = files.length; i < len; i++) {
		content += fs.readFileSync(files[i], 'utf8') +"\n\n";		
	}
	return content;
}
exports.combineFiles = combineFiles;

function getFiles(deps) {
	var files = [];

	for (var i in deps.src) {
		files.push(deps.src[i]);
	}

	return files;
};
exports.getFiles = getFiles;

function getJSThirpartyCombined(deps){
    var filesThirdParty = getFiles(deps.JS.ThirdParty);
    return combineFiles(filesThirdParty)
};
exports.getJSThirpartyCombined = getJSThirpartyCombined;

function loadSilently(path) {
	try {
		return fs.readFileSync(path, 'utf8');
	} catch (e) {
		return null;
	}
};
exports.loadSilently = loadSilently;

function createDirIfNotExist(path)
{
	if (!fs.existsSync(path)) {
		fs.mkdirSync(path);
	}
}

exports.createDirIfNotExist=  createDirIfNotExist;

function getTmpFolder(env)
{
	return ( env ? tmp + "/" + env : tmp);
}
exports.getTmpFolder = getTmpFolder;

function getDeps(env)
{
	return env == "backend" ? deps.Backend : deps.Frontend;
}
exports.getDeps = getDeps;


exports.tmp = tmp;
