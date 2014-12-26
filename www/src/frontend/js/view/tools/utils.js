app.view.tools.utils.variablesTree = function(){
	this.data = {
		"key":"iepg",
        "name" : "iepg",
        "children" : [{
        	"key":"economic_global",
            "name" : "economic_presence",
            "children": [{
            	"key":"energy",
                "name" : "energy",
            },
            {
            	"key":"primary_goods",
                "name" : "primary_goods",
            },
            {
            	"key":"manufactures",
                "name" : "manufactures",
            },
             {
            	"key":"services",
                "name" : "services",
            },
            {
            	"key":"investments",
                "name" : "investments",
            }
            ]
        },{
        	"key":"military_global",
            "name" : "military_presence",
            "children": [{
            		"key":"troops",
                    "name" : "troops",
                },{
                	"key":"military_equipment",
                    "name" : "military_equipment",
                }]
        },{
        	"key":"soft_global",
            "name" : "soft_presence",
            "children": [{
            	"key":"migrations",
                    "name" : "migrations",
                },{
                	"key":"tourism",
                    "name" : "tourism",
                },{
                	"key":"sports",
                    "name" : "sports",
                },{
                	"key":"culture",
                    "name" : "culture",
                },{
                	"key":"information",
                    "name" : "information",
                },{
                	"key":"technology",
                    "name" : "technology",
                 },{
                	"key":"science",
                    "name" : "science",
                },{
                	"key":"education",
                    "name" : "education",
                },{
                	"key":"cooperation",
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