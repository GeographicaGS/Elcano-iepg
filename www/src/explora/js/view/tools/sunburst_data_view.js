app.view.tools.SunburstDataView = Backbone.View.extend({
    _template : _.template( $('#chart_sunburst_data').html() ),
    
    className: 'sunburst_data',

    initialize: function(options) {
    },

    events: {
      'click .childs[data-section]': '_moveTo',
      'click .th2[data-top]' : '_moveTop'
    },

    _setListeners: function(){
      this.listenTo(app.events,'sunburst:moveto',this.render);
    },

    setTree: function(tree){
      this._tree = tree;
    },

    _moveTo: function(e){
      e.preventDefault();
      var $e = $(e.target).closest('.childs'),
        section = $e.attr('data-section');

      if (section)
        app.events.trigger('sunburst:moveto',section,750);
    },

    _moveTop: function(e){
      e.preventDefault();
      var $e = $(e.target).closest('.th2'),
        section = $e.attr('data-top');

      if (section)
        app.events.trigger('sunburst:moveto',section,750);
    },

    render: function(name){
      this.$el.html(this._template({
          data: this.model.get('tree').findElementInTree(name),
          family : this.model.get('family')
      }));
    },

    gofront: function(){
      this.delegateEvents(); 
      this._setListeners();
      console.log('front data');
      
    },

    goback: function(){
      this.undelegateEvents();
      this.stopListening();
      console.log('back data');
    }
    
});