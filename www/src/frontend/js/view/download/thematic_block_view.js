app.view.thematicBlock = Backbone.View.extend({
    _template : _.template( $('#thematic_block_template').html() ),
    
    initialize: function() {
        
        this.render();

        
    },
    
    events:{
    	"click .tematica": "tematicaClick",
    	"click .tematica2": "tematicaClick",
    	
    },
    


    onClose: function(){
        // Remove events on close
        this.stopListening();

    },
    
    render: function() {
        
        this.$el.html(this._template());
        
        var self = this;
        
        this.$el.append(this.getHtmlThematic("iepg","iepe" , ""));
        
        $(app.view.tools.utils.variablesTree().data.children).each(function() {
        	self.$el.append(self.getHtmlThematic(this.name,this.name , "level2"));
        	$(this.children).each(function() {
        		self.$el.append(self.getHtmlThematic(this.name,this.name , "level3"));
        	});
        });
        
        return this;
    },
    
    tematicaClick: function(e) {
    	if($(e.currentTarget).hasClass("active")){
    		$(e.currentTarget).removeClass("active");
    		$(e.currentTarget).siblings("img").removeClass("iconVariableActive");
    	}else{
    		$(e.currentTarget).addClass("active")
    		$(e.currentTarget).siblings("img").addClass("iconVariableActive");
    	}
    	$(".numBloqsSelect").text($(".tematica.active").length + $(".tematica2.active").length);
    },
    
    getHtmlThematic: function(name1, name2, level) {
    	return "<div class='row " + level + "'>" +
					"<div class='col-sm-5 col-md-5' style='margin-left: 8.31%;'>"+
						"<img class='iconVariable' data-variable='" + name1 + "'>"+
						"<div class='tematica'>" + app.variableToString(name1) + "</div>"+
					"</div>"+
					"<div class='col-sm-5 col-md-5'>"+
						"<img class='iconVariable pl' data-variable='" + name2 + "'>"+
						"<div class='tematica2'>" + app.variableToString(name2) + "</div>"+
					"</div>"+
				"</div>";
    	
    },

});