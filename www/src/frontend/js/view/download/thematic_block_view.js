app.view.thematicBlock = Backbone.View.extend({
    _template : _.template( $('#thematic_block_template').html() ),
    
    initialize: function() {

    },
    
    events:{
        "click .todos": "todosClick",
    	"click .tematica[key],.tematica2[key]": "tematicaClick"
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
            if (f=="iepe" && d.key=="military_global" ) return;

            html += self.getHtmlThematic(d.name,d.key, "level2",f);

            _.each(d.children,function(c) {
                if (f=="iepe" && c.key=="cooperation") return;
                html += self.getHtmlThematic(c.name, c.key, "level3",f);
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
    	
    	this._refreshCounters();
    },

    _refreshCounters: function(){

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
        var $el = $(e.target);

        $el = $el.closest(".todos");

        var f = $el.attr("family"),
            themClass = f=="iepg" ? "tematica" : "tematica2";
    	if($el.hasClass("active")){
            $el.removeClass("active");
            $("."+themClass + "[family='"+f+"']").removeClass("active");
            $(".iconVariable[family='"+f+"']").removeClass("iconVariableActive");
    	}
        else{
            $el.addClass("active");
            $("."+themClass + "[family='"+f+"']").addClass("active");
            $(".iconVariable[family='"+f+"']").addClass("iconVariableActive");
    	}

    	this._refreshCounters();
    	
    },
    
    getHtmlThematic: function(name,key, level,family) {
    	
        var themClass = family=="iepg" ? "tematica" : "tematica2",
            html = "<div class='" + level + "'>" +
                    "<div>"+
                        "<div class='iconVariable' data-variable='" + name + "' family='"+ family + "'></div>"+
                        "<div class='" + themClass + "' key='" + key + "' family='"+ family + "'>" + app.variableToString(name) + "</div>"+
                    "</div>" +
                "</div>";

        return html;
    	
    },

});