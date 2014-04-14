var app = app || {};
app.events = {};
_.extend(app.events , Backbone.Events);
app.defaults = {};
app.ini = function(){
    app.ctx = app.defaults;
    this.lang=this.detectCurrentLanguage();
    this.router = new app.router();
    this.lang=='es' ? console.debug('selector idioma es') : console.debug('selector idioma en');
    this.$main = $("main");
    this.basePath = this.config.BASE_PATH + this.lang;
    Backbone.history.start({pushState: true,root: this.basePath });
};
app.detectCurrentLanguage = function(){
    if (document.URL.indexOf("/es/") != -1 || document.URL.endsWith("/es")) {return "es";}
    else if (document.URL.indexOf("/en/") != -1 || document.URL.endsWith("/en")) {return "en";}
    return null;
};
app.showView = function(view) {
    //if (this.currentView){this.currentView.close();}
    this.currentView = view; 
    this.$main.html(this.currentView.el);  
};
$(function(){
    $(document).ajaxError(function(event, jqxhr, settings, exception) {
        if (jqxhr.status == 404) { app.router.navigate("notfound",{trigger: true});} 
        else { app.router.navigate("error",{trigger: true});}
    });
    app.ini();
});