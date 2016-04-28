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
                'limit': [430,120,480,170]
            },
            'primary_goods' : {
                'limit': [526,155,576,211]
            },
            'manufactures' : {
                'limit': [596,232,645,282]
            },
            'services' : {
                'limit': [634,326,686,376]
            },
            'investments' : {
                'limit': [638,427,685,477]
            },
            'economic_presence' : {
                'limit': [485,304,540,351]
            },
            'troops' : {
                'limit': [597,520,644,571]
            },
            'military_equipment' : {
                'limit': [523,594,575,641]
            },
            'military_presence' : {
                'limit': [475,468,522,518]
            },
            'migrations' : {
                'limit': [433,633,475,680]
            },
            'tourism' : {
                'limit': [328,635,377,680]
            },
            'sports' : {
                'limit': [237,591,280,647]
            },
            'culture' : {
                'limit': [165,520,216,569]
            },
            'information' : {
                'limit': [124,426,173,480]
            },
            'technology' : {
                'limit': [126,325,172,376]
               
            },
            'science' : {
                'limit': [163,233,215,281],
                
            },
            'education' : {
                'limit': [235,160,285,210]
                
            },
            'cooperation' : {
                'limit': [332,121,378,170]
                
            },
            'soft_presence' : {
                'limit': [250,400,301,454]
                
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
        //console.log(e.offsetX +',' + e.offsetY);

        var x = e.offsetX,
            y = e.offsetY,
            variables  = this._vars(),
            found=false;

        for (var i in variables){
            var el = variables[i].limit
            if (x>=el[0] && x<=el[2] && y>=el[1] && y<=el[3]){
                return this.model.set({
                    'currentover': i,
                    'pos' : {'x' : el[2], 'y': el[3]}
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
            this.$tooltip.find('p').html(this.$('#'+c+'_text').html());
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