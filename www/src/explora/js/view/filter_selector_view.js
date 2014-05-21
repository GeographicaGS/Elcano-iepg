app.view.FilterSelector = Backbone.View.extend({
    _template : _.template( $('#filter_selector_template').html() ),
    initialize: function(options){
        this.collection = new app.collection.Countries();
        
        this.listenTo(this.collection, "reset",function(){
            this.render();
        });

        this.collection.fetch({reset: true});

        this.$el.html("<div class='loading'></div>");

        $.fancybox(this.$el, app.fancyboxOpts());

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
       
        this.$el.html(this._template({
            collection :  this.collection.toJSON(),
            filters : app.getFilters()
        }));

        this.$n_selected = this.$("#n_selected");

        return this;
    },

    cancel: function(){
        $.fancybox.close();
        app.events.trigger("closepopup",this);
    },

    save: function(){
        $.fancybox.close();

        app.events.trigger("closepopup",this);
        app.events.trigger("filterschanged",$.map(this.$("ul.flag_wrapper li[selected]"),function(e) { return $(e).attr("code") }));
    },

    refreshCounterElements: function(){
        var n = this.$("ul.flag_wrapper li[selected]").length;

        var html = "";

        if (n === 0){
            html = "<lang>0 países seleccionados</lang>";
        }
        else if (n==1){
            html ="<lang>1 país seleccionado</lang>";
        }
        else{
            html = sprintf("<lang>%d países seleccionados</lang>",n);   
        }
        
        this.$n_selected.html(html);

    },


    clickCountry: function(e){
        var $e = $(e.target).closest("li"),
            sel = $e.attr("selected");

        if (sel !== undefined && sel!="undefined"){
            // Unselect element
            $e.removeAttr("selected");
        } 
        else{
            $e.attr("selected",true);
        }
        this.refreshCounterElements();
    }


    

});