app.view.tools.common.Countries = Backbone.View.extend({
    el: "#country_panel",
    _template : _.template( $('#country_bar_template').html() ),

    initialize: function(options){
        
    },

    _events: {
        "click #ctrl_countries": "launchCountriesSelector",
        "click ul.country_bar a": "clickCountry",
        "click #ctrl_variables" : "clickAddVariableSelectorView"
    },

    _setListeners: function(){
    
    },

    bringToFront: function(){
        this.delegateEvents(this._events); 
        this._setListeners();
    },

    bringToBack: function(){
        this.undelegateEvents();
        this.stopListening();
    },

    render: function(){
        //TOREMOVE
        console.log("Render app.view.tools.common.Countries");
        this.$el.show().html(this._template({
            ctx: app.context.data,
        }));
    },

    onClose: function(){

    },
    
    close: function(){
        if (this._variableSelectorView){
            this._variableSelectorView.close();
        }

        this.undelegateEvents();
    
        this.$el.html("").hide();
  
        if (this.onClose){
            this.onClose();
        }
    },

    launchCountriesSelector: function(){
        console.log("launchCountriesSelector");
        this.countrySelector = new app.view.CountrySelector();
       
    },

    clickCountry: function(e){
        e.preventDefault();

        var $e = $(e.target).closest("a"),
            code = $e.attr("code");

        if (code){
            app.events.trigger("countryclick",code);
        }
        
    },
    
    clickAddVariableSelectorView: function(e){
        e.preventDefault();
        if (this._variableSelectorView){
            this._variableSelectorView.close();
        }

        this._variableSelectorView = new app.view.VariableSelector(); 
    },
}); 