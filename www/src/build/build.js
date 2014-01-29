var fs = require('fs'),
    jshint = require('jshint'),
    UglifyJS = require('uglify-js'),
	UglifyCSS = require('uglifycss'),       
	utils = require("./utils.js");



function getSizeDelta(newContent, oldContent, fixCRLF) {
	if (!oldContent) {
		return ' (new)';
	}
	if (newContent === oldContent) {
		return ' (unchanged)';
	}
	if (fixCRLF) {
		newContent = newContent.replace(/\r\n?/g, '\n');
		oldContent = oldContent.replace(/\r\n?/g, '\n');
	}
	var delta = newContent.length - oldContent.length;

	return delta === 0 ? '' : ' (' + (delta > 0 ? '+' : '') + delta + ' bytes)';
}



function combineFilesTemplate(files,rootTemplate) {
	var content = '';
	for (var i = 0, len = files.length; i < len; i++) {
		
		content += "<script type='text/template' id='"+files[i].slice(0,-5) +"'>\n" + fs.readFileSync(rootTemplate + files[i], 'utf8') +"</script>\n\n";		
	}
	return content;
}

function bytesToKB(bytes) {
    return (bytes / 1024).toFixed(2) + ' KB';
};

exports.buildJS = function (env,callback, version, buildName) {

	console.log("Building JS files");
	
	var tmp = utils.getTmpFolder(env),
		deps = utils.getDeps(env),
		files = utils.getFiles(deps.JS.Core);
	console.log('Concatenating and compressing ' + files.length + ' files...');

	var newSrc = utils.combineFiles(files),
	    pathPart = tmp + "/main" + (buildName ? '-' + buildName : ''),
	    srcPath = pathPart + '-src.js',
	    oldSrc = utils.loadSilently(srcPath),
	    srcDelta = getSizeDelta(newSrc, oldSrc, true);

	console.log('\tUncompressed: ' + bytesToKB(newSrc.length) + srcDelta);

	if (newSrc !== oldSrc) {		
		fs.writeFileSync(srcPath, newSrc);
		console.log('\tSaved to ' + srcPath);
	}
	
	var path = pathPart + '.js',
	    oldCompressed = utils.loadSilently(path),
		newCompressed =
			utils.getJSThirpartyCombined(deps)+
			UglifyJS.minify(newSrc, {
				warnings: true,
				fromString: true
			}).code;		
	    delta = getSizeDelta(newCompressed, oldCompressed);
	
	console.log('\tCompressed: ' + bytesToKB(newCompressed.length) + delta);
	
	if (newCompressed !== oldCompressed) {
		fs.writeFileSync(path, newCompressed);
		console.log('\tSaved to ' + path);
	}
	
	
	callback(env);
};

exports.buildCSS = function (env,callback, version, buildName){
	
	
	console.log("Building CSS files");
	var tmp = utils.getTmpFolder(env),
		deps = utils.getDeps(env),
		files = utils.getFiles(deps.CSS.Core);
		filesThirdParty = utils.getFiles(deps.CSS.ThirdParty);
	
	console.log('Concatenating and compressing ' + files.length + ' files...');

	var newSrc = utils.combineFiles(files),
	    pathPart = tmp + "/main" + (buildName ? '-' + buildName : ''),
	    srcPath = pathPart + '-src.css',

	    oldSrc = utils.loadSilently(srcPath),
	    srcDelta = getSizeDelta(newSrc, oldSrc, true);

	console.log('\tUncompressed: ' + bytesToKB(newSrc.length) + srcDelta);

	if (newSrc !== oldSrc) {		
		fs.writeFileSync(srcPath, newSrc);
		console.log('\tSaved to ' + srcPath);
	}
	
	var path = pathPart + '.min.css',
	    oldCompressed = utils.loadSilently(path),		
	    newCompressed =
			utils.combineFiles(filesThirdParty)+
			UglifyCSS.processString(newSrc, {
				maxLineLen : 500,
				expandVars : true 
			}),
	    delta = getSizeDelta(newCompressed, oldCompressed);

	
	console.log('\tCompressed: ' + bytesToKB(newCompressed.length) + delta);
	
	if (newCompressed !== oldCompressed) {
		fs.writeFileSync(path, newCompressed);
		console.log('\tSaved to ' + path);
	}
	
	callback(env);
}

function getTemplateFiles(tplFolder) {
	var files = fs.readdirSync(tplFolder);
	var response = [];
	for (i in files) {
		if (files[i] != "index.html") {
			response.push(files[i]);
		}
	}
	return response;
}

exports.buildTemplate = function (env,callback, version, buildName){
	
	console.log("Building Templates");
	
	var tmp = utils.getTmpFolder(env),
		tplFolder = env + "/js/template/",
		files = getTemplateFiles(tplFolder);
		
	console.log('Concatenating ' + files.length + ' files...');

	var newSrc = combineFilesTemplate(files,tplFolder),
	    pathPart = tmp + "/main-template" + (buildName ? '-' + buildName : ''),
	    srcPath = pathPart + '-src.html',

	    oldSrc = utils.loadSilently(srcPath),
	    srcDelta = getSizeDelta(newSrc, oldSrc, true);

	console.log('\tUncompressed: ' + bytesToKB(newSrc.length) + srcDelta);

	//small compression remove \t\n
	newSrc = newSrc.replace(/\n/g,"");
	newSrc = newSrc.replace(/\t/g,"");
	if (newSrc !== oldSrc) {		
		fs.writeFileSync(srcPath, newSrc);
		console.log('\tSaved to ' + srcPath);
	}
	
	callback(env);
}
