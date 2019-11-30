#!/usr/bin/python3

from pymongo import MongoClient
import getpass
import json
import sys
import os
from dotenv import load_dotenv
load_dotenv()

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = 'mongodb+srv://seorakwon:{}@cluster0-rxtil.mongodb.net/test?retryWrites=true&w=majority'.format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('conversation','chats')

query = {'idChat':0}
test_query = coll.find(query)
print(list(test_query))