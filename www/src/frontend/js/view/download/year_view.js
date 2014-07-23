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
        $(app.config.YEARS).each(function() {
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


        if($(".celda.active").length == "1"){
            $(".numAniosSelect2").html("<lang>" + $(".celda.active").length + " año seleccionado</lang>");
        }else{
            $(".numAniosSelect2").html($(".celda.active").length + "<lang> años seleccionados</lang>");
        }

    	if($(".counter.numAniosSelect").text() == "0" || $(".counter.numPaises").text() == "0" || $(".counter.numBloqsSelect").text() == "0"){
    		$(".boxDonwload").removeClass("activeDownload");
    	}else{
    		$(".boxDonwload").addClass("activeDownload");
    	}
    	
    	if($(".counter.numAniosSelect").text() == "0"){
    		$(".counter.numAniosSelect").siblings("img").attr("src","/img/ELC_flecha_descarga_paso.svg")
    	}else{
    		$(".counter.numAniosSelect").siblings("img").attr("src","/img/ELC_flecha_descarga_paso-selec.svg")
    	}
    	
    },
    
    


});