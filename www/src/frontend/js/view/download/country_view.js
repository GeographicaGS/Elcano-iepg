app.view.countryDownload = Backbone.View.extend({
    _template : _.template( $('#country_download_template').html() ),
    
    initialize: function() {
        
//        this.render();

        
    },
    
    events:{
    	"click .pais": "paisClick",
    	"click .todos": "todosClick",
    },
    


    onClose: function(){
        // Remove events on close
        this.stopListening();

    },
    
    render: function() {
        
        this.$el.html(this._template());
        var self = this;
        
        $.ajax({
				url : "/api/countryfilter/" + app.lang + "?eu",
				dataType: "json",
		        success: function(response) {
		        	var offset = 3;
		        	if(app.isSMDevice()){
		        		offset = 2;
		        	}

		        	var intervalo = Math.floor(response.results.length/offset);
		        	var paises = [];
		        	var aux;

		        	if(app.isXSMDevice()){
		        		$(".pais.todos").parent().addClass("col-sm-6");
		        		$(".pais.todos").parent().addClass("col-md-6");
		        	}else{
		        		$(".pais.todos").parent().addClass("col-sm-4");
		        		$(".pais.todos").parent().addClass("col-md-4");
		        	}

		        	for(var i=0; i<intervalo; i++){
		        		
		        		if(app.isXSMDevice()){
			        		paises.push("<div class='row'>" +
											// "<div class='col-sm-1 col-md-1'></div>" +
											
											"<div class='col-sm-6 col-md-6'>" +
												"<img src='/img/flags/" + response.results[i].id + ".svg" + "'>" +
												"<div class='pais' id='" + response.results[i].id + "'>" + response.results[i].name + "</div>" +
											"</div>" +
											
											"<div class='col-sm-6 col-md-6'>" +
											"<img src='/img/flags/" + response.results[i + intervalo].id + ".svg" + "'>" +
												"<div class='pais' id='" + response.results[i + intervalo].id + "'>" + response.results[i + intervalo].name + "</div>" +
											"</div>" +
											
										"</div>");
		        		}else{
		        			
		        			paises.push("<div class='row'>" +
									// "<div class='col-sm-1 col-md-1'></div>" +
									"<div class='col-sm-4 col-md-4'>" +
										"<img src='/img/flags/" + response.results[i].id + ".svg" + "'>" +
										"<div class='pais' id='" + response.results[i].id + "'>" + response.results[i].name + "</div>" +
									"</div>" +
									
									"<div class='col-sm-4 col-md-4'>" +
									"<img src='/img/flags/" + response.results[i + intervalo].id + ".svg" + "'>" +
										"<div class='pais' id='" + response.results[i + intervalo].id + "'>" + response.results[i + intervalo].name + "</div>" +
									"</div>" +
									
									"<div class='col-sm-4 col-md-4'>" +
									"<img src='/img/flags/" + response.results[i + intervalo*2].id + ".svg" + "'>" +
										"<div class='pais' id='" + response.results[i + intervalo*2].id + "'>" + response.results[i + intervalo*2].name + "</div>" +
									"</div>"+
									
								"</div>");
		        			
		        		}
		        	}
		        	
		        	if(intervalo * offset < response.results.length){
		        		paises.push("<div class='row'>" +
		        						"<div class='" + (app.isXSMDevice()? "col-sm-6 col-md-6":"col-sm-8 col-md-8") + "'></div>" +
										"<div class='" + (app.isXSMDevice()? "col-sm-6 col-md-6":"col-sm-4 col-md-4") + "'>" +
										"<img src='/img/flags/" + response.results[response.results.length-1].id + ".svg" + "'>" +
											"<div class='pais' id='" + response.results[response.results.length-1].id + "' >" + response.results[response.results.length-1].name + "</div>" +
										"</div>" +
										
									"</div>");
		        	}
		        	
		        	for(var i=0; i<paises.length; i++){
		        		self.$el.find(".container").append(paises[i]);
		        	}
		        }
		    }); 
        
        return this;
    },
    
    paisClick: function(e) {
    	if(!$(e.currentTarget).hasClass("todos")){
	    	if($(e.currentTarget).hasClass("active")){
	    		$(e.currentTarget).removeClass("active");
	    	}else{
	    		$(e.currentTarget).addClass("active")
	    	}

	    	if($(".pais.active[id]").length == $(".pais[id]").length){
				$(".pais.todos").addClass("active");
			}else{
				$(".pais.todos").removeClass("active");
			}
	    	
	    	$(".numPaises").text($(".pais.active").length);

			if($(".pais.active").length == 1){
                $(".numPaises2").html(sprintf("<lang> %d país seleccionado</lang>",$(".pais.active").length));
                
	        }else{
	            $(".numPaises2").html(sprintf("<lang> %d países seleccionados</lang>",$(".pais.active").length));
	        }

	    	if($(".counter.numAniosSelect").text() == "0" || $(".counter.numPaises").text() == "0" || $(".counter.numBloqsSelect").text() == "0"){
	    		$(".boxDonwload").removeClass("activeDownload");
	    	}else{
	    		$(".boxDonwload").addClass("activeDownload");
	    	}
	    	
	    	if($(".counter.numPaises").text() == "0"){
	    		$(".counter.numPaises").siblings("img").attr("src","/img/ELC_flecha_descarga_paso.svg")
	    	}else{
	    		$(".counter.numPaises").siblings("img").attr("src","/img/ELC_flecha_descarga_paso-selec.svg")
	    	}
    	}
    },

    todosClick: function(e){
    	if($(e.currentTarget).hasClass("active")){
    		$(".pais").removeClass("active");
    	}else{
    		$(".pais").addClass("active");
    	}
    	$(".numPaises").text($(".pais.active[id]").length);
    	if($(".pais.active").length == 1){
            $(".numPaises2").html(sprintf("<lang> %d país seleccionado</lang>",$(".pais.active").length));
		}
        else{
			$(".numPaises2").html($(".pais.active").length + "<lang> países seleccionados</lang>");
            $(".numPaises2").html(sprintf("<lang> %d países seleccionados</lang>",$(".pais.active").length));
		}
    	if($(".counter.numAniosSelect").text() == "0" || $(".counter.numPaises").text() == "0" || $(".counter.numBloqsSelect").text() == "0"){
    		$(".boxDonwload").removeClass("activeDownload");
    	}
        else{
    		$(".boxDonwload").addClass("activeDownload");
    	}
    	
    	if($(".counter.numPaises").text() == "0"){
    		$(".counter.numPaises").siblings("img").attr("src","/img/ELC_flecha_descarga_paso.svg")
    	}
        else{
    		$(".counter.numPaises").siblings("img").attr("src","/img/ELC_flecha_descarga_paso-selec.svg")
    	}
    	
    },
    

});