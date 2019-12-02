#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import json
import os

def getCollection():
    collection = input('Insert desired collection: ')
    return collection

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = "mongodb+srv://seorakwon:{}@cluster0-rxtil.mongodb.net/test?retryWrites=true&w=majority".format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

collection = getCollection()

db, coll = connectCollection('conversation', collection)


