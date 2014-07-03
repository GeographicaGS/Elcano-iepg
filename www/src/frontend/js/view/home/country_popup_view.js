app.view.CountryPopup = Backbone.View.extend({
    _template : _.template( $('#home_popup_country_template').html() ),
    
    initialize: function(options) {
        
        this.parent = options.parent;

        this.collection = new app.collection.Countries({},{
            "year": 2012
        });

        this.listenTo(this.collection,"reset",this.render);

        this.collection.fetch({"reset": true});
    },

    events: {
        "click .level_1 li": "selectContinent",
        "click .level_2 .goback" : "goParent",
        "click .level_2 [data-l2]" : "selectCountry",
        "click h6.global": "goIEPG",
        "click h6.eu": "goIEPE",

    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {
        this.$el.html(this._template({
           collection : this.collection.toJSON(),
           country: this.parent.getCountry(),
        }));
        this.$level_1 = this.$(".level_1");
        return this;
    },

    selectContinent: function(e){
        var $e = $(e.target),
            l1 = $e.closest("[data-l1]").attr("data-l1"),
            $l2 = this.$(".level_2[data-l1='" + l1 +"']");

        this.$level_1.hide();
        $l2.show();
    },

    goParent: function(){
        this.$(".level_2").hide();
        this.$level_1.show();
    },

    selectCountry: function(e){
        var $e = $(e.target),
            $l2 = $e.closest("[data-l2]"),
            code = $l2.attr("data-l2"),
            name = $l2.attr("data-name");
    
        this.$("[data-l2]").removeAttr("selected");
        $l2.attr("selected",true);

        this.parent.selectCountry(code,name);

    },

    goIEPG: function(e){
        var $e = $(e.target);
        $e.siblings("h6").removeAttr("selected");
        $e.attr("selected",true);
        this.goParent();
    },

    goIEPE: function(e){
        var $e = $(e.target);
        $e.siblings("h6").removeAttr("selected");
        $e.attr("selected",true);
        this.goParent();
    }


});