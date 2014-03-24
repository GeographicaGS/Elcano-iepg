app.view.highlights.ListView = Backbone.View.extend({
    ///highlight/publishedcatalog
    _template : _.template( $('#highlights_list_template').html() ),
    _templateData : _.template( $('#highlights_list_data_template').html() ),
    _page : 0,
    _timeout: null,
    initialize: function() {
        app.events.trigger("menu","highlights");
        this.render();
        this.collectionPublished = new app.collection.HighlightPublish();
        this.collectionUnpublished = new app.collection.HighlightUnpublish();

        this.listenTo(this.collectionPublished,"reset",function(){
            this.renderPublished();
        });

        this.listenTo(this.collectionUnpublished,"reset",function(){
            this.renderUnpublished();
        });


        this.collectionPublished.fetch({"reset" : true});
        this.collectionUnpublished.fetch({"reset" : true});

    },
    events: {
        "click #more" : "nextPage",
        "click #ctrl_search" : "showSearchUI",
        "blur #search_form input" : "closeSearchUI",
        "keyup #search_form input": function(e){
            if (e.keyCode==27){
                this.$searchInput.val("");
                this.search();
            }
            else{
                
                if(this._timeout){
                    clearTimeout(this._timeout);
                    this._timeout = null;
                }
                var self = this;
                this._timeout = setTimeout(function(){
                    self.search();
                }, app.config.SEARCH_TIMER);    
            }
        }
    },

    renderPublished: function(){
        var self = this;
        this.$published.html(this._templateData({
            "collection" : this.collectionPublished.toJSON(),
            "published" : true
        })).sortable({
            stop: function( event, ui ) {
                // get order list of ids
                var data = {
                    "order" :  $.map(self.$published.children(),function(val,id){
                        return $(val).attr("data-id-highlight");
                    })
                }
                // save order in the server
                $.ajax({
                    "url": app.config.API_URL + "/highlight/setorder",
                    "type": "PUT",
                    "contentType": "application/json",
                    "data": JSON.stringify(data),
                });

                var i = 1,
                    max = self.collectionPublished.length;

                self.$published.find(".orden").each(function(){
                    $(this).html(i +"/" + max);
                    i++;
                });

                
            }
        });

    },

    renderUnpublished: function(){
        // this.$unpublished.html(this._templateData({
        //     "collection" : this.collectionUnpublished.toJSON(),
        //     "published" : false
        // }));

        var begin = this._page * app.config.PAGE_SIZE_HIGHLIGHT,
            end = begin + app.config.PAGE_SIZE_HIGHLIGHT,
            subcollection = _.map(this.collectionUnpublished.slice(begin, end),function(e){ return e.toJSON()}),
            html = this._templateData({
                "collection": subcollection,
                "published" : false
            });

        if (!this._page)
            this.$unpublished.html(html);
        else
            this.$unpublished.append(html);

        this.$totalElements.html(this.collectionUnpublished.listSize);
        this.$totalVisibleElements.html(this.collectionUnpublished.length);
        this.$startElement.html(this.collectionUnpublished.length ? "1" : "0");

        if ((this._page && !this.collectionUnpublished.length)
            ||
            this.collectionUnpublished.length < app.config.PAGE_SIZE_HIGHLIGHT
            ||
            this.collectionUnpublished.length == this.collectionUnpublished.listSize
            )
            this.$controlMore.hide();
        else
            this.$controlMore.show();
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {
        this.$el.html(this._template());
        this.$published = this.$("#published");
        this.$unpublished = this.$("#unpublished");
        this.$searchForm = this.$("#search_form");
        this.$controlMore = this.$("#ctrl_more");
        this.$totalElements = this.$("#total_elements");
        this.$totalVisibleElements = this.$("#total_visible_elements");
        this.$startElement = this.$("#start_element");

        return this;
    },

    search: function(){
        this.collectionUnpublished.search = $.trim(this.$searchInput.val());
        this._page = 0;
        this.collectionUnpublished.fetch({"reset" : true},{});
    },

    nextPage: function(){
        this._page++;
        this.collectionUnpublished.page = this._page;
        this.listenToOnce(this.collectionUnpublished,"sync",function(){
            this.renderUnpublished();
        });
        this.collectionUnpublished.fetch({remove: false});
    },

    showSearchUI: function(){
        this.$searchForm.fadeIn(300);
        this.$searchInput.focus();
    },

    closeSearchUI:function(){
         this.$searchForm.fadeOut(300);
    }
});