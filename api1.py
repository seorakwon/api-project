#!/usr/bin/env python

from bottle import route, run, get, post, request
import random
from mongo1 import CollConection
import bson
from bson.json_util import dumps
from populate import db, coll
import json
import requests


@get("/")
def index():
    return dumps(coll.find())

@get("/<username>")
def demo2(username):
    return dumps(coll.find({'userName':username},{'userName':1, 'idUser':1, 'text':1, '_id':0}))


@get("/chat/<chat_id>/list")
def get_chat(chat_id):
    return dumps(coll.find({"idChat":int(chat_id)},{'_id':0, 'idChat':1, 'userName':1, 'text':1}))

# create sole user
@post('/user/create')
def newUser():
    name = str(request.forms.get("name"))
    new_id = coll.distinct("idUser")[-1] + 1
    new_user = {
        "idUser": new_id,
        "participants": name
    }
    coll.insert_one(new_user)
    print(f"{name} added to collection with id {new_id}")


# add new user with message to new chat
@post('/adduser')
def addUserProfile():
    idUser = coll.distinct("idUser")[-1] + 1
    name = str(request.forms.get("userName"))
    idMessage = coll.distinct("idMessage")[-1] + 1
    idChat = coll.distinct("idChat")[-1] + 1
    text = str(request.forms.get("text"))
    document={"idUser":idUser,
            "userName":name,
            "idMessage":idMessage,
            "idChat":idChat,
            "text":text}

    coll.insert_one(document)
    print("New user added to collection")

@post('/chat/create')
def newChat():
    users = request.forms.getlist('user_id')
    return {
        'chat_id':str(db.createChat(users))}


# Adds user to existing chat with their text
@post('/chat/<chat_id>/adduser')
def addUserToChat(idChat):
    idUser = coll.distinct("idUser")[-1] + 1
    name = str(request.forms.get("userName"))
    idMessage = coll.distinct("idMessage")[-1] + 1
    idChat = int(idChat)
    text = str(request.forms.get("text"))
    document = {"idUser":idUser,
            "userName":name,
            "idMessage":idMessage,
            "idChat":idChat,
            "text":text}
    coll.insert_one(document)
    print("New user added to chat{}".format(idChat))

@post('/chat/<chat_id>/addmessage')
def newChatMessage():
    name = str(request.forms.get("name"))
    new_id = coll.distinct("idUser")[-1] + 1
    new_idmessage = coll.distinct("idMessage")[-1] + 1
    new_chat = coll.distinct("idChat")[-1] + 1
    datetime= str(request.forms.get("datetime"))
    text = str(request.forms.get("text"))
    new_user = {
        "idUser": new_id,
        "userName": name,
        "idMessage": new_idmessage,
        "idChat": new_chat,
        "datatime": datetime,
        "text": text
    }
    coll.insert_one(new_user)
    print("{} added to collection with id {}".format(name, new_id))


#coll=CollConection('conversation','chats')
run(host='localhost', port=8080, debug=True)




