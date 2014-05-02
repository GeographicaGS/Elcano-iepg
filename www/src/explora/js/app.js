var app = app || {};

String.prototype.endsWith = function(suffix) {
    return this.indexOf(suffix, this.length - suffix.length) !== -1;
};

// variables. Array of countries with the countries to filter by
app.filters = [];

// Link to the base view
app.baseView = null;


Backbone.View.prototype.close = function(){
    this.remove();
    this.unbind();
  
    if (this.onClose){
        this.onClose();
    }
}

$(function(){

    $("body").on("click","a",function(e){
        
        var attr = $(this).attr("jslink"),
            href = $(this).attr("href");

        if (attr!= undefined && attr!="undefined"){
            e.preventDefault();
            if (href=="#back") {
                history.back();
            }
            app.router.navigate($(this).attr("href").substring(3),{trigger: true});
        }

        if (href=="#"){
            e.preventDefault();
        }
    });
    
    $(document).ajaxError(function(event, jqxhr, settings, exception) {
        if (jqxhr.status == 404) { app.router.navigate("notfound",{trigger: true});} 
        else { app.router.navigate("error",{trigger: true});}
    });

    $.getJSON('http://freegeoip.net/json/', function(location) {
      // example where I update content on the page.
      // jQuery('#city').html(location.city);
      // jQuery('#region-code').html(location.region_code);
      // jQuery('#region-name').html(location.region_name);
      // jQuery('#areacode').html(location.areacode);
      // jQuery('#ip').html(location.ip);
      // jQuery('#zipcode').html(location.zipcode);
      // jQuery('#longitude').html(location.longitude);
      // jQuery('#latitude').html(location.latitude);
      // jQuery('#country-name').html(location.country_name);
      // jQuery('#country-code').html(location.country_code);
        app.country = location.country_code;
        app.ini();
    });
   
});

app.resize = function(){
    var h = $(window).height()-this.$header.outerHeight(true) - this.$footer.outerHeight(true);
    this.$main.height(h);

    var toolDataMarginAndPadding = this.$tool_data.outerHeight(true) - this.$tool_data.height();

    this.$tool_data.height($(window).height() - this.$footer.outerHeight(true) - this.$tool_data.offset().top 
            - toolDataMarginAndPadding);

    this.map.resize();
}

app.ini = function(){

    this.lang = this.detectCurrentLanguage();
    this.router = new app.router();
    this.basePath = this.config.BASE_PATH + this.lang;
    this.$extraPanel = $("#extra_panel");
    this.$popup = $("#popup");
    this.$main = $("main");
    this.$header = $("header");
    this.$footer = $("footer");
    this.$tool_data = $("#tool_data");
    this.$tool = $("#tool");

    // create the context
    this.context = new app.view.tools.context("global");
    this.context.restoreSavedContext();

    app.map.initialize();
    
    this.baseView = new app.view.Base();
    this.baseView.render();

    

    this.resize();

    $(window).resize(function(){
        app.resize();
    });

    

    Backbone.history.start({pushState: true,root: this.basePath });
};

app.detectCurrentLanguage = function(){
    if (document.URL.indexOf("/es/") != -1 || document.URL.endsWith("/es")) {return "es";}
    else if (document.URL.indexOf("/en/") != -1 || document.URL.endsWith("/en")) {return "en";}
    return null;
};

app.getJSURL = function(url){
    url = url ? "/" + url : "";
    return "/" + app.detectCurrentLanguage() + url;
};

app.showViewInExtraPanel = function(view) {
    if (this.currentViewExtra){
      this.currentViewExtra.close();
    }
 
    this.currentViewExtra = view;
    //this.currentView.render();    
 
    this.$extraPanel.html(this.currentViewExtra.el);  
    this.$extraPanel.show()
    app.scrollTop();
}

app.showViewInPopup = function(view) {
    if (this.currentViewPopup){
      this.currentViewPopup.close();
    }
 
    this.currentViewPopup = view;
    //this.currentView.render();    
 
    this.$popup.html(this.currentViewPopup.el);

    app.scrollTop();
}

app.scrollTop = function(){
    var body = $("html, body");
    body.animate({scrollTop:0}, '500', 'swing', function() { 
       
    });
};

app.scrollToEl = function($el){
    $('html, body').animate({
        scrollTop: $el.offset().top
    }, 500);    
};

app.variableToString = function(variable){
    switch(variable){
        case "IEPG":
        case "iepg":
            return "Índice Elcano de Presencia Global";
        case 2:
            return "Índice Elcano de Presencia Europea";

        // TODO complete this mapping 
        default:
            return "No definida"
    }
}

app.countryToString = function(id_country){
    for (var i=0;i<countriesGeoJSON.features.length;i++){

        if (countriesGeoJSON.features[i].properties.code == id_country){
            return countriesGeoJSON.features[i].properties["name_"+app.lang];
        }
    }
    
    return "No country name found";
    
}

app.isSMDevice = function(){
    return ($(window).width()<992);
}

app.fancyboxOpts = function(){

    return   {
        padding : 0,
        autoHeight : false,
        autoSize : false,
        width : "90%",
        maxWidth : 960,
        closeBtn : false,
        helpers : {
            overlay : {
                css : {
                    'background' : 'rgba(255, 255, 255, 0.85)'
                }
            }
        }
    }  
} 

app.events = {};
_.extend(app.events , Backbone.Events);

app.events.on("closepopup", function(popupView) {
    popupView.close();
}); 






