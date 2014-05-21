app.view.news.FormView = Backbone.View.extend({
    _template : _.template( $('#news_form_template').html() ),
    _saveRequest : false,

    initialize: function(options) {
        app.events.trigger("menu","news");

        this.labels = {};
        this.labels["es"] = new app.collection.Label(null,"es");
        this.labels["en"] = new app.collection.Label(null,"en");

        this.sections = new Backbone.Collection([
            {
                "id" : 1,
                "description" : "Blog"
            },
            {
                "id" : 2,
                "description" : "En los medios"
            },
            {
                "id" : 3,
                "description" : "Eventos"
            },
        ]);
     
        if (!options || !options.id){
            this.model = new app.model.New({
                "labels_es" : new Backbone.Collection(),
                "labels_en" : new Backbone.Collection(),
            });
            this._initialize();
        }
        else{
            var self = this;
            this.model = new app.model.New({"id" : options.id});
            this.model.fetch({
                success: function(){
                    self._initialize();
                }
            });
        }
    },
    
    _initialize: function(){


        this.listenTo(this.model.get("labels_es"),"add remove", function(){
            this.renderSelectLabels("es");
        });

        this.listenTo(this.model.get("labels_en"),"add remove", function(){
            this.renderSelectLabels("en");
        });

        
        Backbone.Validation.bind(this);

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
        "click .save_button": "save",
        "blur input[name],textarea[name],select[name]": "validate",
        "click #upload_pdf_es,#upload_pdf_en" : function(e){
            e.preventDefault();
            var $e = $(e.target),
                $file = $e.siblings("input[type='file']");
            $file.trigger("click");
        },
        "click  .cancel" : function(){
            app.router.navigate("news",{trigger: true});
        }
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
        
        if (label && !this.labels[lang].where({"label": label}).length) {
            this.labels[lang].create({label: label});
        }
        
        $input.val("");
        
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
            "text_en" : app.input(this.$("textarea[name='text_en']").val()),
            "text_es" : app.input(this.$("textarea[name='text_es']").val()),
            "url_en" : app.input(this.$("input[name='url_en']").val()),
            "url_es" : app.input(this.$("input[name='url_es']").val()),
            "news_section" : this.$("select[name='news_section']").val()
        };

        this.model.set(data);
         
        if (this.model.isValid(true)){
            // Save on server
            this.model.save(null,{
                saved: true,
                success: function(model){
                    app.router.navigate("news/" + model.get("id"),{trigger: true});
                }
            });
        }
        else{
            app.scrollTop();
        }
    },
    render: function() {


        this.$el.html(this._template({
            model: this.model.toJSON(),
            sections : this.sections.toJSON(),
        }));
        this.$labels_es = this.$("#labels_es .tagsList");
        this.$labels_en = this.$("#labels_en .tagsList");
        this.$cLabelsES = this.$("#labels_es .clabels");
        this.$cLabelsEN = this.$("#labels_en .clabels");
        this.renderSelectLabels("es");
        this.renderSelectLabels("en");
        this.renderLabels();
        return this;
    },
});