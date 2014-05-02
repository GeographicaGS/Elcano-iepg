app.view.tools.common.Slider = Backbone.View.extend({
    el: "#slider",
   
    initialize: function(options){
        //$(window).on("resize", this.render);
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

    onClose: function(){
    
    },

    close: function(){
        this.stopListening();

        //$(window).off("resize", this.render);

        this.$el.html("").hide();
  
        if (this.onClose){
            this.onClose();
        }
    },

    render: function(){
        console.log("Render app.view.tools.common.Slider");
        this.$el.show();
    },
}); 