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

@get("/<tipo>")
def demo2(tipo):
    return dumps(coll.find({'userName':tipo}))

'''@route('/data')
def data():
    return dumps(coll.find())'''


@post('/user/create')
def newUser():
    name = str(request.forms.get("name"))
    print(name)
    new_id = coll.distinct("idUser")[-1] + 1
    print(new_id)
    new_user = {
        "idUser": new_id,
        "userName": name
    }
    print(new_user)
    coll.insert_one(new_user)
    print(f"{name} added to collection with id {new_id}")


'''nombre_nuevo = {'name': 'Paquito'}
requests.post("http://localhost:8080/user/create", data=nombre_nuevo)
'''
'''@get("/<name>")
def getName():
    return template('Hello {{name}}, how are you?', name=name)'''

'''@post('/add')
def add():
    print(dict(request.forms))
    autor=request.forms.get("autor")
    chiste=request.forms.get("chiste")  
    return {
        "inserted_doc": str(coll.addChiste(autor,chiste))}

@post('/userName')
def add_userName():
    new_user = {'name' : request.json.get('name'),'address' : request.json.get('address'),'Dept':request.json.get('Dept')}
    employee.append(new_emp)
    return {'userName' : new_user}
'''
'''@post('/add')
def process():
    userName = request.forms.get('userName')
    return {'userName' : userName}
'''


'''data = requests.get('http://localhost:8080/chiste/chiquito').json()
print(data["chiste"])
Van dos soldados en una moto y no se cae ninguno porque van soldados
In [10]:
requests.post('http://localhost:8080/add')
Out[10]:
<Response [200]>
In [9]:
url='http://localhost:8080/add'
params={'autor':'chiquito',
       'chiste':'prueba5'}'''



'''@get("/chat/<tipo>")
def demo(tipo):
    print(f"un chiste de {tipo}")
    if tipo == "chiquito":
        return {
            "chiste": "Van dos soldados en una moto y no se cae ninguno porque van soldados"
        }
    elif tipo == "eugenio":
        return {
            "chiste": "Saben aquell que diu...."
        }
    else:
        return {
            "chiste": "No puedorrr!!"
        }

@post('/add')
def add():
    print(dict(request.forms))
    autor=request.forms.get("autor")
    chiste=request.forms.get("chiste")  
    return {
        "inserted_doc": str(coll.addChiste(autor,chiste))}

'''
#coll=CollConection('conversation','chats')
run(host='localhost', port=8080)




