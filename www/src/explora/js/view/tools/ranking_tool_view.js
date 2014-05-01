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
        console.log("Render app.view.tools.RankingPlugin");
        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
        }));

    },

    setURL: function(){
        // This method transforms the current context of the tool in a valid URL.
        //country/:id_country/:id_variable/:year
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            country = ctx.countries.selection[0],
            variable = ctx.variables[0],
            year = ctx.slider[0].date.getFullYear();

        //app.router.navigate("ranking/" + country + "/" + variable + "/" + year, {trigger: false});
        app.router.navigate("tool/ranking",{trigger: false});
    },

    renderMap: function(){
        // draw the map
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    }
});