app.view.tools.ContributionsPlugin = app.view.tools.Plugin.extend({
    _template : _.template( $('#contributions_tool_template').html() ),

    type: "contributions",
    initialize: function() {
        this.slider = new app.view.tools.common.SliderSinglePoint();
        this.countries = new app.view.tools.common.Countries({
            "variable" : false
        });
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

     /* Fetch data for the current country*/
    _fetchDataTool: function(){
        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            selection = ctx.countries.selection,
            n_fetches = 0;

        this.models = [];
        for (var i=0;i<selection.length;i++){
            this.models[i] = new app.model.tools.country({
                "id" : ctx.countries.selection[i],
                "family" : ctx.family
            });
            // Fetch model from de server
            var _this = this;
            this.model.fetch({
                success: function() {
                   n_fetches++;
                   if (n_fetches == selection.length){
                        // call to render async when all fetches will be completed
                        _this._renderToolAsync(); 
                   }
                }
            });
        }
    },
    
    _renderToolAsync: function(){
        var year =  this.getGlobalContext().data.slider[0].date.getFullYear();

        this.$el.html(this._template({
            ctx: this.getGlobalContext().data,
            model: this.model.toJSON()[year],
        }));

        this.$chart_legend = this.$(".chart_legend");

        this.$chart = this.$(".chart");

        this._drawD3Chart(year);

        this._renderChartLegend(year,"iepg");

        this._forceFetchDataTool = false;
    },

    /* Render the tool */
    renderTool: function(){
        //TOREMOVE
        console.log("Render app.view.tools.ContributionsPlugin");

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data;

        // Get the data from server if _forceFetchDataTool is set to true. If _forceFetchDataTool is set to false data is not requested to server
        if (this._forceFetchDataTool){
            this._fetchDataTool();
        }
        else{
            this._renderToolAsync();
        }
        

        this.renderMap();
    },

    renderMap: function(){
        // draw the map
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    /* 
        This method adapt the global context. Call on every render.
    */
    adaptGlobalContext: function(){

        var ctxObj = this.getGlobalContext(),
            ctx = ctxObj.data,
            latestCtxObj = this.getLatestContext(),
            latestCtx = latestCtxObj.data;

        /*
        * This tool only could have two countries selected. The options are:
        *   1) The selection is empty
        *       1.1) If The latestContext has a selection the two first (which are present in the countries list) will be choosen. 
        *       1.2) If The latestContext doesn't have a selection. Do nothing.
        *   2) The selection has elements. 
                2.1) If selection has more than two element, we cut off them.
        */
        
        if (!ctx.countries.selection.length){
            // The selection is empty
           
            if (latestCtx.selection>0 ){
                //If the latestContext has a selection all the countries (which are present in the list of countries) will be copied.

                for(var i=0,limit=0;i<latestCtx.countries.list.length && limit<2;i++){
                    // Is the selected country in context list?
                    if (ctx.countries.list.indexOf(latestCtx.countries.selection[i]) != -1){
                        ctx.countries.selection.push(latestCtx.countries.selection[i]);    
                        limit++;
                    }
                }
            }
            else{
                // Do nothing
            }
        }
        else if (ctx.countries.selection.length>2){
            // Cut off extra elements in the selection
            ctx.countries.selection = ctx.countries.selection.slice(0,2);

        }

        // This tool works with a slider composed by a single point and a reference point. 
        var firstPoint = ctxObj.getFirstSliderElement("Point"),

        // Have we a point in the context?
        if (!firstPoint){
            // search the firstPoint on the latest context
            var firstPoint = latestCtxObj.getFirstSliderElement("Point");
            if (!firstPoint){
                // set the last year
                firstPoint = {
                    "type" : "Point",
                    "date" : app.config.SLIDER[app.config.SLIDER.length-1]
                };
            }
        }

        ctx.slider = [firstPoint];

        if (!ctx.family){
            if (latestCtx.family){
                ctx.family = latestCtx.family;
            }
            else{
                ctx.family = "iepg";
            }
        }

        // Save context
        ctxObj.saveContext();

        // update the latest context
        this.copyGlobalContextToLatestContext();
    },
});