app.view.tools.SunburstComparisonDataView = Backbone.View.extend({
    _template : _.template( $('#chart_sunburst_comparison_data').html() ),
    
    className: 'sunburst_comparison_data',

    initialize: function(options) {
      this._iepgvsiepe = options.iepgvsiepe || false;
    },

    events: {
      'click .childs[data-section]': '_moveTo',
      'click .th2[data-top]' : '_moveTop'
    },

    _setListeners: function(){
      this.listenTo(app.events,'sunburst:moveto',this.render);
    },

    _moveTo: function(e){
      e.preventDefault();
      var $e = $(e.target).closest('.childs'),
        section = $e.attr('data-section');

      if (section)
        app.events.trigger('sunburst:moveto',['left','right'],section,750);
    },

    _moveTop: function(e){
      e.preventDefault();
      var $e = $(e.target).closest('.th2'),
        section = $e.attr('data-top');

      if (section)
        app.events.trigger('sunburst:moveto',['left','right'],section,750);
    },

    render: function(pos,name,time){
      console.log('Sunburst comparison');
      this.$el.html(this._template({
          data: {
            'root_left' : this.model.get('tree_left').findElementInTree('global'),
            'root_right' : this.model.get('tree_right') ? this.model.get('tree_right').findElementInTree('global') : null,
            'left': this.model.get('tree_left').findElementInTree(name),
            'right': this.model.get('tree_right') ? this.model.get('tree_right').findElementInTree(name) : null,
          },
          family : this.model.get('family'),
          iepgvsiepe : this._iepgvsiepe
      }));
    },

    gofront: function(){
      this.delegateEvents(); 
      this._setListeners();
    },

    goback: function(){
      this.undelegateEvents();
      this.stopListening();
    }
    
});