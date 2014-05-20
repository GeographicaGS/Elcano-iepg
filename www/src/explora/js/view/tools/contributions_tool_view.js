app.view.tools.ContributionsPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#contributions_tool_template').html() ),

    type: "contributions",
    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePoint();
        this.countries = new app.view.tools.common.Countries();
    },

    setURL: function(){
        app.router.navigate("tool/contributions",{trigger: false});
    },

    _setListeners: function(){
        app.view.tools.Plugin.prototype._setListeners.apply(this);

        this.listenTo(app.events,"slider:singlepointclick",function(year){
            var ctx = this.getGlobalContext();
            ctx.data.slider = [{
                "date" : new Date(year),
                "type" : "Point"
            }];
            ctx.saveContext();
            // The context has changed, let's store the changes in localStore
            this.getGlobalContext().saveContext();
            // Render again the tool without fetch data
            this.render(false);
        });
    },
    
    renderTool: function(){
     //TOREMOVE
        console.log("Render app.view.tools.ContributionsPlugin");
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