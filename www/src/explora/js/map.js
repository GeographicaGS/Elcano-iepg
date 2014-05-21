
app.view.map = function(options){
    this.baseLayer = null;

    this._choroplethColors = ["#800026","#BD0026","#E31A1C","#FC4E2A","#FD8D3C"];

    this.CHOROPLETH_INTERVALS = 5;

    this._choroplethOVerlay = null;

    this.container = options.container;
    this.zoom = options.zoom ? options.zoom : 2;
    this.center = options.center ? options.center  : L.latLng(0,0);

    this.initialize = function(options){

        this._map = L.map(this.container,{
            "attributionControl" : false,
            "zoomControl" : false
        }).setView( this.center, this.zoom);

        this.loadBaseMap();
        return this;
    };

    this.loadBaseMap = function(){
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
    };

    /* Resize the map */ 
    this.resize = function(){
        this._map.invalidateSize(true);
        return this;
    };

    this.getMap = function(){
        return this._map;
    };

    /* This method created a choropleth Map with the data supplied in the parameter */ 
    this.drawChoropleth = function(data){

        var n_intervals = data.length < this.CHOROPLETH_INTERVALS ? data.length :  this.CHOROPLETH_INTERVALS ;
        // Just for security
        if (!data || !data.length) return;

        // Remove previous choropleth, needed for redraws
        this.removeChoropleth();

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
                return _this._choroplethColors[ n_intervals-1];
            }
            else if (d==min){
                return _this._choroplethColors[0];
            }
            else{
                var index = parseInt(  ((d-min) *  n_intervals) /
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
            this._div = L.DomUtil.create('div', 'info data'); // create a div with a class "info"
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

        // Let's add a legend for the map. 

        var legend = L.control({position: 'bottomright'});

        legend.onAdd = function (map) {

            // Create the legend element inside the DOM.
            var div = L.DomUtil.create('div', 'info legend'),
                grades = [],
                labels = [],
                inc = parseInt(max/n_intervals);

            for (var i=0;i<n_intervals;i++){
                grades.push(parseInt(i*inc + min));
            }

            // loop through our density intervals and generate a label with a colored square for each interval
             for (var i=0;i<n_intervals;i++){
                div.innerHTML +=
                    '<i style="background:' + getColor(grades[i] +1) + '"></i> ' +
                    grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
            }

            return div;
        };

        legend.addTo(this._map);

        this._choroplethOVerlay = {
            "geoJson" : l,
            "legend" : legend,
            "info" : info
        };

        return l;
    };

    this.removeChoropleth = function(){
       
        if (this._choroplethOVerlay){   
            this._map.removeLayer(this._choroplethOVerlay["geoJson"]);
            this._choroplethOVerlay["info"].removeFrom(this._map);
            this._choroplethOVerlay["legend"].removeFrom(this._map);
            this._choroplethOVerlay = null;
        }

        return this;
    }   

}