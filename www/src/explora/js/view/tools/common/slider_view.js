app.view.tools.common.Slider = Backbone.View.extend({
    el: "#slider",
   
    initialize: function(options){
        this.plugin = options.plugin;
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



        this.$el.html("").hide();
  
        if (this.onClose){
            this.onClose();
        }
    },

    render: function(){
        this.$el.show();
    },
}); 