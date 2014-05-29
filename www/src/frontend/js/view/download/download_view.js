app.view.Download = Backbone.View.extend({
    _template : _.template( $('#download_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","home");
        
        this.render();

        
    },
    
    events:{
    
    },
    


    onClose: function(){
        // Remove events on close
        this.stopListening();

    },
    
    render: function() {
        
        this.$el.html(this._template());
        
//        var year_view = new app.view.yearDownload();
//        this.$("#yearDiv").append(year_view.render().$el);
        
        var thematic_block = new app.view.thematicBlock();
        this.$("#thematicBlock").append(thematic_block.render().$el);
//        
        return this;
    },




});