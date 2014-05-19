app.view.highlights.FormView = Backbone.View.extend({
    _template : _.template( $('#highlights_form_template').html() ),
    _templateImage : _.template( $('#highlights_form_image_template').html() ),
    _maxImageSize : 8, // 8MB
    _imageWidth : 1920,
    _imageMinHeight : 480,
    _saveRequest : false,

    initialize: function(options) {
        app.events.trigger("menu","highlights");
        
        if (!options || !options.id){
            this.model = new app.model.Highlight();
            this._initialize(); 
        }
        else{
            var self = this;
            this.model = new app.model.Highlight({"id" : options.id});
            this.model.fetch({
                success: function(){
                    self._initialize();
                }
            });
        }
    },
    
    _initialize: function(){
        this.listenTo(this.model,"change:image_hash_en",function(){
            this.renderImage("en","/tmp");
        });
        this.listenTo(this.model,"change:image_hash_es",function(){
            this.renderImage("es","/tmp");
        });
        
        Backbone.Validation.bind(this);
        this.render();  
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    events: {
        "click .upload": function(e){
            e.preventDefault();
            var $e = $(e.target),
                $file = $e.siblings("input[type='file']");
            $file.trigger("click");
        },
        "change input[type='file']" : "uploadIMG",
        "click .save_button": "save",
        "blur input[name],textarea[name]": "validate",
        "click  .cancel" : function(){
            app.router.navigate("highlights",{trigger: true});
        },
        "click .btnDeleteAjunto " : "deleteIMG"
    },
    
    validate : function(e){
        if (!this._saveRequest){
            return;
        }

        var $e = $(e.target),
            name = $e.attr("name");

        this.model.set(name,$.trim($e.val()));
        this.model.isValid(true);    
        
    },

    save: function(){
        this._saveRequest = true;

        var data = {
            "title_en" : app.input(this.$("input[name='title_en']").val()),
            "title_es" : app.input(this.$("input[name='title_es']").val()),
            "text_en" : app.input(this.$("input[name='text_en']").val()),
            "text_es" : app.input(this.$("input[name='text_es']").val()),
            "credit_img_en" : app.input(this.$("input[name='credit_img_en']").val()),
            "credit_img_es" : app.input(this.$("input[name='credit_img_es']").val()),
            "link_en" : app.input(this.$("input[name='link_en']").val()),
            "link_es" : app.input(this.$("input[name='link_es']").val())
        };

        this.model.set(data);
         
        if (this.model.isValid(true)){
            // Save on server
            this.model.save(null,{
                saved: true,
                success: function(model){
                    app.router.navigate("highlights/" + model.get("id"),{trigger: true});
                }
            });
        }
        else{
            app.scrollTop();
        }
    },
    render: function() {

        this.$el.html(this._template({
            model: this.model.toJSON()
        }));

        this.renderImage("es","/media");
        this.renderImage("en","/media");

        return this;
    },

    renderImage: function (lang,imageFolder){
        this.$("#co_image_"+lang).html(this._templateImage({
            model: this.model.toJSON(),
            lang: lang,
            imageFolder : imageFolder
        }));
    },

    uploadIMG: function(e){
        var $file = $(e.target),
            lang  = $file.closest("[lang]").attr("lang");

        if ($file.val()== null || $file.val()==undefined || $file.val()=="undefined" || $file.val()=="" ){
            return;
        }

        var file = $file[0].files[0],
            name = file.name,
            /* Size in bytes */
            size = file.size,
            type = file.type,
            $unot =  this.$("#upload_notification_"+lang);
                    
        if (["image/jpeg"].indexOf(type) == -1 ){
            $unot.html("<lang>Suba una image JPG</lang>.");
            setTimeout(function(){
                $unot.html("");
            },8000);

            return;
        }
  
        // Max allow 8 MB
        if (size/(1024*1024) > this._maxImageSize){
            $unot.html("<lang>El fichero no puede ser mayor de </lang>" + " "+ this._maxImageSize +" MB.");
            setTimeout(function(){
                $unot.html("");
            },8000);

            return;
        }

        // Check image dimension
        var fr = new FileReader,
            self = this;

        fr.onload = function() { // file is loaded
            var img = new Image;

            img.onload = function() {
                var width = img.width,
                    height = img.height;

                if (self._imageWidth == width && self._imageMinHeight<=height){
                    self._upload(lang,name);
                }
                else{
                    $unot.html("<lang>Tamaño de imagen incorrecto, el ancho tiene que ser de 1920px y el alto mayor que 480px</lang>");
                    setTimeout(function(){
                        $unot.html("");
                    },6000);
                }
            };

            img.src = fr.result; // is the data URL because called with readAsDataURL
        };

        fr.readAsDataURL(file); 
    },

    _upload: function(lang,name){
        var $uf = this.$("form[lang="+lang+"]"),
            $progress = $uf.find("progress"),
            formData = new FormData($uf[0]),
            $button = $uf.find("button.upload");

        $progress.show();
        $button.hide();

        var self = this;
        
        $.ajax({
            url: app.config.API_URL  + "/highlight/upload_img",
            type: 'POST',
            dataType: "json",
            xhr: function() { // custom xhr
                var myXhr = $.ajaxSettings.xhr();
                if(myXhr.upload){ // check if upload property exists
                    myXhr.upload.addEventListener('progress',function(e){
                        if(e.lengthComputable){
                            $progress.attr({value:e.loaded,max:e.total});
                        }
                    }, false); // for handling the progress of the upload
                }
                return myXhr;
            },
            success: function(json){
                $progress.hide();
                $button.show();
                
                self.model.set("image_name_"+lang,name);
                self.model.set("image_hash_"+lang,json.filename);
                
            },   
            error: function(){
                $progress.hide();
            },
            // Form data
            data: formData,
            //Options to tell JQuery not to process data or worry about content-type
            cache: false,
            contentType: false,
            processData: false
        });
    },

    deleteIMG: function (e){
        e.preventDefault();
        var $e = $(e.target),
            lang  = $e.closest("[lang]").attr("lang");

        this.model.set("image_name_"+lang,null);
        this.model.set("image_hash_"+lang,null);
        
    }
});