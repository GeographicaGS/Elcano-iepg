var watch = require('node-watch');
var exec = require('child_process').exec;

var param = (process.argv.length == 3 && process.argv[2]=="-debug") ? "-debug" : "",
    mode = " - [ Mode " + (param ? param : "production") + " ]";
    
console.log("Watching "+ mode );

watch(["backend"], function(filename) {
    exec("jake build-backend-alone" + param,function (error, stdout, stderr){
        if (error) {
            console.log(error);
            console.log(stderr);
        }
        else{
            console.log(stdout);    
        }   
    });
});

watch(["frontend"], function(filename) {
    exec("jake build-frontend-alone" + param,function (error, stdout, stderr){
        if (error) {
            console.log(error);
            console.log(stderr);
        }
        else{
            console.log(stdout);    
        }   
    });
});

watch(["explora"], function(filename) {
    exec("jake build-explora-alone" + param,function (error, stdout, stderr){
        if (error) {
            console.log(error);
            console.log(stderr);
        }
        else{
            console.log(stdout);    
        }   
    });
});





