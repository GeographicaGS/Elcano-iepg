# coding=UTF8

"""

Download section.


"""
import common.helpers as chelpers
import datacache as dc

@app.route('/download/<string:years>/<string:variables>/<string:countries>', methods=["GET"])
def getDownloadData(years, variables, countries):
    """Gets download data. Call examples:

    /download/1990,1995,2000,2005/energy@iepg,soft@iepg,military@iepg,soft@iepe,energy@iepg/EN,ES,US,GB,FR
    
    /download/1990,2000/energy@iepg,energy@iepe,iepg,iepe,military_presence@iepg,military_presence@iepe/EN,ES,US
    """

    print chelpers.getData(dc.dataSets["iepg"]
