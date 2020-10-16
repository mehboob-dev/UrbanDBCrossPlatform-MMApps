# -*- coding: utf-8 -*-
"""
Created on 

@author: MMApps
@contact: mehboob_dev@mmappps.in
@ProjectName: UrbanDBCrossPlatform-MMApps
Contact for Getting SubscriptionMany More Method on Way..!!
"""

import requests

API = "OCBwZCu41n"

def getAllRows():
    """

    Returns
    -------
    JSON
        IT WILL RETURN COMPLETE SHETE IN A JSON FORMAT.

    """
    return requests.get("http://urbandb.mmapps.in/"+API+"/Sheet1/getAllRows").json()

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
    return requests.get("http://urbandb.mmapps.in/"+API+"/Sheet1/getRow/"+str(rowIndex+1)).json()

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
    return requests.get("http://urbandb.mmapps.in/"+API+"/Sheet1/getColumn/"+str(columnIndex)).json()

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
    return requests.get("http://urbandb.mmapps.in/"+API+"/Sheet1/getCell/"+cellAddress).json()

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
    return requests.get("http://urbandb.mmapps.in/"+API+"/Sheet1/appendRow/"+str(', '.join(rowData.split(",")))).json()

# print(getAllRows())
# print(getRow(1))
# print(getColumn(1))
# print(getCell(1, 1))
# print(appendRow("a,b,3,r,5,g,u"))
