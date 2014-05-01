app.view.tools.common.SliderSinglePoint = app.view.tools.common.Slider.extend({
    _template : _.template( $('#slider_singlepoint_template').html() ),

    initialize: function(options){
        app.view.tools.common.Slider.prototype.initialize.apply(this,[options]);
    },

    _events: {
        "click a.point" : "changeYear"
    },
    render: function(){
        console.log("Render app.view.tools.common.SliderSinglePoint");

        this.$el.html(this._template({
            ctx: app.context.data,
        }));

        this.$el.show();
        
    },

    changeYear: function(e){
        e.preventDefault();
        
        var $el = $(e.target),
            year = $el.attr("year");

        // Change the date, let's fire this event
        app.events.trigger("slider:singlepointclick",year);

    }

});
