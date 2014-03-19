app.view.DocsList = Backbone.View.extend({
    _template : _.template( $('#docs_list_template').html() ),
    _templateList : _.template( $('#docs_list_data_template').html() ),
    _page : 0,
    _timeout: null,
    initialize: function() {
        app.events.trigger("menu","docs");
        this.collection = new app.collection.Docs();
       
        this.listenTo(this.collection,"reset", function(){
            this.renderPageList();    
        });

        this.filtersCollection = new app.collection.Label();
        
        this.listenTo(this.filtersCollection,"reset", function(){
            this.renderFilters();    
        });

        this.currentFilters = new Backbone.Collection();

        this.listenTo(this.currentFilters,"change reset add remove",function(){
            this.filtersChanged();
        });

        this.collection.fetch({reset: true});
        this.filtersCollection.fetch({reset: true});
        this.render();

    },
    events:{
        "click #ctrl_more" : "nextPage",
        "keyup .search_header input": function(e){
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
        "click #ctrl_filter": "ctrlFilterClick",
        "click #all_filters .label, .list_els .label": "addFilter",
        "click #sel_filters .label" : "removeFilter",
        "click #go_initial_list": "goInitialList"
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
        this.collection.offset = this._page* app.config.PAGE_SIZE ;
        this.listenToOnce(this.collection,"sync",function(){
            this.renderPageList();
        });
        this.collection.fetch({remove: false});
    },

    
    render: function() {
        this.$el.html(this._template());
        this.$searchInput = this.$(".search_header input");
        this.$controlMore = this.$("#ctrl_more");
        this.$listData = this.$(".list_els");
        this.$allFilters = this.$("#all_filters");
        this.$selFilters = this.$("#sel_filters");
        return this;
    },

    renderPageList: function(){

        var begin = this._page * app.config.PAGE_SIZE,
            end = begin + app.config.PAGE_SIZE,
            subcollection = _.map(this.collection.slice(begin, end),function(e){ return e.toJSON()});


        var html = this._templateList({
            collection: subcollection
        });

        if (!this._page){
            this.$listData.html(html);
        }
        else{
            this.$listData.append(html);
        }

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

    ctrlFilterClick : function(){
        if (this.$allFilters.is(":visible")){
            this.$allFilters.fadeOut(300);
        }
        else{
            this.$allFilters.fadeIn(300);
        }
    },
    renderFilters : function(){
        var html = "";

        this.filtersCollection.each(function(m){
            html += "<a href='#' class='label' data-id-filter=" + m.get("id")+ ">+ " + m.get("label") + "</a>";
        });

        this.$allFilters.html(html);
    },

    addFilter: function(e){
        var $e = $(e.target),
            id = $e.attr("data-id-filter");

        this.currentFilters.add(this.filtersCollection.get(id));

    },

    removeFilter: function(e){
        var $e = $(e.target),
            id = $e.attr("data-id-filter");

        this.currentFilters.remove(id);

    },

    filtersChanged: function(){
        var html = "";
        this.currentFilters.each(function(m){
            html += "<a href='#' class='label' data-id-filter=" + m.get("id")+ ">+ " + m.get("label") + "</a>";
        });
        this.$selFilters.html(html);
        this.search();
    },

    goInitialList: function(){
        this.$searchInput.val("");
        this.search();
    }
});