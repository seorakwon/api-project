#!/usr/bin/env python

from bottle import route, run, get, post, request
import random
from mongo1 import CollConection
import bson
from bson.json_util import dumps
from populate import db, coll
import json
import requests
import pandas as pd
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from functools import reduce
from sklearn.feature_extraction.text import CountVectorizer

# get the whole database
@get("/")
def index():
    return dumps(coll.find())

#get the info per username, it will return all their texts
@get("/<username>")
def demo2(username):
    return dumps(coll.find({'userName':username},{'userName':1, 'idUser':1, 'text':1, '_id':0}))

# get all the conversation lines per chat
@get("/chat/<chat_id>/list")
def get_chat(chat_id):
    return dumps(coll.find({"idChat":int(chat_id)},{'_id':0, 'idChat':1, 'userName':1, 'text':1}))

#get chat sentiment per chat(you can get the sentiment per line of conversation and the compound and average)
@get('/chat/<chat_id>/sentiment')
def getSentiment(chat_id):
    query = list(coll.find({'idChat':int(chat_id)}, {"userName":1,"idUser":1,"text": 1,"_id":0}))
    sid = SentimentIntensityAnalyzer()
    total_info=[]
    for text in query:
        info={}
        info["userName"]=text["userName"]
        info["idChat"]=int(chat_id)
        info["text"]=text["text"]
        info["sentiment"]=sid.polarity_scores(text["text"])
        total_info.append(info)
    #return dumps(total_info)
    comp_sent = [s['sentiment']['compound'] for s in total_info]
    avg = reduce((lambda x, y: x+y), comp_sent)/len(comp_sent)
    return dumps({"Sentiments": total_info,
                  "compound sentiments": comp_sent,
                  "avg sentiment [-1,1]": avg})



# create sole user
@post('/user/create')
def newUser():
    name = request.forms.get("name")
    new_id = coll.distinct("idUser")[-1] + 1
    new_user = {
        "idUser": new_id,
        "participants": name
    }
    coll.insert_one(new_user)
    print("{} added to collection with id {}".format(name,new_id))


# add new user with message to new chat
@post('/adduser')
def addUserProfile():
    idUser = coll.distinct("idUser")[-1] + 1
    name = request.forms.get("userName")
    idMessage = coll.distinct("idMessage")[-1] + 1
    idChat = coll.distinct("idChat")[-1] + 1
    text = (request.forms.get("text"))
    document={"idUser":idUser,
            "userName":name,
            "idMessage":idMessage,
            "idChat":idChat,
            "text":text}
    coll.insert_one(document)
    print("New user added to collection")

# create new chat
@post('/chat/create')
def newChat():
    name = request.forms.get("name")
    new_id = coll.distinct("idChat")[-1] + 1
    new_user = {
        "idChat": new_id,
        "participants": name
    }
    coll.insert_one(new_user)
    print("{} added to collection with id {}".format(name,new_id))


# Adds user to existing chat with their text
@post('/chat/<idChat>/adduser')
def chatUser(idChat):
    idUser  = coll.distinct("idUser")[-1] + 1
    name = str(request.forms.get("userName"))
    idMessage = coll.distinct("idMessage")[-1] + 1
    idChat = int(idChat)
    text = str(request.forms.get("text"))
    document={"idUser":idUser,
            "userName":name,
            "idMessage":idMessage,
            "idChat":idChat,
            "text":text
            }
    coll.insert_one(document)
    print("New user added to chat{}".format(idChat))

# Add message to existing conversation
@post("/chat/<chat_id>/addmessage")
def addMessage(chat_id):
    new_idMessage = coll.distinct("idMessage")[-1] + 1
    idUser = int(request.forms.get("idUser"))
    message = str(request.forms.get("text"))
    fields = list(coll.find({"idUser":idUser},{"userName":1, "idUser":1, "_id":0,"idChat":1}))
    print(fields)
    name = fields[0]["userName"]
    for f in fields:
        if f["userName"] == name:
            new_idUser = f["idUser"]
        else:
            name = name
    new_message = {
        "idUser" : idUser,
        "userName" : name,
        "idChat" : int(chat_id),
        "idMessage" : new_idMessage,
        "text" : message
    }
    print(new_message)
    new_user = {
        "idUser" : new_idUser,
        "userName" : name
    }
    print(new_user)
    coll.insert_one(new_message)


# trying to start on the recommendation, but gives error
@get('/user/<user_id>/recommend')
def getRecomm(userName):
    req = list(coll.find({'userName': userName},{"text":1,'_id':0}))
    return req

run(host='localhost', port=8080, debug=True)




