app.view.Structure = Backbone.View.extend({
    _template : _.template( $('#structure_template').html() ),
    
    initialize: function(options) {
        app.events.trigger("menu","about");
        this.model = new Backbone.Model({
            currentover: null
        });
        this.listenTo(this.model,'change:currentover',this.renderTooltip);
        this.render();

    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },

    events: {
        'mousemove #structuremap': '_hoverImage'
    },

    _vars : function(){
        return {
            //'<var>' : [upper left x,u left y,lower right x, lower right y]
            'energy' : {
                'limit': [430,120,480,170],
                'text': '<lang>Variable energy desc TEXTO</lang>'
            },
            'primary_goods' : {
                'limit': [526,155,576,211],
                'text': '<lang>Variable primary_goods desc TEXTO</lang>'
            },
            'manufactures' : {
                'limit': [596,232,645,282],
                'text': '<lang>Variable manufactures desc TEXTO</lang>'
            },
            'services' : {
                'limit': [634,326,686,376],
                'text': '<lang>Variable services desc TEXTO</lang>'
            },
            'investments' : {
                'limit': [638,427,685,477],
                'text': '<lang>Variable investments desc TEXTO</lang>'
            },
            'economic_presence' : {
                'limit': [485,304,540,351],
                'text': '<lang>Variable economic_presence desc TEXTO</lang>'
            },
            'troops' : {
                'limit': [597,520,644,571],
                'text': '<lang>Variable troops desc TEXTO</lang>'
            },
            'military_equipment' : {
                'limit': [523,594,575,641],
                'text': '<lang>Variable military_equipment desc TEXTO</lang>'
            },
            'military_presence' : {
                'limit': [475,468,522,518],
                'text': '<lang>Variable military_presence desc TEXTO</lang>'
            },
            'migrations' : {
                'limit': [433,633,475,680],
                'text': '<lang>Variable migrations desc TEXTO</lang>'
            },
            'tourism' : {
                'limit': [328,635,377,680],
                'text': '<lang>Variable tourism desc TEXTO</lang>'
            },
            'sports' : {
                'limit': [237,591,280,647],
                'text': '<lang>Variable sports desc TEXTO</lang>'
            },
            'culture' : {
                'limit': [165,520,216,569],
                'text': '<lang>Variable culture desc TEXTO</lang>'
            },
            'information' : {
                'limit': [124,426,173,480],
                'text': '<lang>Variable information desc TEXTO</lang>'
            },
            'technology' : {
                'limit': [126,325,172,376],
                'text': '<lang>Variable technology desc TEXTO</lang>'
            },
            'science' : {
                'limit': [163,233,215,281],
                'text': '<lang>Variable science desc TEXTO</lang>'
            },
            'education' : {
                'limit': [235,160,285,210],
                'text': '<lang>Variable education desc TEXTO</lang>'
            },
            'cooperation' : {
                'limit': [332,121,378,170],
                'text': '<lang>Variable cooperation desc TEXTO</lang>'
            },
            'soft_presence' : {
                'limit': [250,400,301,454],
                'text': '<lang>Variable soft_presence desc TEXTO</lang>'
            }
        };
        
    },
    
    render: function() {
        
        this.$el.html(this._template());
        this.$coef = this.$('.coef');
        this.$tooltip = this.$('.tooltip');
        return this;
    },

    _hoverImage: function(e){
        console.log(e.offsetX +',' + e.offsetY);

        var x = e.offsetX,
            y = e.offsetY,
            variables  = this._vars(),
            found=false;

        for (var i in variables){
            var el = variables[i].limit
            if (x>=el[0] && x<=el[2] && y>=el[1] && y<=el[3]){
                return this.model.set({
                    'currentover': i,
                    'pos' : {'x' : el[2], 'y': el[3]},
                    'text' : variables[i].text
                });
            }
        }

        this.model.set('currentover',null);
        
    },

    renderTooltip: function(){
        var c = this.model.get('currentover'),
            pos = this.model.get('pos');

        if (c){
            this.$coef.css('cursor','pointer');
            this.$tooltip.css('left',pos.x).css('top',pos.y);
            this.$tooltip.find('p').html(this.model.get('text'));
            this.$tooltip.find('.variable').html(app.variableToString(c));
            this.$tooltip.attr('data-variable',c);
            this.$tooltip.show();
        }
        else{
            this.$coef.css('cursor','inherit');
            this.$tooltip.hide();
        }


    }
});