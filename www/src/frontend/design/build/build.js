var deps = ["reset.css","base.css","styles.css","home.css"];

var fs = require("fs");

function combineFiles (files) {
    var content = '';
    for (var i = 0, len = files.length; i < len; i++) {
        content += fs.readFileSync("../../css/" + files[i], 'utf8') +"\n\n";       
    }
    return content;
}

function build(){
    var files = combineFiles(deps),
        path = "main.css",
        less = require('less'),
        parser = new(less.Parser),
        newCssCompressed;

    parser.parse(files, function (e, tree) {
        newCssCompressed = tree.toCSS({
            // Minify CSS output
            compress: false
        }); 
    });
    
    fs.writeFileSync(path, newCssCompressed);

    console.log("Build completed successfully");
}

build();