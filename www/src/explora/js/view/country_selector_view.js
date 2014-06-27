app.view.CountrySelector = Backbone.View.extend({
    _template : _.template( $('#country_selector_template').html() ),
    // Stack to stored the selection stack
    _selectedCountriesStack : null,
    initialize: function(options){
        this.collection = new app.collection.Countries();
        
        this.listenTo(this.collection, "reset",function(){
            this.render();
        });

        this.collection.fetch({reset: true});

        this.$el.html("<div class='loading'></div>");

        $.fancybox(this.$el, app.fancyboxOpts());

        this._selectedCountriesStack = [];
        this._selectedBlocksStack = [];

        var countries =  app.context.data.countries.list;
        // Add tools to the stack.
        for (var i=0;i<countries.length;i++){
            if (countries[i].length == 2){
                this._selectedCountriesStack.push(countries[i]);    
            }
            else{
                this._selectedBlocksStack.push(countries[i]);       
            }
        }

        var self = this;
        $(window).on('resize', function(){
            self.render();
        });
    },

    events : {
        "click #save": "save",
        "click #cancel": "cancel",
        "click li[code]" : "clickCountry",
        "click .ctrl_cb li a": "clickPanelCtrl"
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
            ctx: app.context.data
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
        ctx.data.countries.list = _.union(this._selectedCountriesStack,this._selectedBlocksStack);
        ctx.removeInvalidSelected();

        app.events.trigger("closepopup",this);
        app.events.trigger("contextchange:countries");
    },

    refreshCounterElements: function(){
        var nc = this._selectedCountriesStack.length,
            nb = this._selectedBlocksStack.length;

        var html = "";

      
        if (nc==1){
            html ="<lang>1 país </lang>";
        }
        else{
            html = sprintf("<lang> %d países</lang>",nc);   
        }

        html += " <lang>y</lang> ";

        if (nb==1){
            html +="<lang>1 bloque</lang>";
        }
        else{
            html += sprintf("<lang> %d bloques</lang>",nb);   
        }

        html += "<lang> selecccionados</lang>";       
        this.$n_selected.html(html);

    },

    _removeFromStack: function(stack,c){
        var index = stack.indexOf(c);
        if (index > -1) {
            stack.splice(index, 1);
        }
    },

    _addToTopStack: function(stack,c){
        stack.push(c);
    },


    clickCountry: function(e){
        e.preventDefault();

        var $e = $(e.target).closest("li"),
            sel = $e.attr("selected"),
            code = $e.attr("code");

        if (sel !== undefined && sel!="undefined"){
            // Unselect element
            $e.removeAttr("selected");
            if (code.length == 2){
                this._removeFromStack(this._selectedCountriesStack,code);    
            }
            else{
                this._removeFromStack(this._selectedBlocksStack,code);
            }
            

        } 
        else{
            $e.attr("selected",true);
            if (code.length == 2){
                this._addToTopStack(this._selectedCountriesStack,code);    
            }
            else{
                this._addToTopStack(this._selectedBlocksStack,code);
            }
        }
        
        this.refreshCounterElements();
    },

    clickPanelCtrl: function(e){

        e.preventDefault();

        var $e = $(e.target),
            $target = this.$("#"+ $e.attr("data-rel"));

        this.$(".body > div").fadeOut(300, function(){
            $target.show();
        });

        this.$("ul.ctrl_cb li").removeAttr("selected");
        $e.closest("li").attr("selected",true);
       
        
        
    }


    

});