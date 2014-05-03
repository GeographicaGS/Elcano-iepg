
app.map = {
    _baseLayer: null,
    _choroplethColors : ["#800026","#BD0026","#E31A1C","#FC4E2A","#FD8D3C"],
    CHOROPLETH_INTERVALS : 5,

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
        // Just for security
        if (!data || !data.length) return;

        var bigJSON = [],
            values = _.pluck(data,"value"),
            max = _.max(values),
            min = _.min(values),
            rangeData = max - min;

        // We build the GeoJSON, for the choropleth
        for (var i=0;i<data.length;i++){
            if (!data[i].code){
                continue;
            }
            var country = app.findCountry(data[i].code);
            if (!country){
                continue;
            }
            country.properties.value = data[i].value;
            bigJSON.push(country);
        }

        var _this = this;

        function getColor(d){

            if (d == max){
                return _this._choroplethColors[ _this.CHOROPLETH_INTERVALS-1];
            }
            else if (d==min){
                return _this._choroplethColors[0];
            }
            else{
                var index = parseInt(  ((d-min) *  _this.CHOROPLETH_INTERVALS) /
                                    rangeData );
                return _this._choroplethColors[index];
            }
        }

        function style(feature) {
            return {
                fillColor: getColor(feature.properties.value),
                weight: 2,
                opacity: 1,
                color: 'white',
                dashArray: '3',
                fillOpacity: 0.7
            };
        }

        function highlightFeature(e) {
            var layer = e.target;

            layer.setStyle({
                weight: 2,
                color: '#666',
                dashArray: '',
                fillOpacity: 0.7
            });

            if (!L.Browser.ie && !L.Browser.opera) {
                layer.bringToFront();
            }

            info.update(layer.feature.properties);
        }

        function resetHighlight(e) {
            l.resetStyle(e.target);
            info.update();
        }

        function zoomToFeature(e) {
            this._map.fitBounds(e.target.getBounds());
        }

        function onEachFeature(feature, layer) {
            layer.on({
                mouseover: highlightFeature,
                mouseout: resetHighlight,
                click: zoomToFeature
            });
        }

        var l = L.geoJson(bigJSON, {
            style: style,
            onEachFeature: onEachFeature
        });

        l.addTo(this._map);

        var info = L.control();

        info.onAdd = function (map) {
            this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
            this.update();
            return this._div;
        };

        // method that we will use to update the control based on feature properties passed
        info.update = function (props) {
            var country_name = props ?  props["name_"+app.lang] : "<lang>Mueve el ratón sobre un país</lang>";
            this._div.innerHTML = "<h4>" + app.variableToString(app.context.data.variables[0]) + "</h4>" +  (props ?
                "<b>" + country_name + "</b><br />" + sprintf("%0.2f",props.value)
                : "<lang>Mueve el ratón sobre un país</lang>");
        };

        info.addTo(this._map);

        var legend = L.control({position: 'bottomright'});

        legend.onAdd = function (map) {

            var div = L.DomUtil.create('div', 'info legend'),
                grades = [],
                labels = [],
                inc = parseInt(max/_this.CHOROPLETH_INTERVALS);

            for (var i=0;i<_this.CHOROPLETH_INTERVALS;i++){
                grades.push(parseInt(i*inc + min));
            }

            // loop through our density intervals and generate a label with a colored square for each interval
             for (var i=0;i<_this.CHOROPLETH_INTERVALS;i++){
                div.innerHTML +=
                    '<i style="background:' + getColor(grades[i] +1) + '"></i> ' +
                    grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
            }

            return div;
        };

        legend.addTo(this._map);

        return l;
    }   
}