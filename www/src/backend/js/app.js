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
        app.router.navigate($(this).attr("href"),{trigger: true});
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
    
    //Backbone.history.start();root: "/public/search/"
    Backbone.history.start({pushState: true,root: this.config.BASE_PATH + this.detectCurrentLanguage()})

    
    // Is the user logged in ?
    this._user.once('sync',function(){
        if (!this._user.get("id")){
            // user not logged            
            this._logged = false;
            this.login();
        }
        else{
            this._logged = true;
            app.router.navigate("user", {trigger: true});
        }
    },this);
    this._user.fetch();
};

app.showView = function(view) {
    if (this.currentView){
      this.currentView.close();
    }
 
    this.currentView = view;
    this.currentView.render();    
 
    $("#app_container").html(this.currentView.el);  
}

app.login = function(){    
    this.showView(new app.view.LoginView());
};

app.logout = function(){
    var self = this;
    $.get(app.config.API_URL + "/user/logout",function(){
        self.router.navigate("");
        self._user = new app.model.User();
        self._logged = false;
        self.login();
    });
};


app.getUser = function(){
    return this._user;
}

