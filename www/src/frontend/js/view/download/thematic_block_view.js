app.view.thematicBlock = Backbone.View.extend({
    _template : _.template( $('#thematic_block_template').html() ),
    
    initialize: function() {
        
//        this.render();

        
    },
    
    events:{
    	"click .tematica": "tematicaClick",
    	"click .tematica2": "tematicaClick",
    	"click .todos": "todosClick",
    	
    },
    


    onClose: function(){
        // Remove events on close
        this.stopListening();

    },
    
    render: function() {
        
        this.$el.html(this._template());
        
        var self = this;
        
        this.$el.find(".container").append(this.getHtmlThematic("iepg","iepe", "iepg","iepe", ""));
        
        $(app.view.tools.utils.variablesTree().data.children).each(function() {
        	self.$el.find(".container").append(self.getHtmlThematic(this.name,this.name , this.key, this.key, "level2"));
        	$(this.children).each(function() {
        		self.$el.find(".container").append(self.getHtmlThematic(this.name,this.name, this.key, this.key, "level3"));
        	});
        });
        
        return this;
    },
    
    tematicaClick: function(e) {
    	if($(e.currentTarget).hasClass("active")){
    		$(e.currentTarget).removeClass("active");
    		$(e.currentTarget).siblings("div").removeClass("iconVariableActive");
    	}else{
    		$(e.currentTarget).addClass("active")
    		$(e.currentTarget).siblings("div").addClass("iconVariableActive");
    	}
    	
    	if($(e.currentTarget).hasClass("tematica")){
			if($(".tematica.active[key]").length == $(".tematica[key]").length){
				$(".tematica.todos").addClass("active");
			}else{
				$(".tematica.todos").removeClass("active");
			}
		}else{
			if($(".tematica2.active[key]").length == $(".tematica2[key]").length){
				$(".tematica2.todos").addClass("active");
			}else{
				$(".tematica2.todos").removeClass("active");
			}
		}
    	
        var total = $(".tematica.active[key]").length + $(".tematica2.active[key]").length;
    	$(".numBloqsSelect").text(total);

        if(total == 1){
            $(".numBloqsSelect2").html(sprintf("<lang> %d variable seleccionada</lang>",total));
        }else{
            $(".numBloqsSelect2").html(sprintf("<lang> %d variables seleccionadas</lang>",total));
        }

    	if($(".counter.numAniosSelect").text() == "0" || $(".counter.numPaises").text() == "0" || $(".counter.numBloqsSelect").text() == "0"){
    		$(".boxDonwload").removeClass("activeDownload");
    	}else{
    		$(".boxDonwload").addClass("activeDownload");
    	}
    	
    	if($(".counter.numBloqsSelect").text() == "0"){
    		$(".counter.numBloqsSelect").siblings("img").attr("src","/img/ELC_flecha_descarga_paso.svg")
    	}else{
    		$(".counter.numBloqsSelect").siblings("img").attr("src","/img/ELC_flecha_descarga_paso-selec.svg")
    	}
    	
    },
    
    todosClick: function(e){
    	if($(e.currentTarget).hasClass("active")){
    		if($(e.currentTarget).hasClass("tematica")){
    			$(".tematica").removeClass("active");
                $(".tematica").siblings("div").removeClass("iconVariableActive");
    		}else{
    			$(".tematica2").removeClass("active");
                $(".tematica2").siblings("div").removeClass("iconVariableActive");
    		}
    	}else{
    		if($(e.currentTarget).hasClass("tematica")){
    			$(".tematica").addClass("active");
                $(".tematica").siblings("div").addClass("iconVariableActive");
    		}else{
    			$(".tematica2").addClass("active");
                $(".tematica2").siblings("div").addClass("iconVariableActive");
    		}
    	}
    	var total = $(".tematica.active[key]").length + $(".tematica2.active[key]").length;
        $(".numBloqsSelect").text(total);

        if(total == 1){
            $(".numBloqsSelect2").html(sprintf("<lang> %d variable seleccionada</lang>",total));
        }else{
            $(".numBloqsSelect2").html(sprintf("<lang> %d variables seleccionadas</lang>",total));
        }

    	if($(".counter.numAniosSelect").text() == "0" || $(".counter.numPaises").text() == "0" || $(".counter.numBloqsSelect").text() == "0"){
    		$(".boxDonwload").removeClass("activeDownload");
    	}else{
    		$(".boxDonwload").addClass("activeDownload");
    	}
    	
    	if($(".counter.numBloqsSelect").text() == "0"){
    		$(".counter.numBloqsSelect").siblings("img").attr("src","/img/ELC_flecha_descarga_paso.svg")
    	}else{
    		$(".counter.numBloqsSelect").siblings("img").attr("src","/img/ELC_flecha_descarga_paso-selec.svg")
    	}
    	
    },
    
    getHtmlThematic: function(name1, name2, key1, key2, level) {
    	return "<div class='row " + level + "'>" +
					"<div class='col-sm-6 col-md-6'>"+
						"<div class='iconVariable' data-variable='" + name1 + "'></div>"+
						"<div class='tematica' key='" + key1 + "'>" + app.variableToString(name1) + "</div>"+
					"</div>"+
					"<div class='col-sm-6 col-md-6' style='padding-left: " + (level == "level2" ? '30' : (level == "level3" ? '50':'10')) + "px;'>"+
						"<div class='iconVariable pl ml' data-variable='" + name2 + "'></div>"+
						"<div class='tematica2' key='" + key2 + "'>" + app.variableToString(name2) + "</div>"+
					"</div>"+
				"</div>";
    	
    },

});