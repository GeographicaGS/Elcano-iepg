var fs = require('fs'),    
    langs = ["en","es"],        
	utils = require("./utils.js");
    
    
function getScriptTag(file){
	return "<script type='text/javascript' src='" + file + "'></script>";	
}

function generateIndex(env,lang,templates,debug){
	
	var	tmp = utils.getTmpFolder(env),
		cdnPath = "../cdn/"+ env,
		index = fs.readFileSync(tmp +"/index-"+lang + ".html", "utf8");
	
	index = index.replace("<body>","<body>" + templates);
	
	if (!debug) {
		index = index.replace("</body>",getScriptTag("js/main.min.js") + "</body>").replace(/\n/g,"");
	}
	else{
		var deps = utils.getDeps(env),
			jsThird = deps.JS.ThirdParty.src;
		var jsCore =  deps.JS.Core.src;
		
		var js = "";
		
		for (i in jsThird) {
			js += getScriptTag("/src/" + jsThird[i]) +"\n\n";
		}
		
		for (i in jsCore) {
			js += getScriptTag("/src/" + jsCore[i]) +"\n\n";
		}
		
		index = index.replace("</body>",js + "</body>");
	}
    
   
	var newPath = cdnPath +"/" + lang +"/index.html",
		oldStream = utils.loadSilently(newPath)
    
	if (oldStream != index) {
		// index has been modified
		fs.writeFileSync(newPath, index);
		console.log("\tSaved "+ newPath);
	}
	else{
		// index has not been modified
		console.log("\t"+newPath + " (unchanged)");
	}
	
};

function copyFileIsNew(oldPath,newPath) {
    var oldStream = utils.loadSilently(oldPath)
        newStream = fs.readFileSync(newPath, 'utf8');
        
    // read file silently
    if (oldStream != newStream) {
        // file has changed
        fs.writeFileSync(oldPath, newStream);
        console.log("\tSaved "+oldPath);
    }
    else{
        // File has not changed
        console.log("\t"+oldPath + " (unchanged)");
    }
    
}

exports.create = function(env,callback,debug){
    console.log("Creating resources files" + (debug ? " (debug enable)" : ""));
	
	var tmp = utils.getTmpFolder(env),
		cdnPath = "../cdn/"+ env;
		
    for (i in langs){
        var lng = langs[i],
			cdnLangPath = cdnPath + "/" + lng,
			jsLangPath = cdnPath + "/" + lng +"/js";
		
		utils.createDirIfNotExist(cdnLangPath);
		utils.createDirIfNotExist(jsLangPath);
        // Recreate index.html
        templates = fs.readFileSync(tmp +"/template-"+lng+".html", "utf8");
        generateIndex(env,lng,templates,debug);
        
        // Refresh js main file
		if (!debug) {
			
			var jsNewPath = tmp +"/main-" + lng + ".min.js",
				jsOldPath = jsLangPath + "/main.min.js";
			copyFileIsNew(jsOldPath,jsNewPath);
		}
       
    }
    
    // Refresh css main file.
    var cssNewPath =  tmp +"/main.min.css",
        cssOldPath = cdnPath + "/css/main.min.css";
        copyFileIsNew(cssOldPath,cssNewPath);
		
	callback();
    
};