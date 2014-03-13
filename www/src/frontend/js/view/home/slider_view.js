app.view.Slider = Backbone.View.extend({
    _template : _.template( $('#slider_template').html() ),
    // transition time
    _msSlide : 600000,
    _timer: null,
    _idx : 0,
    _firstAnimation : true,
    initialize: function() {        
        this.collection = new app.collection.Slider();
        this.collection.set([
            {
                "slogan" : "Nueva edición 2012",
                "text" : "Índice Elcano de Presencia Global 2012",
                "img": "slide/slide1.png"
            },
            {
                "slogan" : "Nueva edición 2013",
                "text" : "Índice Elcano de Presencia Global 2013",
                "img": "slide/slide2.png"
            },
            {
                "slogan" : "Nueva edición 2014",
                "text" : "Índice Elcano de Presencia Global 2014",
                "img": "slide/slide3.png"
            }
        ]);

    },

    events:{
       "click .next" : "next",
       "click .prev" : "prev",
       "click .ctrl_images" : "goPos"
    },

    drawSlide: function(){
        // another timer running, let's stop it
        if (this._timer){
            clearTimeout(this._timer);
        }

        var $img = this.$co_imgs.find("img[data-img-idx="+this._idx+"]"),
            loaded = $img[0].complete;

        this.$ctrl_images.children().removeAttr("selected");
        this.$ctrl_images.find("li:nth-child("+(this._idx +1)+")").attr("selected",true);
        
        if (false && !loaded){
            var self = this;
            $img.load(function(){
                self._drawSlide($img);
            });
        }
        else{
            this._drawSlide($img);
        }
    },

    _drawSlide: function($img){

        var oldImage = this.$co_img.find("img");
        var newImage = $img.clone();

        this.$co_img.append(newImage);
        newImage.animate({ opacity: 1 }, 'slow',function(){
            oldImage.remove();
        });
        
        // no animation on start
        if (!this._firstAnimation){
             var  
                //calculate the number of pixels to hide the text to the right
                wrapper_text_animation_offset = this.$wrapper_text.offset().left,
                // calculate  the offset for the circle
                circle_back_animation_offset = this.$circle_back.width(),
                self = this;

            this.$wrapper_text.animate({
                right : -wrapper_text_animation_offset - 20 /*security gap */
            },500,'easeInExpo',function(){
                var m = self.collection.at(self._idx);

                self.$wrapper_text.find("h3").html(m.get("slogan"));
                self.$wrapper_text.find("h4").html(m.get("text"));

                self.$wrapper_text.animate({
                    right: 0
                },600,'easeOutExpo');
            });


            this.$circle_back.animate({
                "left": "+=" + (circle_back_animation_offset - 0 /*security gap */)+ "px" 
                
            },500,'easeInExpo',function(){
                
                self.$circle_back.animate({
                     "left": "-=" + (circle_back_animation_offset - 0 /*security gap */)+ "px" 
                },300,'easeOutExpo');
            });
        }
        else{
            this._firstAnimation = false;
        }
       

        var self = this;
        this.timer = setTimeout(function(){
            self.next();
        },this._msSlide);
    },

    next: function(){
        this._idx++;
        this._idx = (this._idx % this.collection.length);
        this.drawSlide();
    },

    prev: function(){
        if (this._idx>0){
            this._idx--;
            this._idx = (this._idx % this.collection.length);
        }
        else{
            this._idx = this.collection.length -1;
        }
        this.drawSlide();
    },
    
    goPos: function(e){
        this._idx = parseInt($(e.target).attr("data-idx"));
        this.drawSlide();
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {
        
        this.$el.html(this._template());
        this.$co_imgs = this.$("#co_imgs");
        this.$co_img = this.$(".co_img");
        this.$ctrl_images = this.$(".ctrl_images");
        this.$wrapper_text = this.$(".wrapper_text");
        this.$circle_back = this.$("#circle_back");

        var imgs = "";
        var lis = ""
        this.collection.each(function(model, index) {
            imgs += "<img src='/img/" + model.get("img") + "' data-img-idx="+ index +" style='opacity:0' />";
            lis += "<li data-idx='"+ index + "'></li>";
        });

        this.$co_imgs.html(imgs);

        this.$ctrl_images.html(lis);


        this.drawSlide();

        return this;
    }
});