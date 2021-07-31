from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import os
import logging
import dbMongoInsert

app = Flask(__name__)

@app.route('/')
def getFun():
    x= request.args.get('arg1')
    y= request.args.get('arg2')
    ##  return render_template('intro.html')
    dbMongoInsert.insertRecord(x,y)
    return render_template('intro.html', arg1=x)

@app.route('/list')
def listFun():
    listval = dbMongoInsert.listRecords()
    return render_template('list.html', arg3= listval)

@app.route('/ind')
def indFun():
    return 'From ind Fun'

if __name__ == "__main__":
    app.run(debug=True)

