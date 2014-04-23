app.view.tools.common.Slider = Backbone.View.extend({
    el: "#slider",
   
    initialize: function(options){
        this.plugin = options.plugin;
    },

	render: function(){
        this.$el.show();
    },

    onClose: function(){
    
    },

    close: function(){
        this.stopListening();

        this.$el.html("").hide();
  
        if (this.onClose){
            this.onClose();
        }
    }
}); 