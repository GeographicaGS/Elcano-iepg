var ENTER_KEY = 13;

Backbone.View.prototype.close = function(){
  this.remove();
  this.unbind();
  
  if (this.onClose){
    this.onClose();
  }
}

$(function() {
    


    String.prototype.endsWith = function(suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };

    $(document).ajaxError(function(event, jqxhr, settings, exception) {
        if (jqxhr.status == 404) {
            app.router.navigate("notfound",{trigger: true});
        } 
        else {
            app.router.navigate("error",{trigger: true});
        }
    });

    $("body").on("click","a",function(e){
        var href = $(this).attr("href");
        if ($(this).attr("target")=="_blank" || href=="/es" || href=="/en"){
            return;
        }

        e.preventDefault();
        if (href=="#back") {
            history.back();
        }

        else if (href!="" && href!="#") {
            app.router.navigate($(this).attr("href").substring(3),{trigger: true});
        }
    });

    $("body").on("click","#ctrl_language",function(e){
        var $el = $("#menu_language");
        if ($el.is(":visible")){
            $el.fadeOut(300);
        }
        else{
            $el.fadeIn(300);
        }
    });

    $("body").on("mouseenter","#menu li[data-has-submenu]",function(e){
        $(this).find(" > a").css("color","#28282b").css("background-color","#fdc300");
        $(this).find("ul").fadeIn(300);
    });
   
    $("body").on("mouseleave","#menu li[data-has-submenu]",function(e){
        $(this).find(" > a").css("color","").css("background-color","");
        $(this).find("ul").fadeOut(300);
    });

    $("body").on("click","#menu li[data-has-submenu],#menu li[data-submenu]",function(e){
        var $el = $(this).closest("[data-has-submenu]");
        $el.find(" > a").css("color","").css("background-color","");
        $el.find("ul").fadeOut(300);
    });

    app.ini();

    $(document).resize(function(){
        app.resizeMe();
    });

    app.resizeMe();
    
});

app.resizeMe = function(){
    $("main").css("min-height",$(window).height() - $("footer").height() - $("header").height());
};

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
    
    this.lang = this.detectCurrentLanguage();
    if (this.lang == "es"){
        $("#menu_language li:nth-child(1)").attr("selected",true);
    }
    else{
        $("#menu_language li:nth-child(2)").attr("selected",true);
    }

    // detect browser version

    if (!this.isSupportedBrowser()){
        // Old IE explorer, not supported
        window.location = "/" + this.lang + "/html/browser_error.html";
    }

    $("#lang_marker").html(this.lang);
    this.router = new app.router();
    this.basePath = this.config.BASE_PATH + this.lang;
    this.$main = $("main");
    this.$menu = $("#menu");
    //Backbone.history.start();root: "/public/search/"
    Backbone.history.start({pushState: true,root: this.basePath });

};

app.showView = function(view) {
    if (this.currentView){
      this.currentView.close();
    }
 
    this.currentView = view;
    //this.currentView.render();    
 
    this.$main.html(this.currentView.el);  
    app.scrollTop();
}

app.events = {};

_.extend(app.events , Backbone.Events);

app.events.on("menu", function(id){
   
    app.$menu.children().removeAttr("selected");
    app.$menu.find("[data-menu="+id+"]").closest("li").attr("selected",true);
});

app.scrollTop = function(){
    var body = $("html, body");
    body.animate({scrollTop:0}, '500', 'swing', function() { 
       
    });
}

app.scrollToEl = function($el){
    $('html, body').animate({
        scrollTop: $el.offset().top
    }, 500);    
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

app.urlify = function(text,attr) {
    if (!text){
        return ""
    }
    var exp = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/i;
    return text.replace(exp,"<a href='$1' "+ attr+ ">$1</a>"); 
}

app.loadingHTML = function(){
    return "<div class='container'>"
            +   "<div class='row'>"
            +       "<div class='grid-md-10 col-md-offset-2'>"
            +           "<div class='loading'><lang>Loading</lang></div>"
            +       "</div>"
            +   "</div>"
            + "</div>" ;
}

app.renameID = function(array,oldID,newID){
    for (var i=0;i< array.length;i++){
        array[i][newID] = array[i][oldID];
        delete array[i][oldID];
    }
    return array;
}

app.isSMDevice = function(){
    return ($(window).width()<992);
}

app.isSupportedBrowser = function(){
    var browser= app.getBrowser();

    alert(browser);
    return true;
};

app.getBrowser = function(){
    var ua= navigator.userAgent, tem, 
    M= ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*([\d\.]+)/i) || [];
    if(/trident/i.test(M[1])){
        tem=  /\brv[ :]+(\d+(\.\d+)?)/g.exec(ua) || [];
        return 'IE '+(tem[1] || '');
    }
    M= M[2]? [M[1], M[2]]:[navigator.appName, navigator.appVersion, '-?'];
    if((tem= ua.match(/version\/([\.\d]+)/i))!= null) M[2]= tem[1];
    return M;
};