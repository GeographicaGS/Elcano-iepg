app.context = {
    data: {
        "countries": [],
        "slider": {
            "dates": ["Mon Jan 1 1990 00:00:00 GMT+0000",
                "Mon Jan 1 1995 00:00:00 GMT+0000",
                "Mon Jan 1 2000 00:00:00 GMT+0000", 
                "Mon Jan 1 2005 00:00:00 GMT+0000",
                "Mon Jan 1 2010 00:00:00 GMT+0000",
                "Mon Jan 1 2015 00:00:00 GMT+0000 "],
            "current" : "Mon Jan 1 2005 00:00:00 GMT+0000"
        },
        "variables": [1],    
    },

    // Slider sample data definition.
    // {
    //     "type" : "TypeSinglePointSlider",
    //     "dates": ["Mon Jan 1 1990 00:00:00 GMT+0000 ",
    //         "Mon Jan 1 1995 00:00:00 GMT+0000",
    //         "Mon Jan 1 2000 00:00:00 GMT+0000", 
    //         "Mon Jan 1 2005 00:00:00 GMT+0000",
    //         "Mon Jan 1 2010 00:00:00 GMT+0000",
    //         "Mon Jan 1 2015 00:00:00 GMT+0000 "],
    //     "current" : "Mon Jan 1 2005 00:00:00 GMT+0000"
    // }

    // {
    //     "type" : "TypeIntervalSlider",
    //     "dates": ["Mon Jan 1 1990 00:00:00 GMT+0000 ",
    //         "Mon Jan 1 1995 00:00:00 GMT+0000",
    //         "Mon Jan 1 2000 00:00:00 GMT+0000", 
    //         "Mon Jan 1 2005 00:00:00 GMT+0000",
    //         "Mon Jan 1 2010 00:00:00 GMT+0000",
    //         "Mon Jan 1 2015 00:00:00 GMT+0000 "],
    //        "current" : {
    //            "start": "Mon Jan 1 2005 00:00:00 GMT+0000",
    //            "end" : "Mon Jan 1 2005 00:00:00 GMT+0000"
    //        }
    // }
        
    // This method modifies the global context, it also store the context in localStorage
    setContext: function(data){
        this.data = _.clone(data);
        this.saveContext();
    },

    // It saves the context in the local storage
    saveContext: function(){
        localStorage.setItem("context",
            JSON.stringify(data)
        );
    },

    // Restore the context from local store
    restoreSavedContext: function(){
        var tmp = localStorage.getItem("context");
        if (tmp){
            this.data = tmp;    
        }
    }

};
