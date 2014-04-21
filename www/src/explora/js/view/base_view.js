app.view.Base = Backbone.View.extend({
    el: "#base",
    // _template : _.template($('#home_template').html()),
    initialize: function() {  
        this.toolView = new app.view.tools.Plugin();
        this.render();
    },
    events: {
        "click #ctrl_filter" : "showFilters"
    },

    render: function() {
        //this.$el.html(this._template());
        this.toolView.render();
        return this;
    },
    
    showFilters: function(){
        console.debug("filters");
    }
});