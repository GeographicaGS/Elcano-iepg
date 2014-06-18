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
        "click li[code]" : "clickCountry",
        "change input#all_countries": "toggleSelection"
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
        this.refreshCounterElements();

        return this;
    },

    cancel: function(){
        $.fancybox.close();
        app.events.trigger("closepopup",this);
    },

    save: function(){
        $.fancybox.close();

        app.events.trigger("closepopup",this);
        var filters = $.map(this.$("ul.flag_wrapper li[selected]"),function(e) { return $(e).attr("code") });

        if (filters.length == this.collection.length){
            // all selected is the same as no filters
            filters = [];
        }
        app.events.trigger("filterschanged",filters);
    },

    refreshCounterElements: function(){
        var n = this.$("ul.flag_wrapper li[code]:not([selected])").length;

        var html = "";

        if (n === 0 || n== this.collection.length) {
            html = "<lang>Ningún páis filtrado</lang>";
        }
        else if (n===1){
            html ="<lang>1 país filtrado</lang>";
        }
        else{
            html = sprintf("<lang>%d países filtrados</lang>",n);   
        }
        
        this.$n_selected.html(html);

    },

    clickCountry: function(e){
        var $e = $(e.target).closest("li"),
            sel = $e.attr("selected"),
            n = this.$("ul.flag_wrapper li[code][selected]").length,
            $toggle = this.$("input#all_countries");

        if (sel !== undefined && sel!="undefined"){
            // Unselect element
            $e.removeAttr("selected");
        } 
        else{
            $e.attr("selected",true);
        }

        if (n != this.collection.length){
            $toggle.attr("checked",true);
        }
        else{
            $toggle.removeAttr("checked");
        }

        this.refreshCounterElements();
    },

    toggleSelection: function(e){
        var $e = $(e.target);

        if (!$e.is(":checked")){
            // Unselect element
            this.$("ul.flag_wrapper li").removeAttr("selected");
            //this.$("ul.flag_wrapper").removeAttr("disable");
        }
        else{
            this.$("ul.flag_wrapper li").attr("selected",true);
            //this.$("ul.flag_wrapper").removeAttr("disable");
        }

        this.refreshCounterElements();
    }

});