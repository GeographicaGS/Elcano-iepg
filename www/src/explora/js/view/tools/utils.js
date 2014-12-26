app.view.tools.utils.variablesColors = {
    "iepg" :"#fdc300",
    "iepe" : "#039",
    "economic_global" : "#2b85d0",
    "energy": "#4191d5",
    "primary_goods" : "#559dd9",
    "manufactures" : "#6baade",
    "services" : "#80b6e3",
    "investments": "#95c2e7",
    "military_global" : "#669900",
    "troops" : "#76a318",
    "military_equipment":"#85ad33",
    "soft_global": "#ff9000",
    "migrations" : "#ff960d",
    "tourism" : "#ff9b1a",
    "sports" : "#ffa126",
    "culture" : "#ffa633",
    "information" : "#ffac40",
    "technology" : "#ffb24d",
    "science" : "#ffb759",
    "education" : "#ffbc66",
    "cooperation" : "#ffc273"
};

app.view.tools.utils.getVariablesColorsForText = function(variable,family){
    switch(variable)
    {
        case "global":
            if (family == "iepg"){
                return "#d60006"
            }
            else{
                return app.view.tools.utils.variablesColors["iepe"];    
            }

        case "economic_global":
        case "energy":
        case "primary_goods":
        case "manufactures":
        case "services":
        case "investments":
            return app.view.tools.utils.variablesColors["economic_global"];

        case "military_global":
        case "troops":
        case "military_equipment":
            return app.view.tools.utils.variablesColors["military_global"];

        case "soft_global":
        case "migrations":
        case "tourism":
        case "sports":
        case "culture":
        case "information":
        case "technology":
        case "science":
        case "education":
        case "cooperation":
            return app.view.tools.utils.variablesColors["soft_global"];
    }
}

app.view.tools.utils.choroplethColors = {
    "iepg": ["#ffd88b","#f9be84","#fa976a","#ee6756","#de3338"],
    "iepe" : ["#ffe6b5","#e0cca4","#9f9a91","#607194","#264c97"],
    "economic_global" : ["#ffe0a2","#dfcc96","#a4ae99","#6e98ac","#4086bc"],
    "military_global": ["#fae5b8","#efd687","#cdc05c","#9ba333","#6b950e"],
    "soft_global": ["#ffe3b5","#ffd38d","#ff9922","#ff931f","#ff790a"]
}


app.view.tools.utils.getChoroplethColors = function(family,variable){
    switch(variable)
    {
        case "global":
            return app.view.tools.utils.choroplethColors[family];

        case "economic_global":
        case "energy":
        case "primary_goods":
        case "manufactures":
        case "services":
        case "investments":
            return app.view.tools.utils.choroplethColors["economic_global"];

        case "military_global":
        case "troops":
        case "military_equipment":
            return app.view.tools.utils.choroplethColors["military_global"];

        case "soft_global":
        case "migrations":
        case "tourism":
        case "sports":
        case "culture":
        case "information":
        case "technology":
        case "science":
        case "education":
        case "cooperation":
            return app.view.tools.utils.choroplethColors["soft_global"];
    }
}

app.view.tools.utils.variablesTree = function(variables,family){
	this.data = {
        "name" : "global",
        "color" : family == "iepg" ? "#fdc300" : "#039",
        "size" : !variables ? null : variables.global.value ,
        "perc" : !variables ? null : variables.global.percentage,

        "children" : [{
            "name" : "economic_global",
            "color" : "#2b85d0",
            "size" : !variables ? null : variables.economic_global.value,
            "perc" : !variables ? null : variables.economic_global.percentage,
            "ord" : 1,
            "children": [{
                "name" : "energy",
                "size" : !variables ? null : variables.energy.value,
                "perc" : !variables ? null : variables.energy.percentage,
                "color" : "#4191d5",
                "ord" : 1
            },
            {
                "name" : "primary_goods",
                "size" : !variables ? null : variables.primary_goods.value,
                "perc" : !variables ? null : variables.primary_goods.percentage,
                "color" : "#559dd9",
                "ord" : 2
            },
            {
                "name" : "manufactures",
                "size" : !variables ? null : variables.manufactures.value,
                "perc" : !variables ? null : variables.manufactures.percentage,
                "color" : "#6baade",
                "ord" : 3
            },
             {
                "name" : "services",
                "size" : !variables ? null : variables.services.value,
                "perc" : !variables ? null : variables.services.percentage,
                "color" : "#80b6e3",
                "ord" : 4
            },
            {
                "name" : "investments",
                "size" : !variables ? null : variables.investments.value,
                "perc" : !variables ? null : variables.investments.percentage,
                "color" : "#95c2e7",
                "ord" : 5

            }
            ]
        },{
            "name" : "military_global",
            "color" : "#669900",
            "size" : !variables ? null : variables.military_global.value,
            "perc" : !variables ? null : variables.military_global.percentage,
            "ord" : 2,
            "children": [{
                    "name" : "troops",
                    "size" : !variables ? null : variables.troops.value,
                    "perc" : !variables ? null : variables.troops.percentage,
                    "color" : "#76a318",
                    "ord" : 1
                },{
                    "name" : "military_equipment",
                    "size" : !variables ? null : variables.military_equipment.value,
                    "perc" : !variables ? null : variables.military_equipment.percentage,
                    "color" : "#85ad33",
                    "ord" : 2

                }]
        },{
            "name" : "soft_global",
            "color" : "#ff9000",
            "size" : !variables ? null : variables.soft_global.value,
            "perc" : !variables ? null : variables.soft_global.percentage,
            "ord" : 3,
            "children": [{
                    "name" : "migrations",
                    "size" : !variables ? null : variables.migrations.value,
                    "perc" : !variables ? null : variables.migrations.percentage,
                    "color" : "#ff960d",
                    "ord" : 1
                },{
                    "name" : "tourism",
                    "size" : !variables ? null : variables.tourism.value,
                    "perc" : !variables ? null : variables.tourism.percentage,
                    "color" : "#ff9b1a",
                    "ord" : 2
                },{
                    "name" : "sports",
                    "size" : !variables ? null : variables.sports.value,
                    "perc" : !variables ? null : variables.sports.percentage,
                    "color" : "#ffa126",
                    "ord" : 3
                },{
                    "name" : "culture",
                    "size" : !variables ? null : variables.culture.value,
                    "perc" : !variables ? null : variables.culture.percentage,
                    "color": "#ffa633",
                    "ord" : 4
                },{
                    "name" : "information",
                    "size" : !variables ? null : variables.information.value,
                    "perc" : !variables ? null : variables.information.percentage,
                    "color" : "#ffac40",
                    "ord" : 5
                },{
                    "name" : "technology",
                    "size" : !variables ? null : variables.technology.value,
                    "perc" : !variables ? null : variables.technology.percentage,
                    "color" : "#ffb24d",
                    "ord" : 6
                 },{
                    "name" : "science",
                    "size" : !variables ? null : variables.science.value,
                    "perc" : !variables ? null : variables.science.percentage,
                    "color" : "#ffb759",
                    "ord" : 7
                },{
                    "name" : "education",
                    "size" : !variables ? null : variables.education.value,
                    "perc" : !variables ? null : variables.education.percentage,
                    "color" : "#ffbc66",
                    "ord" : 8
                },{
                    "name" : "cooperation",
                    "size" : !variables ? null : variables.cooperation.value,
                    "perc" : !variables ? null : variables.cooperation.percentage,
                    "color" : "#ffc273",
                    "ord" : 9
                }]
        }

        ]
    };


    this.get = function(){
    	return this.data;
    };

    this.findElementInTree = function (el){
    	return this._findElementInTree(this.data,el);
    };

    this._findElementInTree = function(tree,el){
    	 if (tree.name == el){
            return tree;
        }

        if (!tree.hasOwnProperty("children")){
            return null;
        }
        for (var i=0;i<tree.children.length;i++){
            var found = this._findElementInTree(tree.children[i],el);
            if (found){
                return found;
            }

        }
        return null;
    }

    this.findParentInTreeByName = function(name){
        if (name == "global"){
            return null;
        }
        // Find at second level
        for(var i=0;i<this.data.children.length;i++){
            if (this.data.children[i].name == name){
                return this.data.name;
            }
        }

        // Find at third level
        for(var i=0;i<this.data.children.length;i++){
            for (var j=0;j<this.data.children[i].children.length;j++){
                if (this.data.children[i].children[j].name == name){
                    return this.data.children[i].name;
                }
            }
        }
        
    }

    return this;

};
