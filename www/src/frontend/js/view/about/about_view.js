app.view.About = Backbone.View.extend({
    _template : _.template( $('#about_template').html() ),
    
    initialize: function(options) {
        app.events.trigger("menu","about");
        this._section = options.section;
        this.render();
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {
        
        this.$el.html(this._template({
            "section" : this._section
        }));
        return this;
    }
});