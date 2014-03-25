app.view.Home = Backbone.View.extend({
    _template : _.template( $('#home_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","home");
        
        this.latestNews = new app.view.LatestNews();
        this.slider = new app.view.Slider();
        this.render();
    },

    events:{
        "mouseenter #explora_desc button" : "hoverExploraDesc",
        "mouseleave #explora_desc button" : "outExploraDesc",
        "click #news ul li" :"selectNewsMenu",
        "click #year" : "togglePopupYear",
        "click #popup_year a" : "selectYear"
    },
    
    hoverExploraDesc: function(e){

        var $el = $(e.target),
            id = $el.attr("class");

        this.$explora_desc.find("p").hide();
        this.$explora_desc.find("p[data-el="+id+"]").show();
        this.$explora.removeClass("eco").removeClass("military").removeClass("soft");
        this.$explora.addClass(id);
    },

    outExploraDesc: function(e){
        var $el = $(e.target),
            id = $el.attr("class");

        this.$explora_desc.find("p").hide();
        this.$explora.removeClass("eco").removeClass("military").removeClass("soft");
        this.$explora_desc.find("p[data-el=default]").show();
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
    },
    
    render: function() {
        
        this.$el.html(this._template());
        this.$explora = this.$("#explora");
        this.$explora_desc = this.$("#explora_desc");
        this.$("#co_news").html(this.latestNews.el);
        this.$("#carousel").html(this.slider.el);
        this.$popupYear = this.$("#popup_year");
        this.$year = this.$("#year");
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

    }
});