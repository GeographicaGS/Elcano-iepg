app.view.tools.common.Slider = Backbone.View.extend({
    el: "#slider",
	render: function(){
		this.$el.html("Contenido del slider");
    },

    onClose: function(){
        // Remove events on close
        this.stopListening(); 
    } 	
}); 