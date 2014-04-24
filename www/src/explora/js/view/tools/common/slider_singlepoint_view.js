app.view.tools.common.SliderSinglePoint = app.view.tools.common.Slider.extend({
    _template : _.template( $('#slider_singlepoint_template').html() ),

    initialize: function(options){
        app.view.tools.common.Slider.prototype.initialize.apply(this,[options]);
    },

    render: function(){
        // We do nothing with the local context, all is done with the global context.
        // We'll do it in the future
        this.$el.html(this._template({
            ctx: this.plugin.getGlobalContext().data,
        }));
        
    },

    changeCurrent: function(){
        // Change the date, let's re-render the tool.
        this.plugin.refreshTool();

    }

});
