from explora import app
from flask import jsonify,request,make_response

@app.route('/quotes/<string:family>/<string:variable>/<string:countries>/<string:lang>', methods=['GET'])
def quotes(family,variable,countries,lang):
    
    response = [
    	{
    		"year" : 1990,
    		"values" : [
    			{
    				"country" : "ES",
    				"value" :  130.0
    			},
    			{
    				"country" : "FR",
    				"value" :  180.0
    			},
    			{
    				"country" : "US",
    				"value" :  470.0
    			}
    		]
    	},
    	{
    		"year" : 1995,
    		"values" : [
    			{
    				"country" : "ES",
    				"value" :  135.0
    			},
    			{
    				"country" : "FR",
    				"value" :  185.0
    			},
    			{
    				"country" : "US",
    				"value" :  475.0
    			}
    		]
    	},
    	{
    		"year" : 2000,
    		"values" : [
    			{
    				"country" : "ES",
    				"value" :  140.0
    			},
    			{
    				"country" : "FR",
    				"value" :  190.0
    			},
    			{
    				"country" : "US",
    				"value" :  480.0
    			}
    		]
    	},
    	{
    		"year" : 2005,
    		"values" : [
    			{
    				"country" : "ES",
    				"value" :  145.0
    			},
    			{
    				"country" : "FR",
    				"value" :  195.0
    			},
    			{
    				"country" : "US",
    				"value" :  485.0
    			}
    		]
    	},
    	{
    		"year" : 2010,
    		"values" : [
    			{
    				"country" : "ES",
    				"value" :  150.0
    			},
    			{
    				"country" : "FR",
    				"value" :  200.0
    			},
    			{
    				"country" : "US",
    				"value" :  500.0
    			}
    		]
    	},
    	{
    		"year" : 2013,
    		"values" : [
    			{
    				"country" : "ES",
    				"value" :  155.0
    			},
    			{
    				"country" : "FR",
    				"value" :  205.0
    			},
    			{
    				"country" : "US",
    				"value" :  505.0
    			}
    		]
    	}
    ]
    
    return jsonify({"results": response })
    