var app = app || {};

String.prototype.endsWith = function(suffix) {
    return this.indexOf(suffix, this.length - suffix.length) !== -1;
};

// Link to the base view
app.baseView = null;

app.filters = [];


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

  
    if (app.config.DETECT_COUNTRY_LOCATION){
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
    }
    else{
        app.country = "ES";
        app.ini();  
    }
 
});

app.delay = (function(){
  var timer = 0;
  return function(callback, ms){
    clearTimeout (timer);
    timer = setTimeout(callback, ms);
  };
})();

app.resize = function(){
    console.log("resize me");
    // If device's screen width is smaller than 1024px, force to 1024px
    var vp = document.getElementById('appViewport');
    if(screen.width < 1024) {
        vp.setAttribute('content','width=1024');
    }else{
        vp.setAttribute('content','width=device-width, initial-scale=1');
    }

    var h = $(window).height()-this.$header.outerHeight(true) - this.$footer.outerHeight(true);
    this.$main.height(h);

    var toolDataMarginAndPadding = this.$tool_data.outerHeight(true) - this.$tool_data.height() + 20;

    this.$tool_data.height($(window).height() - this.$footer.outerHeight(true) - this.$tool_data.offset().top 
            - toolDataMarginAndPadding);

    this.map.resize();

    if(app.baseView.currentTool){
     
        app.delay(function(){
            app.baseView.currentTool.resizeMe();
        },500);
       

    }

}

app.ini = function(){

    this.lang = this.detectCurrentLanguage();

    // detect browser version
    if ( !this.isSupportedBrowser()){
        // Old IE explorer, not supported
        window.location = app.config["FRONT_URL"] + "/" + this.lang + "/html/browser_error.html";
        return;
    }

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
    
    if (app.config.CLEAR_CONTEXT_NOMATCHING_VERSION 
        && this.context.data.version != this.version){
        this.clearData();
    }

    this.filters =  localStorage.getItem("filters");
    if (!this.filters){
        this.filters = [];
    }
    else{
        this.filters = JSON.parse(this.filters);
    }

    this.refreshFiltersCtrl();

    app.map = new app.view.map({"container": "map"}).initialize();
    
    this.baseView = new app.view.Base();
    this.baseView.render();

    this.resize();

    $(window).resize(function(){
        app.resize();
    });

    // Check and show help
    if (!(localStorage['dontShowHelp'] === 'true')) {
        app.showHelp();
    }
    $("#help_btn").click(function(e){
        e.preventDefault();
        app.showHelp();
    });

    // Events for top menu on touch screens
    $("nav > div > img").click(function(){
        $(this).parent().toggleClass('opened');
    });

    $("nav > div").mouseenter(function(){
        $(this).addClass('opened');
    }).mouseleave(function(){
        $(this).removeClass('opened');
    });

    $("nav > div .quees").click(function(e){
        e.preventDefault();

        $("nav > div").eq(0).toggleClass('opened');
        $(this).toggleClass('opened'); 
    });

    $("nav > div .quees").mouseenter(function(){
        $(this).addClass('opened');
    }).mouseleave(function(){
        $(this).removeClass('opened');
    });

    $("nav > div .quees a").click(function(e){
        e.preventDefault();

        $("nav > div").eq(0).removeClass('opened');
    });

    $("#menu_btn li.explora a").click(function(e){
        e.preventDefault();
    });

    $("#map_zoom_in").click(function(e){
         e.preventDefault();
         app.map.zoomIn();
    });

    $("#map_zoom_out").click(function(e){
         e.preventDefault();
         app.map.zoomOut();
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

app.scrollToEl = function($el,offset){
    if (!offset) offset = 0;
    $('html, body').animate({
        scrollTop: $el.offset().top + offset
    }, 500);    
};

app.variableToString = function(variable,family){
    switch(variable){
        case "global":
            if (family == "iepg"){
                return "<lang>Índice Elcano de Presencia Global</lang>";
            }
            else if (family == "iepe"){
                return "<lang>Índice Elcano de Presencia Europea</lang>";
            }
            else{
                return "No definida"
            }
      
        case "economic_global":
            return "<lang>Presencia económica</lang>";
        case "soft_global":
            return "<lang>Presencia blanda</lang>";
        case "military_global":
            return "<lang>Presencia militar</lang>";

        // Military presence
        case "troops":
            return "<lang>Tropas</lang>";
        case "military_equipment":
            return "<lang>Equipamiento militar</lang>";

        // Economic presence
        case "energy":
            return "<lang>Energía</lang>";
        case "primary_goods":
            return "<lang>Bienes primarios</lang>";
        case "manufactures":
            return "<lang>Manufacturas</lang>";
        case "services":
            return "<lang>Servicios</lang>";
        case "investments":
            return "<lang>Inversiones</lang>";

        // Soft presences
        case "migrations":
            return "<lang>Migraciones</lang>";
        case "tourism":
            return "<lang>Turismo</lang>";
        case "sports":
            return "<lang>Deportes</lang>";
        case "culture":
            return "<lang>Cultura</lang>";
        case "information":
            return "<lang>Información</lang>";
        case "technology":
            return "<lang>Tecnología</lang>";
        case "science":
            return "<lang>Ciencia</lang>";
        case "education":
            return "<lang>Educación</lang>";
        case "cooperation":
            return "<lang>Cooperación</lang>";

        // TODO complete this mapping 
        default:
            return "No definida"
    }
}

app.countryToString = function(id_country){

    if(!id_country){
        return "";
    }
    
    // Temporal, we must add singapur to countries's geojson
    if (id_country == "SG"){
        if (app.lang == "es"){
            return "Singapur";  
        }
        else{
            return "Singapore";
        }
    }

    if (id_country.length == 2){


        for (var i=0;i<countriesGeoJSON.features.length;i++){

            if (countriesGeoJSON.features[i].properties.code == id_country){
                return countriesGeoJSON.features[i].properties["name_"+app.lang];
            }
        }
    }
    else{
        // It's a block
        return app.blocks[id_country]["name_" + app.lang];
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
        modal : true,
        helpers : {
            overlay : {
                css : {
                    'background' : 'rgba(255, 255, 255, 0.85)'
                }
            }
        }
    }  
};


app.fancyboxOptsHelper = function(){

    return   {
        padding : 0,
        autoHeight : false,
        autoSize : false,
        width : "90%",
        maxWidth : 960,
        closeBtn : false,
        modal : true,
        helpers : {
            overlay : {
                css : {
                    'background' : 'rgba(81, 81, 85, 0.94)'
                }
            }
        }
    }  
};

app.findCountry = function(id_country){
    for (var i=0;i<countriesGeoJSON.features.length;i++){

        if (countriesGeoJSON.features[i].properties.code == id_country){
            return $.extend(true, {}, countriesGeoJSON.features[i]);
            //return countriesGeoJSON.features[i];
        }
    }
};

app.getFilters = function(){
    return this.filters;
};

app.setFilters = function(filters){
    this.filters = filters;
    localStorage.setItem("filters", JSON.stringify(this.filters));
};

    
app.filterschanged = function(filters){
    this.setFilters(filters);

    // we've to remove from the context the countries which are not present in the filter
    this.context.removeCountriesInFilter();
    this.context.saveContext();

    if (app.baseView.currentTool){
        app.baseView.currentTool.forceFetchDataOnNextRender().render();
    }
  
    this.refreshFiltersCtrl();
};

app.refreshFiltersCtrl =  function(){
    if (this.filters.length){
        $("#ctrl_filter").addClass("enable");
    }
    else{
        $("#ctrl_filter").removeClass("enable");   
    }
};
      
app.events = {};
_.extend(app.events , Backbone.Events);

app.events.on("closepopup", function(popupView) {
    popupView.close();
}); 

app.events.on("filterschanged", function(filters) {
    app.filterschanged(filters);
}); 

app.clearData = function(){
    for (var key in localStorage){
        if (key != "dontShowHelp"){
            localStorage.removeItem(key);
        }
    }
}

app.reset = function(){
    this.clearData();
    window.location  = "/es";
}

app.countryCodeToStr = function(country){
    if (country.length == 2) {
        return country;
    }
    else{
        var s = country.substring(2);
        if (s=="E2"){
            return "EU";
        }
        else{
            return s;
        }
    }
};

app.getLoadingHTML = function(){
    return "<div class='co_loading'>" + 
                "<div class='loading'> " + 
                   
                        "<img src='/img/ELC_icon_loading_white.gif' />" + 
                        "<span><lang>Loading</lang></span>" + 
                   
                "</div>" +
            "</div>";
};

app.formatNumber = function (n,decimals){

    if (!decimals){
        decimals = 2;
    }

    if (n===null){
        return "";
    }

    if (typeof n == "number"){
        return parseFloat(sprintf("%."+ decimals + "f",n)).toLocaleString();
    }
    else{
        
        if (n.indexOf(".") != -1){
            n = sprintf("%."+ decimals + "f",n);
            return parseFloat(n).toLocaleString();    
        }
        else{

            return parseInt(n).toLocaleString();
        }    
    }
};

app.toolTypeToString = function(type){
    switch(type)
    {
        case "country":
            return "<lang>Ficha país</lang>";
        case "ranking":
            return "Ranking";
        case "contributions":
            return "<lang>Contribuciones de presencia</lang>";
        case "quotes":
            return "<lang>Cuotas de presencia</lang>";
        case "comparison":
            return "<lang>Presencia global frente a presencia europea</lang>";

    }
};

app.showHelp = function() {
    // Create and insert element
    if($('#help-bck').length == 0){

        loadHelpPage = function(idx, elem){
            // Remove old elements
            $('.elemHighlighted').removeClass('elemHighlighted');
            $('canvas').remove();

            $('#help-bck .content').html($($('#help_template').html())[idx]);
            if(elem){
                var $elem = $('#'+elem);
                $elem.addClass('elemHighlighted');
                var $content = $('#help-bck > .content > div');
                
                var canvas = document.createElement('canvas');
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                var elemPos = $elem.offset();
                var titlePos = $content.offset();
                var ctx = canvas.getContext("2d");
                ctx.setLineDash([12]);
                ctx.lineWidth = 2;
                ctx.strokeStyle = '#fdc300';
                if(titlePos.top > elemPos.top){
                    if(elemPos.left < canvas.width / 2) {
                        var $title = $content.find('h2').first();
                        ctx.moveTo($title.offset().left - 15 ,$title.offset().top + $title.height() / 2);
                        ctx.lineTo(elemPos.left + $elem.width(), elemPos.top + $elem.height() / 2);
                    }else{
                        ctx.moveTo(canvas.width / 2 ,titlePos.top - 15);
                        ctx.lineTo(elemPos.left + $elem.width() / 2 ,elemPos.top + $elem.height() - 15);
                    }
                }else{
                    var $title = $content.find('h2').first();
                    if(elemPos.left + $elem.width() < canvas.width / 2) {
                        ctx.moveTo($title.offset().left - 15 ,$title.offset().top + $title.height() / 2);
                        ctx.lineTo(elemPos.left + $elem.width(), elemPos.top);
                    }else{
                        ctx.moveTo(canvas.width / 2 ,titlePos.top + $content.height() + 15);
                        ctx.lineTo($elem.width() / 2 ,elemPos.top);
                    }
                }
                ctx.stroke();
                $('#help-bck').prepend(canvas);
            }

            if( localStorage['dontShowHelp'] === 'true' ){
                $container.find('.help-checkbox').addClass('checked');
            }
        }

        var $background = $('<div id="help-bck"><div class="content"></div></div>');
        var $container = $background.children().eq(0);
        $('body').prepend($background);

        // Load first page
        var $content = $($('#help_template').html());
        loadHelpPage(0);
        if( localStorage['dontShowHelp'] === 'true' ){
            $container.find('.help-checkbox').addClass('checked');
        }

        // Bind events
        $background.on('click', '.help-btn_continue', function(e){
            e.preventDefault();

            var $this = $(this);
            var next_idx = $this.attr('next-idx');
            var elem = $this.attr('elem');
            
            loadHelpPage(next_idx, elem);
        });

        $background.on('click', '.help-btn_goback', function(e){
            e.preventDefault();

            var $this = $(this);
            var prev_idx = $this.attr('prev-idx');
            var elem = $this.attr('elem');
            
            loadHelpPage(prev_idx, elem);
        });

        $background.on('click', '.help-checkbox', function(e){
            e.preventDefault();

            var $this = $(this);
            if ($this.hasClass('checked')){
                $this.removeClass('checked');
                localStorage['dontShowHelp'] = false;
            }else{
                $this.addClass('checked');
                localStorage['dontShowHelp'] = true;
            }
        });

        $background.on('click','.help-btn_close', function(e){
            e.preventDefault();
            
            // Remove old elements
            $('.elemHighlighted').removeClass('elemHighlighted');
            $('canvas').remove();
            // Unbind events
            $('.help-btn_next').off('click');
            $('.help-checkbox').off('click');
            $('.help-btn_close').off('click');

            $background.remove();
        });
    }
}

app.isTouchDevice = function () {
    return (('ontouchstart' in window)
        || (navigator.MaxTouchPoints > 0)
        || (navigator.msMaxTouchPoints > 0));
}

app.isSupportedBrowser = function(){
    var browser= app.getBrowser();

    if ((browser[0]=="IE" || browser[0] =="MSIE") && !isNaN(browser[1]) && parseFloat(browser[1]) < 11.0){
        return false;
    }
    if (browser[0]=="Firefox" &&  !isNaN(browser[1]) && parseFloat(browser[1]) < 24.0){
        return false;
    }

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