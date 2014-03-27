app.view.Contact = Backbone.View.extend({
    _template : _.template( $('#contact_template').html() ),
    pos : new google.maps.LatLng(40.431215,-3.679846),
    
    initialize: function() {
        app.events.trigger("menu","");
        this.render();
    },
    
    onClose: function(){
        // Remove events on close
        this.stopListening();
    },
    _drawMap: function(){ 
        var mapStyle = [
            {
                featureType: "all",
                elementType: "all",
                stylers: [
                    { lightness: 30 },
                    { saturation: -100 }
                ]
            }
        ];

        var mapOptions = {
            zoom: 15,
            center: this.pos,
            disableDefaultUI: true,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            mapTypeControlOptions: {
                mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'basslineStyle']
            }
        };

        this._map = new google.maps.Map(this.$("#map")[0],mapOptions);

        var styledMapOptions = {
            name: "Elcano"
        }

        var mapType = new google.maps.StyledMapType(mapStyle, styledMapOptions);
        this._map.mapTypes.set('geoStyle', mapType);
        this._map.setMapTypeId('geoStyle');

        var marker = new google.maps.Marker({             
            icon:  {
                url: "/img/ELC_marcador_mapa.png",
                size: new google.maps.Size(34,34),
                anchor: new google.maps.Point(10,30)
            },        
            map: this._map,
            position: this.pos
        });     
    },
    
    render: function() {
        this.$el.html(this._template());
        this._drawMap();
        var self= this;
        setTimeout(function(){
            google.maps.event.trigger(self._map, "resize");
        },1000);

        
        return this;
    }
});