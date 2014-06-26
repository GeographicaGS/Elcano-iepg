var fs = require('fs'),
    pg = require('pg'),  
    langs = ["en","es"],    
    config = require("./config.js").config,
    conString = "postgres://"+config.database.user + ":" + config.database.password + "@" + config.database.host + ":" + config.database.port+ "/" + config.database.db,
    utils = require("./utils.js");

function getLangTags(s){
    var matches =  s.match( /<lang>(.*?)<\/lang>/g);
    if (matches) {
        return matches.map(function(val){
            return val.replace(/<\/?lang>/g,'');
        });
    }
    else{
        return [];    
    }
    
}

function replaceLangString(str,origin,target){
    origin = origin.replace("(","\\(");
    origin = origin.replace(")","\\)");
    var regex = new RegExp("<lang>"+ origin + "</lang>","g");
    return str.replace(regex,target);
}

function executeQuery(sql,callback) {
    var client = new pg.Client(conString);
    client.connect(function(err) {
        if(err){
            console.error('could not connect to postgres', err);
            callback(err,null);
            return;
        }
        client.query(sql, function(err, result) {
            if(err)
            {
                console.error('error running query', err);
                callback(err,null);
                return;
            }
            client.end();
            callback(err,result);
            return;
        });
    });
}

exports.translate = function(env,callback,debug){
    var tmp = utils.getTmpFolder(env),
        templates = fs.readFileSync(tmp+"/main-template-src.html", 'utf8'),
        templatesKeys = getLangTags(templates),
        
        js = fs.readFileSync(tmp+"/main.js", 'utf8'),
        jsKeys = getLangTags(js),
        
        index = fs.readFileSync(env +"/js/template/index.html", 'utf8'),
        indexKeys = getLangTags(index),
        
        allKeys = templatesKeys.concat(jsKeys).concat(indexKeys);

        
    function getDBKeys(callback){        
        executeQuery("SELECT * from www.translation",function(err,result){
            if (err) {
                callback(null);
            }
            else{                
                var dbKeys = {}
                for (i in result.rows){
                    var row = result.rows[i]                
                    dbKeys[row.key] = {}
                    for (l in langs){
                        dbKeys[row.key][langs[l]] = row[langs[l]];
                    }
                }               
                
                callback(dbKeys);
            }
        });    
    }
    
    function insertMissingKeys(dbKeys,callback){
        
        // check if the current keys are in the database. If not, we insert it        
        var keysToInsert = [];
        for (i in allKeys)
        {
            var k = allKeys[i];
            // Does the key exist? Is the key already in the array?
            if( (!k || !dbKeys.hasOwnProperty(k))
                && (keysToInsert.indexOf(k) ==-1)) {
                keysToInsert.push(k);
            }
        }
        
        if (keysToInsert.length>0) {
            // Insert new keys in database
            
            // Build SQL sentence
            var sql = "INSERT INTO www.translation VALUES ";
            
            for (i in keysToInsert){
                k = keysToInsert[i];
                sql += "('"+ k +"',NULL,NULL),";
            }
            
            sql = sql.slice(0,-1) + ";";
            
            executeQuery(sql,function(err,result){
                callback();
            });
            
            
        }
        else{
            callback();    
        }
    }
    
    
    function applyTranslations(dbKeys){
        // Create translations dictionary
        dict = {};
        for (i in allKeys)
        {
            var k = allKeys[i];
            dict[k] = {};
            // Does the key exist?
            if (!k || !dbKeys.hasOwnProperty(k) ) {
                // key missing
                for (l in langs){
                    //dict[k][langs[l]] = "<span class='translation_error'>" + k + "</span>";
                    
                    if (debug){
                        dict[k][langs[l]] = k;
                    }
                    else{
                        dict[k][langs[l]] = "<span class='translation_error'>" + k + "</span>";    
                    }
                }
            }
            else{
                // key exist                
                for (l in langs){
                    if (dbKeys[k][langs[l]]) {
                        dict[k][langs[l]] = dbKeys[k][langs[l]];
                    }
                    else{
                        if (debug){
                            dict[k][langs[l]] = k;
                        }
                        else{
                            dict[k][langs[l]] = "<span class='translation_error'>" + k + "</span>";    
                        }
                    }
                }
            }
        }
        
        // Here we've the dictonary created. Let's replace strings
        // Translations for template in all languages
        var template_translations = {};
        // Translations for template in all languages
        var js_translations = {};
        // Translations for index.html in all languages
        var index_translations = {};
        
        for (l in langs){
            lng = langs[l];
            template_translations[lng] = templates;
            js_translations[lng] = js;
            index_translations[lng] = index;
        }
            
        for (k in dict){
            for (l in langs){
                lng = langs[l];
                template_translations[lng] = replaceLangString(template_translations[lng],k,dict[k][lng]);
                js_translations[lng] = replaceLangString(js_translations[lng],k,dict[k][lng]);
                index_translations[lng] = replaceLangString(index_translations[lng],k,dict[k][lng]);
            }
        }
        
        for (l in langs){
            lng = langs[l];
            var name = tmp + "/template-"+lng + ".html";
            fs.writeFileSync(name, template_translations[lng]);
            console.log("\tSaved "+ name);
            
            name = tmp + "/main-"+lng + ".min.js";
            fs.writeFileSync(name, js_translations[lng]);
            console.log("\tSaved "+ name);
            
            var name = tmp + "/index-"+lng + ".html";
            fs.writeFileSync(name, index_translations[lng]);
            console.log("\tSaved "+ name);
        }
        
        
        // Now we've the template file and the js file translated. Let's write it to temp folder.
        callback();
        
    }
    
    // get db keys
    getDBKeys(function(dbKeys){
        // Insert missing keys in database
        insertMissingKeys(dbKeys,function(){
            applyTranslations(dbKeys);
        });
    });    
    
}