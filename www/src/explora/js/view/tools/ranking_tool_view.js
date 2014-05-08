app.view.tools.RankingPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#ranking_tool_template').html() ),

    type: "ranking",

    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePoint();
        this.countries = new app.view.tools.common.Countries();
    },

    _events: {
       
    },

    _setListeners: function(){
        //app.view.tools.Plugin.prototype._setListeners.apply(this);

        this.listenTo(app.events,"countryclick",function(id_country){
            //TOREMOVE
            console.log("countryclick at app.view.tools.CountryPlugin");

            var ctx = this.getGlobalContext();
            ctx.data.countries.selection = [id_country];
            ctx.saveContext();
            // The context has changed, let's store the changes in localStore
            this.getGlobalContext().saveContext();
            // Render again the tool with the new context
            this._forceFetchDataTool = true;
            this.render();
        });

    },

    /* Fetch data for the current country*/
    _fetchDataTool: function(){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        this.model = new app.model.tools.ranking({
            "id" : ctx.countries.selection[0],
            "year" : ctx.slider[0].date.getFullYear(),
            "variable" : ctx.variables[0],
            "family" : "iepg"
        });

        // Fetch model from de server
        var self = this;
        this.model.fetch({
            success: function() {
               self._renderToolAsync();
            }
        });
    },

     _renderToolAsync: function(){
        var year =  this.getGlobalContext().data.slider[0].date.getFullYear();

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
            model: this.model.toJSON(),
        }));

        // this.$chart = this.$(".chart");

        // this._drawD3Chart(year);

        this._forceFetchDataTool = false;
    },

    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.RankingPlugin");

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        if (!ctx.countries.selection.length){
            // it happens when remove the latest element from the filter
            this.$el.html(this._template({
                ctx: this.getGlobalContext().data,
                model: null,
            }));
        }
        else{
            // Get the data from server if _forceFetchDataTool is set to true. If _forceFetchDataTool is set to false data is not requested to server
            if (this._forceFetchDataTool){
                this._fetchDataTool();
            }
            else{
                this._renderToolAsync();
            }
        }

    },

    setURL: function(){
        // This method transforms the current context of the tool in a valid URL.
        //country/:id_country/:id_variable/:year
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            countries = ctx.countries.list;
            country = ctx.countries.selection[0],
            variable = ctx.variables[0],
            year = ctx.slider[0].date.getFullYear();

        app.router.navigate("ranking/" + variable + "/" + year + "/" + countries.join(",") + "/" + country ,{trigger: false});
    },

    renderMap: function(){
        // draw the map
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    }
});