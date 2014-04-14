app.context = {
    data: {
        "countries": [],
        "slider": null,
        "variables": [],    
    },
    
    saveContext: function(){
        localStorage.setItem("context",
            JSON.stringify(data)
        );
    },
    restoreSavedContext: function(){
        var tmp = localStorage.getItem("context");
        if (tmp){
            this.data = tmp;    
        }
    }

};
