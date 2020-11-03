# -*- coding: utf-8 -*-
"""
Created on

@author: MMApps
@contact: mehboob_dev@mmappps.in
@ProjectName: UrbanDBCrossPlatform-MMApps
Contact for Getting Subscription. Many More Method on Way..!!
"""

from flask import Flask, request, redirect, render_template
import requests as req

app = Flask(__name__)
API = "OCBwZCu41n"#Enter API Here
SHEETNAME = "Sheet1"#Enter your Sheet Name Here

@app.route("/")
def homepage():
    return render_template("index.html")

def request_url():
    """

    Returns
    -------
    URL
        INTERNAL FUNCTION.

    """
    return "https://urbandb-mmapps.herokuapp.com/"+API+"/"+SHEETNAME

def append_row(rowdata):
    """

    Parameters
    ----------
    rowdata : STRING
        EXAMPLE ("THIS,IS,A,SAMPLE,STRING")
        ENTER THE STRING WITH COMMA SEPRETED STYLE WITH INCERTED COMMA AT START AND END.

    Returns :
    -------
    JSON
        IT WILL RETURN INFORMATION WITH CORDINATES OF UPLOADED DATA.

    """
    return req.get(request_url()+"/appendRow/"+str(', '.join(rowdata.split(","))))#.json()

@app.route('/connect.html', methods = ['POST'])
def connect():
    connectformdata = request.form
    temp = ""
    for key in connectformdata:
        temp=temp+connectformdata[key]+","
    append_row(temp[0:-1])
    return redirect('/')

if __name__ ==  "__main__":
    app.run(debug=True, use_reloader=False)