app.collection.Authors = Backbone.Collection.extend({
    
    initialize: function(models, options) {

    },

    removeEmpties: function() {
	    filtered = this.filter(function(a) {
	      return a.get("twitter_user") =! "" || a.get("name")!="";
	    });

	    return this.set(filtered);
	}

});
