app.map = {
    _baseLayer: null,
    
    initialize : function(){

        this._map = L.map('map',{
            "attributionControl" : false,
            "zoomControl" : false
        }).setView( L.latLng(48.99,-104.05), 3);

        this.loadBaseMap();
    },

    loadBaseMap : function(){
        this._baseLayer = L.geoJson(countriesGeoJSON, {
            style: {
                fillColor: "#fff",
                weight: 2,
                opacity: 1,
                color: '#e3e3e6',
                // dashArray: '3',
                fillOpacity: 0.7
            }
        });
        this._baseLayer.addTo(this._map);  
    },

    resize: function(){
        this._map.invalidateSize(true);
    },

    getMap: function(){
        return this._map;
    },

    drawChoropleth : function(data){

    }

    
}