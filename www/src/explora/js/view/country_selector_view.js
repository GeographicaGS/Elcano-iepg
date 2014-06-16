app.view.CountrySelector = Backbone.View.extend({
    _template : _.template( $('#country_selector_template').html() ),
    // Stack to stored the selection stack
    _selectedStack : null,
    initialize: function(options){
        this.collection = new app.collection.Countries();
        
        this.listenTo(this.collection, "reset",function(){
            this.render();
        });

        this.collection.fetch({reset: true});

        this.$el.html("<div class='loading'></div>");

        $.fancybox(this.$el, app.fancyboxOpts());

        this._selectedStack = [];

        var countries =  app.context.data.countries.list;
        // Add tools to the stack.
        for (var i=0;i<countries.length;i++){
            this._selectedStack.push(countries[i]);
        }

        var self = this;
        $(window).on('resize', function(){
            self.render();
        });
    },

    events : {
        "click #save": "save",
        "click #cancel": "cancel",
        "click li[code]" : "clickCountry"
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    
        $(window).off('resize', this.repositionBoards)
    },

    render: function(){

        var col = app.getFilters().length ?  this.collection.applyGlobalFilter() :  this.collection;

        this.$el.html(this._template({
            collection :  col.toJSON(),
            ctx: app.context.data,
            n_selected : this._selectedStack.length,
        }));

        this.$n_selected = this.$("#n_selected");

        this.refreshCounterElements();

        return this;
    },

    cancel: function(){
        $.fancybox.close();
        app.events.trigger("closepopup",this);
    },

    save: function(){
        $.fancybox.close();
        
        var ctx =  app.context;
        ctx.data.countries.list = this._selectedStack;
        ctx.removeInvalidSelected();

        app.events.trigger("closepopup",this);
        app.events.trigger("contextchange:countries");
    },

    refreshCounterElements: function(){
        var n = this._selectedStack.length;

        var html = "";

        if (n === 0){
            html = "<lang>0 países seleccionados</lang>";
        }
        else if (n==1){
            html ="<lang>1 país seleccionado</lang>";
        }
        else{
            html = sprintf("<lang> %d países seleccionados</lang>",n);   
        }
        
        this.$n_selected.html(html);

    },

    _removeCountryFromStack: function(c){
        var index = this._selectedStack.indexOf(c);
        if (index > -1) {
            this._selectedStack.splice(index, 1);
        }
    },

    _addCountryToTopStack: function(c){
        this._selectedStack.push(c);
    },


    clickCountry: function(e){
        var $e = $(e.target).closest("li"),
            sel = $e.attr("selected"),
            code = $e.attr("code");

        if (sel !== undefined && sel!="undefined"){
            // Unselect element
            $e.removeAttr("selected");
            this._removeCountryFromStack(code);

        } 
        else{
            $e.attr("selected",true);
            this._addCountryToTopStack(code);
        }
        this.refreshCounterElements();
    }


    

});