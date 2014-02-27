var ENTER_KEY = 13;

Backbone.View.prototype.close = function(){
  this.remove();
  this.unbind();
  
  if (this.onClose){
    this.onClose();
  }
}

$(function() {
   $.fn.serializeObject = function()
    {
        var o = {};
        var a = this.serializeArray();
        $.each(a, function() {
            if (o[this.name] !== undefined) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return o;
    };
    
    String.prototype.endsWith = function(suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };
    
    $("body").on("click","a",function(e){
        if ($(this).attr("target")=="_blank"){
            return;
        }
        e.preventDefault();
        var href = $(this).attr("href");
        if (href=="#back") {
            history.back();
        }
        else if (href!="" && href!="#") {
            app.router.navigate($(this).attr("href").substring(3),{trigger: true});
        }
        
    });
    
    $("button#logout").click(function(){
        app.logout();
    });

    app.ini();
    
});

app.detectCurrentLanguage = function(){
    // Detect lang analyzing the URL
    if (document.URL.indexOf("/es/") != -1 || document.URL.endsWith("/es")) {        
        return "es";
    }
    else if (document.URL.indexOf("/en/") != -1 || document.URL.endsWith("/en")) {        
        return "en";
    }
    
    return null;
};
app.ini = function(){
    this._user = new app.model.User();
    this.router = new app.router();
    
    this.lang = this.detectCurrentLanguage();
    this.basePath = this.config.BASE_PATH + this.lang;
    
  
    // Is the user logged in ?
    this._user.once('sync',function(){
        if (!this._user.get("id")){
            // user not logged. go to login
           this.goLogin();
        }
        else{
            this._logged = true;
              //Backbone.history.start();root: "/public/search/"
            Backbone.history.start({pushState: true,root: this.basePath });
            //app.router.navigate("user", {trigger: true});
        }
    },this);
    this._user.fetch({
        error: function(){
            app.goLogin();
        }
    });
};

app.showView = function(view) {
    if (this.currentView){
      this.currentView.close();
    }
 
    this.currentView = view;
    this.currentView.render();    
 
    $("#app_container").html(this.currentView.el);  
}

app.logout = function(){
    var self = this;
    $.get(app.config.API_URL + "/user/logout",function(){
        self.goLogin();
    });
};

app.goLogin = function(){
    window.location = "/" + this.basePath + "/login.html";
};

app.getUser = function(){
    return this._user;
}

app.events = {};

_.extend(app.events , Backbone.Events);

app.events.on("menu", function(id){
    var $menu = $("ul.nav-sidebar");
    $menu.children().removeClass("active");
    $menu.find("#"+id).addClass("active");
});

app.scrollTop = function(){
    var body = $("html, body");
    body.animate({scrollTop:0}, '500', 'swing', function() { 
       
    });
}

app.input = function(str){
    str = $.trim(str);
    if (str === "")
        return null;
    return str;
}

app.renameID = function(array,oldID,newID){
    for (var i=0;i< array.length;i++){
        array[i][newID] = array[i][oldID];
        delete array[i][oldID];
    }
    return array;
}


app.nl2br = function nl2br(str, is_xhtml) {
    var breakTag = (is_xhtml || typeof is_xhtml === 'undefined') ? '<br />' : '<br>';
    return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1' + breakTag + '$2');
}

// Tue, 25 Feb 2014 22:32:40 GMT
app.dateFormat = function(dateStr){
    var date = new Date(dateStr);
    
    var month = date.getMonth() + 1; //Months are zero based
    var day = date.getUTCDate(); 
    var year = date.getFullYear();
    
    if (day < 10) day = "0" + day;
    if (month < 10) month = "0" + month;
    return day +"/"+month+"/"+year;
}

/* dateStr must be a date in GMT Tue, 25 Feb 2014 22:32:40 GMT*/
app.dateTimeFormat = function(dateStr){
    var date = new Date(dateStr);
    
    var month = date.getMonth() + 1; //Months are zero based
    var day = date.getUTCDate(); 
    var year = date.getFullYear();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    
    if (month < 10) month = "0" + month;
    if (day < 10) day = "0" + day;
    if (hours < 10) hours = "0" + hours;
    if (minutes < 10) minutes = "0" + minutes;
    
    return day +"/"+month+"/"+year +" - " + hours + ":" + minutes ;
}
