# -*- coding: utf-8 -*-
"""
Created on

@author: MMApps
@contact: mehboob_dev@mmappps.in
@ProjectName: UrbanDBCrossPlatform-MMApps
Contact for Getting Subscription. Many More Method on Way..!!
"""

from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import requests as req

app = Flask(__name__)
API = "OCBwZCu41n"#Enter API Here
SHEETNAME = "Sheet1"#Enter your Sheet Name Here

def request_url():
    """

    Returns
    -------
    URL
        INTERNAL FUNCTION.

    """
    return "https://urbandb-mmapps.herokuapp.com/"+API+"/"+SHEETNAME

@app.route('/', methods=("POST", "GET"))
def getData():
    df = pd.DataFrame(req.get(request_url()+"/getAllRows").json())
    return render_template('index.html',  tables=[df.to_html(X`='data')], titles=df.columns.values)

if __name__ ==  "__main__":
    app.run(debug=True, use_reloader=False)