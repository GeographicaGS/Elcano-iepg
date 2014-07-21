Date.prototype.toJSON = function() {
    return 'date:' + (+this);
}

function revive(k, v) {
    if (typeof v == 'string' && v.indexOf('date:') == 0) {
        return new Date(+(v.slice(5)));
    }
    return v;
}

app.view.tools.context = function(id){
    

    /* DATA sample

     data: {
        "countries": {
            // List of countries
            "list" : ["ES","FR","AL"],
            // Countries selected. It's a FIFO Queue. 
            "selection" : ["ES"]
        },
        "slider": [{
                "type": "Point",
                "date" : "Mon Jan 1 1995 00:00:00 GMT+0000", // date object
            },
            {
                "type": "PointReference",
                "date" : "Mon Jan 1 1995 00:00:00 GMT+0000", // date object
            },
            {
                "type" : "Interval",
                "date_start": "Mon Jan 1 2005 00:00:00 GMT+0000", // date object
                "date_finish": "Mon Jan 1 2006 00:00:00 GMT+0000", // date object
            },

        ],
        // List of variables
        "variables": [1],    
    }

     */
        
    // It saves the context in the local storage
    this.saveContext = function(){
        localStorage.setItem("context-"+this.id,
            JSON.stringify(this.data)
        );
    };

    // Restore the context from local store
    this.restoreSavedContext = function(){
        var tmp = localStorage.getItem("context-"+this.id);
        if (tmp){
            //this.data = JSON.parse(tmp);  
            this.data = JSON.parse(tmp,revive);  
        }

        if (!this.data.countries.list.length){
            this.data.countries.list = [(app.country ? app.country : "ES")];
        }

        if (!this.data.slider.length){
            this.data.slider = [{
                "type" : "Point",
                "date" : app.config.SLIDER[app.config.SLIDER.length -1]
            }];
        }
    },

    this.getFirstSliderElement= function(type){
        for (var i=0;i<this.data.slider.length;i++){
            if (this.data.slider[i].type == type){
                return this.data.slider[i];
            }
        }

        return null;
    };

    this.removeInvalidSelected = function(){
        this.data.countries.selection =  _.intersection(this.data.countries.selection,this.data.countries.list);
    },

    this.clear = function(){
        localStorage.removeItem("context-"+this.id);
    }

    this.reset = function(){
        this.clear();
        this.data = this._initData();
    }

    // This method remove countries which are in the filter
    this.removeCountriesInFilter = function(){
        var filters = app.getFilters();
        if (filters.length){

            this.data.countries.list = _.difference(this.data.countries.list, filters);
            this.removeInvalidSelected();
        }
    }

    this._initData = function(){
        return {
            "countries": {
                // List of countries. This list always has a country, the default value will be spain.
                "list" : ["ES"],
                // Countries selected. It's a FIFO Queue. 
                "selection" : []
            },
            // List of the current slider in the context. 
            "slider": [{
                "type" : "Point",
                "date" : app.config.SLIDER[app.config.SLIDER.length -1]
            }],
            // List of variables
            "variables": ["global"],

            // Family it could be iepg or iepe
            "family" : "iepg",

            "block_analize" : 0,

            "version" : app.version
        };
    }

    // ID of the context
    this.id = id;
    
    this.data = this._initData();

};
