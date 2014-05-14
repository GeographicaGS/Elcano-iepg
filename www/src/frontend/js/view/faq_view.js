app.view.FAQ = Backbone.View.extend({
    _template : _.template( $('#faq_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","faq");
        this.render();
    },

    events: {
        "click .index li" : "goToEL"
    },
    
    onClose: function(){
        // Remove events on close
        //this.stopListening();
    },
    
    render: function() {
        
        this.$el.html(this._template());
        return this;
    },

    goToEL: function(e){
        var $e = $(e.target),
            idx = $e.index() +1;

        app.scrollToEl(this.$("[data-el="+idx+"]"));
    }


});