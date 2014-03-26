app.view.news.ListView = Backbone.View.extend({
    _template : _.template( $('#news_list_template').html() ),
    _templateList : _.template( $('#news_list_item_data_template').html() ),
    _page : 0,
    _timeout: null,
    initialize: function() {
        app.events.trigger("menu","docs");
        this.collection = new app.collection.New();
        this.collection.fetch({"reset" : true},{});
        this.listenTo(this.collection,"reset", function(){
            this.renderPageList();    
        });
        this.render();
    },

    events:{
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
            
           
        },
    },

    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    search: function(){
        this.collection.search = $.trim(this.$searchInput.val());
        this._page = 0;
        this.collection.fetch({"reset" : true},{});

    },

    nextPage: function(){
        this._page++;
        this.collection.page = this._page;
        this.listenToOnce(this.collection,"sync",function(){
            this.renderPageList();
        });
        this.collection.fetch({remove: false});
    },

    showSearchUI: function(){
        this.$searchForm.fadeIn(300);
        this.$searchInput.focus();
    },

    closeSearchUI:function(){
         this.$searchForm.fadeOut(300);
    },

    renderPageList: function(){

        var begin = this._page * app.config.PAGE_SIZE,
            end = begin + app.config.PAGE_SIZE,
            subcollection = _.map(this.collection.slice(begin, end),function(e){ return e.toJSON()}),
            html = this._templateList({
                collection: subcollection
            });

        if (!this._page)
            this.$listData.html(html);
        else
            this.$listData.append(html);

        this.$totalElements.html(this.collection.listSize);
        this.$totalVisibleElements.html(this.collection.length);
        this.$startElement.html(this.collection.length ? "1" : "0");

        if ((this._page && !this.collection.length)
            ||
            this.collection.length < app.config.PAGE_SIZE
            ||
            this.collection.length == this.collection.listSize
            )
            this.$controlMore.hide();
        else
            this.$controlMore.show();
    },

    render: function() {
        this._page = 0;
        this.$el.html(this._template({
            //collection : this.collection.toJSON(),
            //listSize : this.collection.listSize
        }));
        this.$listData = this.$("#list_data");
        this.$searchForm = this.$("#search_form");
        this.$ctrlSearch = this.$("#ctrl_search");
        this.$searchInput = this.$searchForm.find("input");
        this.$totalElements = this.$("#total_elements");
        this.$totalVisibleElements = this.$("#total_visible_elements");
        this.$startElement = this.$("#start_element");
        this.$controlMore = this.$("#ctrl_more");
           
        return this;
    }

});