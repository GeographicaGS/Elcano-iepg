app.view.Download = Backbone.View.extend({
    _template : _.template( $('#download_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","home");
        
        this.render();

        
    },
    
    events:{
     "click .menuItem" : "menuItemClick",
     "click .siguiente" : "siguienteClick"
    },
    


    onClose: function(){
        // Remove events on close
        this.stopListening();

    },
    
    render: function() {
        
        this.$el.html(this._template());
        
        this.$(".contain").hide();
        this.$("#yearDiv").show();
        this.actual = 1;
        
        var year_view = new app.view.yearDownload();
        this.$("#yearDiv").append(year_view.render().$el);
        
        var thematic_block = new app.view.thematicBlock();
        this.$("#thematicBlock").append(thematic_block.render().$el);
        
        var country = new app.view.countryDownload();
        this.$("#countryDownload").append(country.render().$el);
        
        return this;
    },

    menuItemClick: function(e){
    	this.actual = parseInt($(e.currentTarget).attr("idMenu"));
    	$(".contain").hide();
    	
    	switch(this.actual) {
    	case 1:
    		$("#yearDiv").show();
    	    break;
    	case 2:
    		$("#thematicBlock").show();
    	    break;
    	case 3:
    		$("#countryDownload").show();
    		break;
    	}
    	
    },
    
    siguienteClick: function(){
    	if(this.actual == 3){
    		this.actual = 1;
    	}else{
    		this.actual ++;
    	}
    	$(".menuItem[idMenu=" + this.actual + "]").trigger("click");
    }


});