# coding=UTF8

"""

IEPG Calculation Engine service.

"""
from backend import app
from backend.utils import auth
from flask import request, session, send_file
from common.config import backend
import hashlib
import time
import os
from common.flux import Flux


@app.route("/iepgengine", methods=["POST"])
@auth
def iepgengine():
    """Recieves an Excel file and launches the IEPG calculation. Returns
    an Excel with the results."""
    
    file = request.files["file"]

    if file is not None and file.filename.rsplit(".",1)[1] in ["xlsx","XLSX"]:
        filename = hashlib.md5(str(time.time())+session["email"]).hexdigest()
        path_filename = os.path.join(backend["tmpFolder"], filename+".xlsx")
        outFileName = os.path.join(backend["tmpFolder"],
                                   hashlib.md5(str(time.time())+session["email"]+"outputIEPGEngine").hexdigest()+ \
                                   ".xlsx")
        file.save(path_filename)
        flux = Flux()
        flux.calculusFromXLSXToXLSX(path_filename,outFileName)

        return(send_file(outFileName, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                     attachment_filename="Real_Instituto_Elcano-Calculo_IEPG.xlsx",
                     as_attachment=True))

    else:
        return jsonify({"Error": "Bad file."})


