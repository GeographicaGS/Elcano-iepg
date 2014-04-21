app.view.tools.Plugin = Backbone.View.extend({
    ctx: null,
    el: "#tool",

    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePoint();
        this.countries = new app.view.tools.common.Countries();
    }, 
    
    getGlobalContext: function(){
        // leemos el conexto de la aplicacion del local store
        app.getGlobalContext();
    },

    setLocalContext: function(){

    },

    getLocalContext: function(){

    },

    setContext: function(){

    },

    renderTool: function(){
        // draw the tool. This method must be overwritten
        this.$el.html("Generic tool");        
    },

    renderMap: function(){
        // draw the map. This method must be overwritten
    },

    hideCountryBar : function(){
        this.slider.el.hide();
    },

    showCountryBar : function(){
        this.slider.el.show();
    },

    toggleCountryBar: function(){
        if (this.slider.is(":visible")){
            this.hideCountryBar();
        }
        else{
            this.showCountryBar();
        }
    },



    hideTool: function(){

    },

    render: function(){
        this.renderTool();
        this.slider.render();
        this.countries.render();

    },
    onClose: function(){
       // Remove events on close
       this.stopListening();
    }
});






