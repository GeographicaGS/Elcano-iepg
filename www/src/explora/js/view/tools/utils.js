app.view.tools.utils.variablesTree = function(variables){
	this.data = {
        "name" : "global",
        "color" : "#fdc300",
        "size" : variables.global.value,
        "perc" : variables.global.percentage,
        "children" : [{
            "name" : "economic_global",
            "color" : "#2b85d0",
            "size" : variables.economic_global.value,
            "perc" : variables.economic_global.percentage,
            "children": [{
                "name" : "energy",
                "size" : variables.energy.value,
                "perc" : variables.energy.percentage,
                "color" : "#4191d5"
            },
            {
                "name" : "primary_goods",
                "size" : variables.primary_goods.value,
                "perc" : variables.primary_goods.percentage,
                "color" : "#559dd9"
            },
            {
                "name" : "manufactures",
                "size" : variables.manufactures.value,
                "perc" : variables.manufactures.percentage,
                "color" : "#6baade"
            },
             {
                "name" : "services",
                "size" : variables.services.value,
                "perc" : variables.services.percentage,
                "color" : "#80b6e3"
            },
            {
                "name" : "investments",
                "size" : variables.investments.value,
                "perc" : variables.investments.percentage,
                "color" : "#95c2e7"
            }
            ]
        },{
            "name" : "military_global",
            "color" : "#669900",
            "size" : variables.military_global.value,
            "perc" : variables.military_global.percentage,
            "children": [{
                    "name" : "troops",
                    "size" : variables.troops.value,
                    "perc" : variables.troops.percentage,
                    "color" : "#76a318"
                },{
                    "name" : "military_equipment",
                    "size" : variables.military_equipment.value,
                    "perc" : variables.military_equipment.percentage,
                    "color" : "#85ad33"

                }]
        },{
            "name" : "soft_global",
            "color" : "#ff9000",
            "size" : variables.soft_global.value,
            "perc" : variables.soft_global.percentage,
            "children": [{
                    "name" : "migrations",
                    "size" : variables.migrations.value,
                    "perc" : variables.migrations.percentage,
                    "color" : "#ff960d",
                },{
                    "name" : "tourism",
                    "size" : variables.tourism.value,
                    "perc" : variables.tourism.percentage,
                    "color" : "#ff9b1a"
                },{
                    "name" : "sports",
                    "size" : variables.sports.value,
                    "perc" : variables.sports.percentage,
                    "color" : "#ffa126"
                },{
                    "name" : "culture",
                    "size" : variables.culture.value,
                    "perc" : variables.culture.percentage,
                    "color": "#ffa633"
                },{
                    "name" : "information",
                    "size" : variables.information.value,
                    "perc" : variables.information.percentage,
                    "color" : "#ffac40"
                },{
                    "name" : "technology",
                    "size" : variables.technology.value,
                    "perc" : variables.technology.percentage,
                    "color" : "#ffb24d"
                 },{
                    "name" : "science",
                    "size" : variables.science.value,
                    "perc" : variables.science.percentage,
                    "color" : "#ffb759"
                },{
                    "name" : "education",
                    "size" : variables.education.value,
                    "perc" : variables.education.percentage,
                    "color" : "#ffbc66"
                },{
                    "name" : "cooperation",
                    "size" : variables.cooperation.value,
                    "perc" : variables.cooperation.percentage,
                    "color" : "#ffc273"
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



    return this;

}