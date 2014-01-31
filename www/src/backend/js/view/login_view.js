app.view.LoginView = Backbone.View.extend({
    _template : _.template( $('#login_template').html() ),  
    initialize: function() {
        
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    // The DOM events specific to an item.
    events: {
      "click button" : "doLogin"
    },
    
    doLogin: function(e){
        e.preventDefault();
        
        $.ajax({
            url : app.config.API_URL + "/user/login",
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify($('form').serializeObject()),
            success: function(json){
                if (json.Login) {
                    app.router.navigate("user", {trigger: true});
                    app._logged = true;
                }
                else{
                    alert("Bad user or password");
                }
            }
        });
    },
    
    render: function() {
        this.$el.html(this._template());
        return this;
    }
});