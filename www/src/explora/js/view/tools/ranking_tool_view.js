app.view.tools.RankingPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#ranking_tool_template').html() ),

    type: "ranking",
    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePoint({
            "plugin": this
        });

        this.countries = new app.view.tools.common.Countries({
            "plugin": this
        });
    },

    _events: {
       
    },

    renderTool: function(){
     //TOREMOVE
        console.log("Render app.view.tools.RankingPlugin");
        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
        }));
    },

    renderMap: function(){
        // draw the map
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    }
});