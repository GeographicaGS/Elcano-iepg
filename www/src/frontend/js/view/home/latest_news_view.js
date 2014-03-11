app.view.LatestNews = Backbone.View.extend({
    _template : _.template( $('#latest_news_template').html() ),
    
    initialize: function() {
    
        this.collection = new app.collection.LatestNews();
        
        this.listenTo(this.collection,"reset",function(){
            this.render();
        });

        this.$el.html(app.loadingHTML());
        this.collection.fetch({"reset":true});
    },

    load: function(idx){
       
        switch(idx){
            case 0: 
                this.collection.section = null;
                break;
              
            case 1:
                this.collection.section = "Blog";
                break;
            case 2:
                this.collection.section = "Media";
                break;
            case 3: 
                this.collection.section = "Events";
                break;
            case 4: 
                this.collection.section = "Documents";
                break;
            case 5:
                this.collection.section = "Twitter";
                break;
        }
        this.$el.html(app.loadingHTML());
        this.collection.fetch({"reset":true});
    },


    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    
    render: function() {

        this.$el.html(this._template({
            collection: this.collection.toJSON(),
            section : this.collection.section
        }));
        return this;
    }
});