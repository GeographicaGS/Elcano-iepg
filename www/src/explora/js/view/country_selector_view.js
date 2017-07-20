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
            if (countries[i].length == 2 || countries[i] =="XBEU"){
                this._selectedCountriesStack.push(countries[i]);
            }
            else{
                this._selectedBlocksStack.push(countries[i]);
            }
        }

        $(window).bind("resize.c_sel", _.bind(this.render, this));
    },

    events : {
        "click #save": "save",
        "click #cancel": "cancel",
        "click li[code]" : "clickCountry",
        "click .ctrl_cb li a": "clickPanelCtrl",
       // "click #ctrl_countries_plain,#ctrl_blocks_plain ": "clickCountryBlockCheckbox",
        "click .ctrl_selc" : "clickCountryBlockSel"
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();

        $(window).unbind("resize.c_sel");
    },

    render: function(){

        var col = app.getFilters().length ?  this.collection.applyGlobalFilter() :  this.collection;

        this.$el.html(this._template({
            collection :  col.toJSON(),
            ctx: app.context.data
        }));

        this.$n_selected = this.$("#n_selected");

        this.refreshCounterElements();
        //this.showHideDeselectBtn();

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

        if ($("#countries_plain li[selected]").length > 0){
            $(".ctrl_selc[data-type='country'][data-action='none']").show();
            $(".ctrl_selc[data-type='country'][data-action='all']").hide();
        }
        else{
            $(".ctrl_selc[data-type='country'][data-action='none']").hide();
            $(".ctrl_selc[data-type='country'][data-action='all']").show();
        }


        if ($("#blocks_plain li[selected]").length > 0){
            $(".ctrl_selc[data-type='block'][data-action='none']").show();
            $(".ctrl_selc[data-type='block'][data-action='all']").hide();
        }
        else{
            $(".ctrl_selc[data-type='block'][data-action='none']").hide();
            $(".ctrl_selc[data-type='block'][data-action='all']").show();
        }



        //this.$("#ctrl_blocks_plain").prop("checked",$("#blocks_plain li").not("[selected]").length == 0);

        html += " <lang>selecccionados</lang>";
        this.$n_selected.html(html);

    },

    _removeFromStack: function(stack,c){
        var index = stack.indexOf(c);
        if (index > -1) {
            stack.splice(index, 1);
        }
    },

    _addToTopStack: function(stack,c){
        if (stack.indexOf(c)==-1){
            stack.push(c);
        }

    },


    clickCountry: function(e){
        e.preventDefault();

        var $e = $(e.target).closest("li"),
            sel = $e.attr("selected");

        if (sel !== undefined && sel!="undefined"){
            $e.removeAttr("selected");
        }
        else{
            $e.attr("selected",true);
        }

        this.updateCountryOrBlockInStack($e);

        this.refreshCounterElements();
        //this.showHideDeselectBtn();
    },

    updateCountryOrBlockInStack: function($e){
        var sel = $e.attr("selected"),
            code = $e.attr("code");

        if (sel == undefined || sel=="undefined"){
            // // Unselect element
            // $e.removeAttr("selected");
            if (code.length == 2 || code =="XBEU"){
                this._removeFromStack(this._selectedCountriesStack,code);
            }
            else{
                this._removeFromStack(this._selectedBlocksStack,code);
            }
        }
        else{
            //$e.attr("selected",true);
            if (code.length == 2 || code =="XBEU"){
                this._addToTopStack(this._selectedCountriesStack,code);
            }
            else{
                this._addToTopStack(this._selectedBlocksStack,code);
            }
        }
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
    },

    clickCountryBlockSel: function(e){
        var $e = $(e.target),obj = this,
            selector = $e.attr("data-type") == "country" ? "#countries_plain li" : "#blocks_plain li",
            selected = $e.attr("data-action") == "all" ? true : false;

        this.$(selector).each(function(){
            if (selected){
                $(this).attr("selected",true);
            }
            else{
                $(this).removeAttr("selected");
            }
            obj.updateCountryOrBlockInStack($(this));
        });

        this.refreshCounterElements();
    }
});
