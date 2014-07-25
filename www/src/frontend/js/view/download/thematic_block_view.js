app.view.thematicBlock = Backbone.View.extend({
    _template : _.template( $('#thematic_block_template').html() ),
    
    initialize: function() {

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

        self.renderFamily("iepg");
        self.renderFamily("iepe");

        return this;
    },

    renderFamily: function(f){
        var html = "",
            self = this;

        _.each(app.view.tools.utils.variablesTree().data.children,function(d){
            if (f=="iepe" && d.key=="military_global") return;

            html += self.getHtmlThematic(d.name,d.key, "level2");

            _.each(d.children,function(c) {
                html += self.getHtmlThematic(c.name, c.key, "level3");
            });
        });

        this.$("#cod_variables_"+f).html(html);
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
    		}
            else{
    			$(".tematica2").removeClass("active");
                $(".tematica2").siblings("div").removeClass("iconVariableActive");
    		}
    	}
        else{
    		if($(e.currentTarget).hasClass("tematica")){
    			$(".tematica").addClass("active");
                $(".tematica").siblings("div").addClass("iconVariableActive");
    		}
            else{
    			$(".tematica2").addClass("active");
                $(".tematica2").siblings("div").addClass("iconVariableActive");
    		}
    	}
    	var total = $(".tematica.active[key]").length + $(".tematica2.active[key]").length;
        $(".numBloqsSelect").text(total);

        if(total == 1){
            $(".numBloqsSelect2").html(sprintf("<lang> %d variable seleccionada</lang>",total));
        }
        else{
            $(".numBloqsSelect2").html(sprintf("<lang> %d variables seleccionadas</lang>",total));
        }

    	if($(".counter.numAniosSelect").text() == "0" || $(".counter.numPaises").text() == "0" || $(".counter.numBloqsSelect").text() == "0"){
    		$(".boxDonwload").removeClass("activeDownload");
    	}
        else{
    		$(".boxDonwload").addClass("activeDownload");
    	}
    	
    	if($(".counter.numBloqsSelect").text() == "0"){
    		$(".counter.numBloqsSelect").siblings("img").attr("src","/img/ELC_flecha_descarga_paso.svg")
    	}
        else{
    		$(".counter.numBloqsSelect").siblings("img").attr("src","/img/ELC_flecha_descarga_paso-selec.svg")
    	}
    	
    },
    
    getHtmlThematic: function(name,key, level) {
    	var html = "<div class='row " + level + "'>" +
					"<div class='col-sm-6 col-md-6'>"+
						"<div class='iconVariable' data-variable='" + name + "'></div>"+
						"<div class='tematica' key='" + key + "'>" + app.variableToString(name) + "</div>"+
					"</div>";
        html += "</div>";

        return html;
    	
    },

});