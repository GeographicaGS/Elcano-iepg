app.view.yearDownload = Backbone.View.extend({
    _template : _.template( $('#year_download_template').html() ),
    
    initialize: function() {
        
//        this.render();

        
    },
    
    events:{
    	"click .celda": "yearClick",
    	
    },
    


    onClose: function(){
        // Remove events on close
        this.stopListening();

    },
    
    render: function() {
        
        this.$el.html(this._template());
        
        var self = this;
        $(app.config.SLIDER).each(function() {
        	self.$(".yearList").append("<div class='celda'>" + this.getFullYear() + "</div>");
        });
        
        return this;
    },


    yearClick: function(e){
    	if($(e.currentTarget).hasClass("all")){
    		if($(e.currentTarget).hasClass("active")){
    			$(".celda").removeClass("active")
        	}else{
        		$(".celda").addClass("active")
        	}
    	}
    	else{
    		if($(e.currentTarget).hasClass("active")){
        		$(e.currentTarget).removeClass("active");
        	}else{
        		$(e.currentTarget).addClass("active")
        	}
    	}
    	$(".numAniosSelect").text($(".celda.active").length);
    },
    
    


});