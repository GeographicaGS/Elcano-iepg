app.view.docs.FormView = Backbone.View.extend({
    _template : _.template( $('#docs_form_template').html() ),
    _authorsTemplate : _.template( $('#docs_author_template').html() ),
    _pdfsTemplate: _.template($("#docs_pdf_files_data_template").html()),
    _saveRequest : false,

    initialize: function(options) {
        app.events.trigger("menu","docs");

        this.labels = {};
        this.labels["es"] = new app.collection.Label(null,"es");
        this.labels["en"] = new app.collection.Label(null,"en");

     
       
        if (!options || !options.id){
            
            this.model = new app.model.Document({
                "labels_es" : new Backbone.Collection(),
                "labels_en" : new Backbone.Collection(),
                "pdfs_es" : new Backbone.Collection(),
                "pdfs_en" : new Backbone.Collection(),
                "authors" : new app.collection.Authors({
                    "twitter_user" : null,
                    "name" : null,
                    "position_es" : null,
                    "position_en" : null
                })
            });
            this._initialize();
            
        }
        else{
            var self = this;
            this.model = new app.model.Document({"id" : options.id});
            this.model.fetch({
                success: function(){
                    self._initialize();
                }
            });
        }
    },
    
    _initialize: function(){

     

        this.listenTo(this.model.get("pdfs_es"),"add remove", function(){
            this.renderPDFs();
        });

        this.listenTo(this.model.get("pdfs_en"),"add remove", function(){
            this.renderPDFs();
        });

        this.listenTo(this.model.get("labels_es"),"add remove", function(){
            this.renderSelectLabels("es");
        });

        this.listenTo(this.model.get("labels_en"),"add remove", function(){
            this.renderSelectLabels("en");
        });

        this.listenTo(this.model.get("authors"),"add remove",function(){
            this.renderAuthors();
        });
        Backbone.Validation.bind(this/*, {
            valid: function(view, attr) {
              // do something
            }
            invalid: function(view, attr, error) {
                Backbone.Validation.callbacks.invalid.apply(this,[view, attr,error,"name"]);
            }
        },*/);

        this.render();

        for (i in this.labels){
            this.labels[i].fetch({reset: true});
            // Nested closure to render each labels
            this._listenToLabel(i);
        }

    },
    _listenToLabel: function(lang){
        this.listenTo(this.labels[lang],"reset change",function(){
            this.renderLabels(lang);
        });
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    
    events: {
        "click .ctrl_labels .anadir-bt": "toggleAddLabelUI",
        "click .ctrl_labels .btn-default": "addLabel",
        "click .ctrl_labels .tagsList .tag-add-bt": "selectLabel",
        "click .ctrl_labels .tag-active-bt" : "deleteLabel",
        'keyup .ctrl_labels .add_label_text': function(e){
             if (e.keyCode == 13) {
                // Enter pressed
                this.addLabel(e);
            }
        },
        "click #authors .btn-resena-remove" : "removeAuthor",
        "click #authors .btn-resena-more" : "addAuthor",
        "blur [twitter] input" : "editAuthor",
        "click .save_button": "save",
        "blur input[name],textarea[name]": "validate",
        "click #upload_pdf_es,#upload_pdf_en" : function(e){
            e.preventDefault();
            var $e = $(e.target),
                $file = $e.siblings("input[type='file']");
            $file.trigger("click");
        },
        "change input[type='file']" : "uploadPDF",
        "click .btnDeleteAjunto": "deletePDF",
        "click  .cancel" : function(){
            app.router.navigate("docs",{trigger: true});
        },

        "click .btn-resena-twitter-edit,.btn-resena-twitter" :  "toggleAuthorTwitterUI"
    },

    toggleAddLabelUI: function(e){
        var $el = $(e.target),
            $ui = $el.siblings(".tagForm");
            
        $el.blur();
        
        if ($ui.is(":visible")) 
            $ui.fadeOut(400);
        else
            $ui.fadeIn(400);
        
    },
    
    addLabel: function(e){
        // Add Label to server, also add this label to the list  of labels
        $e = $(e.target),
            $input = $e.is("input") ? $e : $e.parent().siblings("input"),
            label = $input.val().trim(),
            lang = $e.closest(".ctrl_labels").attr("id").substr(-2);
        
        if (label) {
            this.labels[lang].create({label: label});
            $input.val("");
        }
        
    },
    
    selectLabel: function(e){
        var $e = $(e.target),
            id_label = $e.attr("id_label"),
            label = $e.html().trim(),
            lang = $e.closest(".ctrl_labels").attr("id").substr(-2);

       
        if (!this.model.get("labels_"+lang).get(id_label)){
            this.model.get("labels_"+lang).add({
                id : id_label,
                label: label
            });
        
            // Close add form
            //.$("#labels_"+ lang +" .anadir-bt").trigger("click");    
        }
        
    },
    
    renderSelectLabels: function(lang){
        var labels = this.model.get("labels_"+lang),
            $c = lang == "es" ? this.$cLabelsES : this.$cLabelsEN,
            html = "";

        if (labels && labels.length) {
            //code
            for(var i=0;i<labels.length;i++){
                html += " <button type='button' class='btn btn-xs tag-active-bt' id_label="+labels.at(i).get("id") +">"
                            + labels.at(i).get("label") 
                            + "</button>";
            }
        }
        else{
            html = "<span class='cleanP'><lang>No hay etiquetas definidas</lang></span>";
        }
        $c.html(html);
    },
    
    deleteLabel: function(e){
        var $e = $(e.target),
            id_label = $e.attr("id_label"),
            lang = $e.closest(".ctrl_labels").attr("id").substr(-2);

        this.model.get("labels_"+lang).remove(id_label);
    },
    
    renderLabels: function(lang){
        if (!this.labels[lang])
            return;
        
        var $c = lang == "es" ? this.$labels_es : this.$labels_en;
        var html = "";
        for (var i=0;i<this.labels[lang].length;i++){
            var m = this.labels[lang].at(i);
            html += "<button type='button' class='btn btn-xs tag-add-bt' id_label="+ m.get("id") +">" + m.get("label") + "</button>";
        }
        $c.html(html);
    },
    
    addAuthor: function(){
        this.model.get("authors").add({
            "twitter_user" : null,
            "name" : null,
            "position_es" : null,
            "position_en" : null
        });  
    },
    
    removeAuthor: function(e){

        var $e = $(e.target),
            idx = $e.closest("[idx_author]").attr("idx_author");
            
        if (idx>0 ) {
            this.model.get("authors").remove(this.model.get("authors").at(idx));
        }
    },
    
    renderAuthors: function(){
        if (this.model.get("authors")){
            this.$("#authors").html(this._authorsTemplate({
                authors : this.model.get("authors").toJSON()
            }));    
        }
    },
    
    editAuthor: function(e){
        var $e = $(e.target),
            idx = $e.closest("[idx_author]").attr("idx_author"),
            m = this.model.get("authors").at(idx),
            val = $e.val().trim();
            
        m.set($e.attr("name"),val);    
    },
    
    validate : function(e){
        if (!this._saveRequest){
            return;
        }

        var $e = $(e.target),
            name = $e.attr("name");

        if (name!="authors"){
            this.model.set(name,$.trim($e.val()));
            this.model.isValid(true);    
        }
    },

    save: function(){
        this._saveRequest = true;
        var data = {
            "title_en" : app.input(this.$("input[name='title_en']").val()),
            "title_es" : app.input(this.$("input[name='title_es']").val()),
            "theme_en" : app.input(this.$("textarea[name='theme_en']").val()),
            "theme_es" : app.input(this.$("textarea[name='theme_es']").val()),
            "description_en" : app.input(this.$("textarea[name='description_en']").val()),
            "description_es" : app.input(this.$("textarea[name='description_es']").val()),
            "link_en" : app.input(this.$("input[name='link_en']").val()),
            "link_es" : app.input(this.$("input[name='link_es']").val()),
            
        }


        this.model.set(data);

        
         
        if (this.model.isValid(true)){

            this.model.get("authors").removeEmpties();

            // Save on server
            this.model.save(null,{
                saved: true,
                success: function(model){
                    app.router.navigate("docs/" + model.get("id"),{trigger: true});
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
        this.$labels_es = this.$("#labels_es .tagsList");
        this.$labels_en = this.$("#labels_en .tagsList");
        this.$cLabelsES = this.$("#labels_es .clabels");
        this.$cLabelsEN = this.$("#labels_en .clabels");
        this.$listPDFS = this.$("#list_pdf_files");

        this.renderAuthors();
        this.renderSelectLabels("es");
        this.renderSelectLabels("en");
        this.renderPDFs();
        this.renderLabels();
        return this;
    },

    uploadPDF: function(e){
        var $file = $(e.target),
            lang  = $file.attr("id").substr(-2);

        if ($file.val()== null || $file.val()==undefined || $file.val()=="undefined" || $file.val()=="" ){
            return;
        }

        var file = $file[0].files[0],
            name = file.name,
            /* Size in bytes */
            size = file.size,
            type = file.type,
            $unot =  this.$("#upload_notification_"+lang);
                    
        if (["application/pdf"].indexOf(type) == -1 ){
            $unot.html("<lang>Suba un fichero PDF</lang>.");
            setTimeout(function(){
                $unot.html("");
            },8000);

            return;
        }
                
        //max allow 8 MB
        max_allow = 8;
        if (size/(1024*1024) > max_allow){
            $unot.html("<lang>El fichero no puede ser mayor de </lang>" + " "+ max_allow +" MB.");
            setTimeout(function(){
                $unot.html("");
            },8000);

            return;
        }
        this._upload(lang,name);
    },

    _upload: function(lang,name){
        var $progress = this.$("#progress_"+lang),
            $uf = this.$("#upload_form_"+lang),
            formData = new FormData($uf[0]),
            $button = this.$("#upload_pdf_"+lang);

        $progress.show();
        $button.hide();

        var self = this;
        
        $.ajax({
            url: app.config.API_URL  + "/document/upload_pdf",
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
                
                self.model.get("pdfs_"+lang).add({
                    "hash": json.filename,
                    "name":name
                });   


                
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

    renderPDFs: function(){
        if (this.model.get("pdfs_es") && this.model.get("pdfs_en")){
            this.$listPDFS.html(this._pdfsTemplate({
                pdfs_es : this.model.get("pdfs_es").toJSON(),
                pdfs_en : this.model.get("pdfs_en").toJSON()
            }));    
        }
        
    },

    deletePDF: function (e){
        e.preventDefault();
        var $e = $(e.target),
            id_pdf = parseInt($e.attr("id_pdf")),
            lang = $e.attr("lang"),
            pdfs = lang == "es" ? this.model.get("pdfs_es") : this.model.get("pdfs_en");

        pdfs.remove(pdfs.at(id_pdf));
    },

    toggleAuthorTwitterUI: function(e){
        var $e = $(e.target),
            $parent = $e.closest("[twitter]"),
            idx = $parent.attr("idx_author");

        if ($parent.attr("twitter") == "yes"){
            $parent.attr("twitter","no");
            $parent.find(".twitter input").val("");
            this.model.get("authors").at(idx).set({
                "twitter_user" : null
            });
        }
        else{
            $parent.attr("twitter","yes");

            this.model.get("authors").at(idx).set({
                "name" : null,
                "position_en" : null,
                "position_es" : null
            });
            $parent.find(".notwitter input").val("");
        }
    }
});