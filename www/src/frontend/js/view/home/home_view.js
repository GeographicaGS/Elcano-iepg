app.view.Home = Backbone.View.extend({
    _template : _.template( $('#home_template').html() ),
    _currentCountry : null,
    
    initialize: function() {
        app.events.trigger("menu","home");
        
        this.latestNews = new app.view.LatestNews();
        this.slider = new app.view.Slider();
        this.countryPopup = new app.view.CountryPopup({
            parent: this
        });
        this.render();

        var self = this;

        $("body").on("mouseup",function (e){

            if (!self.$popupCountry.is(e.target) // if the target of the click isn't the container...
                 && self.$popupCountry.has(e.target).length === 0) // ... nor a descendant of the container
            {
                self.$popupCountry.fadeOut(300);
            }

            if (!self.$popupYear.is(e.target) // if the target of the click isn't the container...
                 && self.$popupYear.has(e.target).length === 0) // ... nor a descendant of the container
            {
                self.$popupYear.fadeOut(300);
            }

        });
    },
    
    events:{
        "mouseenter #explora_desc button" : "hoverExploraDesc",
        "mouseleave #explora_desc button" : "outExploraDesc",
        "click #explora_desc button" : "goToStructure",
        "click #news ul li" :"selectNewsMenu",
        "click #year" : "togglePopupYear",
        "click #popup_year a" : "selectYear",
        "click #country": "togglePopupCountry",
        "click button.go_explora": "goExplora"

    },
    
    hoverExploraDesc: function(e){

        var $el = $(e.target),
            id = $el.attr("class");

        this.$explora_desc.find("p").hide();
        this.$explora_desc.find("p[data-el="+id+"]").show();
        this.$explora.removeClass("eco").removeClass("military").removeClass("soft");
        $el.siblings("button").css("opacity","0.3");
        this.$explora.addClass(id);
    },

    outExploraDesc: function(e){
        var $el = $(e.target),
            id = $el.attr("class");

        this.$explora_desc.find("p").hide();
        this.$explora.removeClass("eco").removeClass("military").removeClass("soft");
        this.$explora_desc.find("p[data-el=default]").show();
        $el.siblings("button").css("opacity","1");

    },

    selectNewsMenu: function(e){
        var $el = $(e.target).closest("li"),
            idx = $el.parent().children().index($el);

        $el.parent().children().removeAttr("selected");
        $el.attr("selected",true);
    
        this.latestNews.load(idx);

    },

    onClose: function(){
        // Remove events on close
        this.stopListening();

        this.latestNews.close();
        $("body").off("mouseup");
    },
    
    render: function() {
        
        this.$el.html(this._template());
        this.$explora = this.$("#explora");
        this.$explora_desc = this.$("#explora_desc");
        this.$("#co_news").html(this.latestNews.el);
        this.$("#carousel").html(this.slider.el);
        this.$popupCountry = this.$("#popup_country");
        this.$popupCountry.html(this.countryPopup.el);
        this.$popupYear = this.$("#popup_year");

        this.$year = this.$("#year");
        this.$country = this.$("#country");
        this.$co_country = this.$("#co_country");
        return this;
    },

    togglePopupYear: function(){
        //this.$popupYear.fadeIn(300);
        if (this.$popupYear.is(":visible")){
            //this.$popupYear.slideUp(300);
            this.$popupYear.fadeOut(300);
        }
        else{
            //this.$popupYear.slideDown(300);
            this.$popupYear.fadeIn(300);
        }
    },

    selectYear: function(e){
        var $e = $(e.target),
            year = parseInt($e.html());

        this.$year.html(year);
        this.togglePopupYear();
        $e.parent().siblings().removeAttr("selected");
        $e.parent().attr("selected",true);

    },

    togglePopupCountry: function(){
        //this.$popupYear.fadeIn(300);
        if (this.$popupCountry.is(":visible")){
            //this.$popupYear.slideUp(300);
            this.$popupCountry.fadeOut(300);
        }
        else{
            //this.$popupYear.slideDown(300);
            this.$popupCountry.fadeIn(300);
        }
    },

    selectCountry: function(code,name){
        this.togglePopupCountry();
        this._currentCountry = {
            "code" : code,
            "name" : name
        };
        this.$country.html(name);
        this.$co_country.removeClass("invalid");

    },

    getCountry: function(){
        return this._currentCountry;
    },

    goToStructure: function(){
        app.router.navigate(app.router.langRoutes["_link about infr"][app.lang],{trigger: true});
    },

    goExplora: function(e){
        e.preventDefault();
        
        if (this._currentCountry){
            window.location = app.config.EXPLORA_URL + "/" + app.lang + "/country/iepg/global/" +
                    this._currentCountry.code + "/" + this._currentCountry.code + "/" + $("#year").html();
        }
        else{
            this.$co_country.addClass("invalid");
        }
    }


});