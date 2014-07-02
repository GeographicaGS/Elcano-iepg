app.view.tools.common.Countries = Backbone.View.extend({
    el: "#country_panel",
    _template : _.template( $('#country_bar_template').html() ),
    _variableCtrlStatus : null,
    _draggable : false,

    initialize: function(options){
        this._variableCtrlStatus = options && options.variable!=undefined && options.variable!="undefined" ? options.variable : true; 
        this._draggable = options && options.draggable!=undefined && options.draggable!="undefined" ? options.draggable : false; 
        
        var self = this;
        $(window).on('resize', function(){
            self.render();
        });
    },

    _events: {
        "click #ctrl_countries": "launchCountriesSelector",
        "click ul.country_bar a": "clickCountry",
        "click #ctrl_variables" : "clickAddVariableSelectorView",
        "click .country_bar_prev.active": "moveBarLeft",
        "click .country_bar_next.active": "moveBarRight"
    },

    _setListeners: function(){
    
    },

    bringToFront: function(){
        this.delegateEvents(this._events); 
        this._setListeners();
    },

    bringToBack: function(){
        this.undelegateEvents();
        this.stopListening();
    },

    render: function(){
        //TOREMOVE
        console.log("Render app.view.tools.common.Countries");
        this.$el.show().html(this._template({
            ctx: app.context.data,
            variableCtrl : this._variableCtrlStatus
        }));

        if (this._draggable){
            this.$("ul.country_bar li").draggable({
                revert: true,
                revertDuration: 500,
                helper: 'clone',
                appendTo: 'body',
                zIndex: 100,
                containment: 'window',
                scroll: false,
                start: function(event, ui){ //hide original when showing clone
                    $(this).addClass('dragged');
                },
                stop: function(event, ui){ //show original when hiding clone
                    $(this).removeClass('dragged');
                    //$(ui.helper).fadeOut().promise(function(){$(this).remove()});
                }
            });    
        }

        this.$btn_prev = this.$('.country_bar_prev');
        this.$btn_next = this.$('.country_bar_next');
        this.$country_bar = this.$('ul.country_bar');

        // Adjust list width
        elements = this.$country_bar.children('li');
        // Width of all other elements in this row: 465
        this.maxVisibleFlags = Math.round( (document.body.offsetWidth - 465) / elements.outerWidth(true) );
        this.maxFlagsWidth = this.maxVisibleFlags * this.$country_bar.children().outerWidth(true);

        this.$('.country_bar_container').css('max-width',this.maxFlagsWidth);
        this.$country_bar.width(elements.length * elements.outerWidth(true));
        if(elements.length > this.maxVisibleFlags){
            this.$('.country_bar_nav').addClass('active');
            this.$btn_next.addClass('active');
        }else{
            this.$('.country_bar_nav').removeClass('active');
            this.$('.country_bar_nav .active').removeClass('active');
        }
        
    },

    onClose: function(){

    },
    
    close: function(){
        if (this._variableSelectorView){
            this._variableSelectorView.close();
        }

        this.undelegateEvents();
    
        this.$el.html("").hide();
  
        if (this.onClose){
            this.onClose();
        }
    },

    launchCountriesSelector: function(){
        console.log("launchCountriesSelector");
        this.countrySelector = new app.view.CountrySelector();
       
    },

    clickCountry: function(e){
        e.preventDefault();

        var $e = $(e.target).closest("a"),
            code = $e.attr("code");

        if (code){
            app.events.trigger("countryclick",code);
        }
        
    },
    
    clickAddVariableSelectorView: function(e){
        e.preventDefault();
        if (this._variableSelectorView){
            this._variableSelectorView.close();
        }

        this._variableSelectorView = new app.view.VariableSelector(); 
    },

    moveBarLeft: function(e){
        var remainingWidth = 0 - parseInt(this.$country_bar.css('left'));
        if(remainingWidth > this.maxFlagsWidth){
            this.$country_bar.css('left','+=' + this.maxFlagsWidth);
            if(remainingWidth - this.maxFlagsWidth == 0){
                this.$btn_prev.removeClass('active');    
            }
        }else{
            this.$country_bar.css('left','+='+remainingWidth);
            this.$btn_prev.removeClass('active');
        }
        this.$btn_next.addClass('active');
    },

    moveBarRight: function(e){
        var remainingWidth = this.$country_bar.width() - this.maxFlagsWidth + parseInt(this.$country_bar.css('left'));
        if(remainingWidth > this.maxFlagsWidth){
            this.$country_bar.css('left','-=' + this.maxFlagsWidth);
            if(remainingWidth - this.maxFlagsWidth == 0){
                this.$btn_next.removeClass('active');
            }
        }else{
            this.$country_bar.css('left','-='+remainingWidth);
            this.$btn_next.removeClass('active');
        }
        this.$btn_prev.addClass('active');
    }
}); 