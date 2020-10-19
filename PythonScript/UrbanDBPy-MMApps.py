# -*- coding: utf-8 -*-
"""
Created on 

@author: MMApps
@contact: mehboob_dev@mmappps.in
@ProjectName: UrbanDBCrossPlatform-MMApps
Contact for Getting Subscription. Many More Method on Way..!!
"""

import requests
import os

API = "OCBwZCu41n"
SheetName = "Sheet1"
#Enter Your API Key.

def requestURL():
    return "https://urbandb-mmapps.herokuapp.com/"+API+"/"+SheetName

def getAllRows():
    """

    Returns
    -------
    JSON
        IT WILL RETURN COMPLETE SHETE IN A JSON FORMAT.

    """
    return requests.get(requestURL()+"/getAllRows").json()

def getRow(rowIndex):
    """

    Parameters
    ----------
    rowIndex : INT
        PASS THE INDEX OF ROW OF WHICH YOU REQUIRED DATA.

    Returns
    -------
    JSON
        IT WILL RETURN THE ROW AT THE ENTERED INDEX IN JSON FORMAT.
        
    """
    return requests.get(requestURL()+"/getRow/"+str(rowIndex+1)).json()

def getColumn(columnIndex):
    """

    Parameters
    ----------
    columnIndex : INT
         PASS THE INDEX OF COLUMN OF WHICH YOU REQUIRED DATA.

    Returns
    -------
    JSON
        IT WILL RETURN ROW DATA AT THE ENTERED INDEX IN JSON FORMAT.

    """
    return requests.get(requestURL()+"/getColumn/"+str(columnIndex)).json()

def getCell(rowIndex, columnIndex):
    """
    Parameters
    ----------
    rowIndex : INT
        PASS THE INDEX OF ROW OF WHICH YOU REQUIRED DATA.
        .
    columnIndex : INT
        PASS THE INDEX OF COLUMN OF WHICH YOU REQUIRED DATA.

    Returns
    -------
    STRING
        IT WILL RETURN THE CELL VALUE FROM THE ENTERED CORDINATES

    """
    cellAddress=str(1+1)+"/"+str(1)
    return requests.get(requestURL()+"/getCell/"+cellAddress).json()

def getHeader():
    """

    Returns
    -------
    LIST
        IT WILL RETURN HEADER IN A LIST FORMAT

    """
    return requests.get(requestURL()+"/getHeader").json()
    
def appendRow(rowData):
    """

    Parameters
    ----------
    rowData : STRING
        EXAMPLE ("THIS,IS,A,SAMPLE,STRING")
        ENTER THE STRING WITH COMMA SEPRETED STYLE WITH INCERTED COMMA AT START AND END.

    Returns : 
    -------
    JSON
        IT WILL RETURN INFORMATION WITH CORDINATES OF UPLOADED DATA.

    """
    return requests.get(requestURL()+"/appendRow/"+str(', '.join(rowData.split(",")))).json()

def appendRows(rowsData):
    """

    Parameters
    ----------
    rowsData : STRING
        EXAMPLE ("THIS,IS,A,SAMPLE,STRING>>P,Y,T,H,O,N>>I,S>>P,O,W,E,R")
        ENTER THE STRING WITH COMMA SEPRETED STYLE WITH INCERTED COMMA AT START AND ENDFOR EACH ROW.
        SEPERATE ROW USING >>

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return requests.get(requestURL()+"/appendRows/"+str(', '.join(rowsData.split(",")))).json()

def upload_file(filepath):
    """

    Parameters
    ----------
    filepath : STRING
        ENTER THE FILE LOCATION.

    Returns
    -------
    JSON
        RETURN THE MESSAGE WHEATHER UPLOAD IS SUCESSFUL OR NOT.

    """
    payload = {}
    files = [
      ('file', open(filepath,'rb'))
    ]
    headers= {}
    response = requests.request("POST", requestURL()+"/file-upload", headers=headers, data = payload, files = files)
    return response.text#.encode('utf8')

def download_file(filename, downloadpath=""):
    """

    Parameters
    ----------
    filename : STRING
        ENTER THE FILE NAME DURING UPLOAD.
    downloadpath : PATH, optional
        PATH TO DOWNLOAD LOCATION, DO NOT PASS ANY VALUE IF YOU WANT TO DOWNLOAD ON ROOT DIRECTORY OF CODE. The default is "".

    Returns
    -------
    None.

    """
    reqfile = requests.get(requestURL()+"/getupload/"+str(filename)).url
    response=requests.get(reqfile)
    with open(os.path.join(downloadpath,reqfile.split("/")[-1]), 'wb') as f:
        f.write(response.content)
    print("Download Done")
    
# print(getAllRows())
# print(getRow(1))
# print(getColumn(1))
# print(getCell(1, 1))
# print(appendRow("p,y,t,h,o,n"))
# print(getHeader())
# appendRows("p,y,t,h,o,n>>i,s>>p,o,w,e,r")
# jj=upload_file("PathToMediaFile")
aa = download_file(4642)#.text