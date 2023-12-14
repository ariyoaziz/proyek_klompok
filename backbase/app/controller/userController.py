from app.model.user import User
from app import response, app,db
from flask import request


def index():
    try:
        user = User.query.all()
        data = transfrom (user)
        return response.ok (data, "success")
    except Exception as e:
        print (e)

def transfrom(users):
    array = []
    for i in users:
        array.append({
            'id' : i.id,
            'name' : i.name,
            'email' : i. email,
            'phone' : i.phone
        })
    return array

def show(id):
    try:
        users = User.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([],'Empty....')
        
        data = singleTransfrom(users)
        return response.ok(data,"")
    except Exception as e:
        print(e)

def singleTransfrom(users):
    data ={
        'id' : users.id,
        'name' : users.name,
        'email' : users.email,
        'phone' : users.phone
    }

    return data

def stord():
    try:
        name = request.json['name']