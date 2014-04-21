app.view.Base = Backbone.View.extend({
    el: "#base",
    // _template : _.template($('#home_template').html()),
    initialize: function() {  

        this.$tool = $("#tool");
        // Let's save the original left, this will be modified by animations in toggleTools
        this.originLeft =  this.$tool.offset().left;



        this.toolView = new app.view.tools.CountryPlugin();
        this.render();
    },
    events: {
        "click #ctrl_tool" : "toggleTools"
    },

    render: function() {
        //this.$el.html(this._template());
        this.toolView.render();
        return this;
    },
    
    toggleTools: function(e){
        var $e = $(e.target),
            ml;

        if ($e.hasClass("open")){
            // hide tool panel
            $e.removeClass("open");
            ml = this.$tool.width() * -1;

            this.$tool.find("#tool_data").width( $(window).width() -  this.originLeft - 20).height();

            this.$tool.animate({"left": ml});
        }

        else{
            $e.addClass("open");
            
            var self = this;
            this.$tool.animate({"left": this.originLeft},function(){
                console.log("complete");
                $(this).find("#tool_data").css('width', 'auto')
            });
        }
    }
});