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
        "click #news ul li" :"selectNewsMenu"
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
        return this;
    }
});