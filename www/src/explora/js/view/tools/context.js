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
    // ID of the context
    this.id = id;
    
    this.data = {
        "countries": {
            // List of countries. This list always has a country, the default value will be the country where the user is.
            "list" : [],
            // Countries selected. It's a FIFO Queue. 
            "selection" : []
        },
        // List of the current slider in the context. 
        "slider": [],
        // List of variables
        "variables": ["iepg"],    
    };


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
                "type" : "Interval",
                "date_start": "Mon Jan 1 2005 00:00:00 GMT+0000", // date object
                "date_finish": "Mon Jan 1 2006 00:00:00 GMT+0000", // date object
            }
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
            }]
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
        for (var i=0;i<this.data.countries.selection.length;i++){
            var index = this.data.countries.list.indexOf(this.data.countries.selection[i]);
            if (index == -1) {
                this.data.countries.selection.splice(i, 1);
            }
        }    
        
        
    },

    this.clear = function(){
        localStorage.removeItem("context-"+this.id);
    }

};
