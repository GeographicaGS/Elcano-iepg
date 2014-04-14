app.view.tools.common.SliderSinglePoint = app.view.tools.common.Slider.extend({
    render: function(){
        app.view.tools.common.Slider.prototype.render.apply(this);
    },

    events: {
        "click #ctrl_filter" : "showFilters"
    },

    showFilters: function(){
        console.debug("filters");
    }
});
