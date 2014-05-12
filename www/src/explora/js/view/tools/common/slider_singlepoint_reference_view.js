app.view.tools.common.SliderSinglePointReference = app.view.tools.common.Slider.extend({
    _template : _.template( $('#slider_singlepoint_reference_template').html() ),

    initialize: function(options){
        app.view.tools.common.Slider.prototype.initialize.apply(this,[options]);
    },

    _events: {
        "click a.point" : "changeYearClick"
    },
    render: function(){
        console.log("Render app.view.tools.common.SliderSinglePointReference");

        this.$el.html(this._template({
            ctx: app.context.data,
        }));

        this.$el.show();

        this.$ul = this.$("ul.slider");

        var _this = this;

        this.$(".draggable").draggable({ 
            axis: "x" , 
            containment: "parent",
            stop: function( event, ui ) {
                var ulwidth = _this.$ul.width(),
                    pos = ui.position.left,
                    perc_pos = (100* pos) / ulwidth,
                    mindist = ulwidth;

                // let's find the closest element 
                var $closest = null;

                _this.$ul.children("[base]").each(function(idx, el){

                    var dist = Math.abs($(el).position().left -pos);
                    if (dist < mindist){
                        mindist = dist;
                        $closest = $(el);
                    }
                });

                // let's move the element to the closest
                $(ui.helper).find(".ornament").html($closest.find(".ornament").html() );
                $(ui.helper).animate({
                    left: $closest.position().left
                }, 200,function(){
                    // let's fire the year change event
                    var year = $closest.find("a.point").attr("year"),
                    ref = $(ui.helper).is("[ref]");
                    _this.changeYear(year,ref);
                });

                

            }
        });
        
    },

    changeYearClick: function(e){
        e.preventDefault();
        
        var $el = $(e.target),
            year = $el.attr("year");

        this.changeYear(year,false)

    },

    changeYear: function(year,ref){
        if (!ref){
            // Change the date, let's fire this event
            app.events.trigger("slider:singlepointclick",year);
        }
        else{
            app.events.trigger("slider:singlepointreferenceclick",year);
        }

    }

});
