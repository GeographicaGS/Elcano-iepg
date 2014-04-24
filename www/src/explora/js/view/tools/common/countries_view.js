app.view.tools.common.Countries = Backbone.View.extend({
    el: "#country_panel",
    _template : _.template( $('#country_bar_template').html() ),

    initialize: function(options){
        this.plugin = options.plugin;
    },

    _events: {
        "click #ctrl_countries": "launchCountriesSelector"
    },

    launchCountriesSelector: function(){
        this.countrySelector = new app.view.CountrySelector();
       
    },

    render: function(){
        this.delegateEvents(this._events);

        this.$el.show().html(this._template({
            ctx: this.plugin.getGlobalContext().data,
        }));
    },

    onClose: function(){

    },

    close: function(){
        this.stopListening();

        this.undelegateEvents();
    
        this.$el.html("").hide();
  
        if (this.onClose){
            this.onClose();
        }
    },
}); 