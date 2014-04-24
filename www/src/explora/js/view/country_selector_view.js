app.view.CountrySelector = Backbone.View.extend({
    _template : _.template( $('#country_selector_template').html() ),
    initialize: function(){
        this.collection = new app.collection.Countries();
        
        this.listenTo(this.collection, "reset",function(){
            this.render();
        });

        this.collection.fetch({reset: true});

        this.$el.html("<div class='loading'></div>");

        $.fancybox(this.$el, app.fancyboxOpts());
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
       
    },

    render: function(){
       
        this.$el.html(this._template({
            collection :   this.collection.toJSON()
        }));


        return this;
    }
    

});