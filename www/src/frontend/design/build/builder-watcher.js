var watch = require('node-watch');
var exec = require('child_process').exec;
    
console.log("Watching");

watch(["../../css"], function(filename) {
    exec("node build.js",function (error, stdout, stderr){
        if (error) {
            console.log(error);
            console.log(stderr);
        }
        else{
            console.log(stdout);    
        }   
    });
});
