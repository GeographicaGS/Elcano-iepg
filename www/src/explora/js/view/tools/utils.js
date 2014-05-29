app.view.tools.utils.variablesTree = function(variables){
	this.data = {
        "name" : "iepg",
        "color" : "#fdc300",
        "size" : variables.iepg.value,
        "children" : [{
            "name" : "economic_presence",
            "color" : "#2b85d0",
            "size" : variables.economic_presence.value,
            "children": [{
                "name" : "energy",
                "size" : variables.energy.value,
                "color" : "#4191d5"
            },
            {
                "name" : "primary_goods",
                "size" : variables.primary_goods.value,
                "color" : "#559dd9"
            },
            {
                "name" : "manufactures",
                "size" : variables.manufactures.value,
                "color" : "#6baade"
            },
             {
                "name" : "services",
                "size" : variables.services.value,
                "color" : "#80b6e3"
            },
            {
                "name" : "investments",
                "size" : variables.investments.value,
                "color" : "#95c2e7"
            }
            ]
        },{
            "name" : "military_presence",
            "color" : "#669900",
            "size" : variables.military_presence.value,
            "children": [{
                    "name" : "troops",
                    "size" : variables.troops.value,
                    "color" : "#76a318"
                },{
                    "name" : "military_equipment",
                    "size" : variables.military_equipment.value,
                    "color" : "#85ad33"

                }]
        },{
            "name" : "soft_presence",
            "color" : "#ff9000",
            "size" : variables.soft_presence.value,
            "children": [{
                    "name" : "migrations",
                    "size" : variables.migrations.value,
                    "color" : "#ff960d",
                },{
                    "name" : "tourism",
                    "size" : variables.tourism.value,
                    "color" : "#ff9b1a"
                },{
                    "name" : "sports",
                    "size" : variables.sports.value,
                    "color" : "#ffa126"
                },{
                    "name" : "culture",
                    "size" : variables.culture.value,
                    "color": "#ffa633"
                },{
                    "name" : "information",
                    "size" : variables.information.value,
                    "color" : "#ffac40"
                },{
                    "name" : "technology",
                    "size" : variables.technology.value,
                    "color" : "#ffb24d"
                 },{
                    "name" : "science",
                    "size" : variables.science.value,
                    "color" : "#ffb759"
                },{
                    "name" : "education",
                    "size" : variables.education.value,
                    "color" : "#ffbc66"
                },{
                    "name" : "cooperation",
                    "size" : variables.cooperation.value,
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