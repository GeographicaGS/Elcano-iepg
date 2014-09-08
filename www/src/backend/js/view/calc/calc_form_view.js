app.view.calc.CalcFormView = Backbone.View.extend({
    _template : _.template( $('#calc_form_template').html() ),
    
    initialize: function() {
        app.events.trigger("menu","calc");
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    events:  {
        "click .calc_button": function(){
            $("input[name='file']").trigger("click");
        },
        "click  .cancel" : function(){
            history.back();
        },
        "change input[name='file']": function(){
            this.$("form").submit();
        }
    },
    
    render: function() {
        this.$el.html(this._template({}));

        return this;
    }
});