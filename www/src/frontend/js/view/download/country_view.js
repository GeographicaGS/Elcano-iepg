app.view.countryDownload = Backbone.View.extend({
    _template : _.template( $('#country_download_template').html() ),
    
    initialize: function() {
        
        this.render();

        
    },
    
    events:{
    	"click .pais": "paisClick",  	
    },
    


    onClose: function(){
        // Remove events on close
        this.stopListening();

    },
    
    render: function() {
        
        this.$el.html(this._template());
        
        $.ajax({
				url : "/api/countryfilter/" + app.lang,
				dataType: "json",
		        success: function(response) {
		        	response.results[0].name
		        }
		    }); 
        
        return this;
    },
    
    paisClick: function(e) {
    	if($(e.currentTarget).hasClass("active")){
    		$(e.currentTarget).removeClass("active");
    	}else{
    		$(e.currentTarget).addClass("active")
    	}
    	
    	$(".numPaises").text($(".pais.active").length);
    }
    

});