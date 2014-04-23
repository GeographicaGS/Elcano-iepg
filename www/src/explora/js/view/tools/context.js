app.view.tools.context = function(){
    
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
        "variables": [1],    
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
        localStorage.setItem("context",
            JSON.stringify(data)
        );
    };

    // Restore the context from local store
    this.restoreSavedContext = function(){
        var tmp = localStorage.getItem("context");
        if (tmp){
            this.data = tmp;    
        }

        if (!this.data.countries.list.length){
            this.data.countries.list = [(app.country ? app.country : "ES")];
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

};
