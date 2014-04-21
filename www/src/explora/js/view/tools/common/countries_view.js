app.view.tools.common.Countries = Backbone.View.extend({
    el: "#country_panel",
    render: function(){
        this.$el.html("Contenido de los países");
    },
    onClose: function(){
        // Remove events on close
        this.stopListening(); 
    }   
}); 