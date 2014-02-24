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

