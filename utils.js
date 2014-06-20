app.view.tools.utils.variablesTree = function(){
	this.data = {
        "name" : "iepg",
        "children" : [{
            "name" : "economic_presence",
            "children": [{
                "name" : "energy",
            },
            {
                "name" : "primary_goods",
            },
            {
                "name" : "manufactures",
            },
             {
                "name" : "services",
            },
            {
                "name" : "investments",
            }
            ]
        },{
            "name" : "military_presence",
            "children": [{
                    "name" : "troops",
                },{
                    "name" : "military_equipment",
                }]
        },{
            "name" : "soft_presence",
            "children": [{
                    "name" : "migrations",
                },{
                    "name" : "tourism",
                },{
                    "name" : "sports",
                },{
                    "name" : "culture",
                },{
                    "name" : "information",
                },{
                    "name" : "technology",
                 },{
                    "name" : "science",
                },{
                    "name" : "education",
                },{
                    "name" : "cooperation",
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
