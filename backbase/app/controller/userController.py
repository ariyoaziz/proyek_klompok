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

def store():
    try:
        id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        password = request.json['password']

        user = User(id=id, name=name, email=email, phone=phone)
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()

        return response.ok('', 'Successfully Create data!')
    
    except Exception as e:
        print(e)

def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        password = request.json['password']

        users = User.query.filter_by(id=id).first()
        users.name = name
        users.email = email
        users.phone = phone

        users.setPassword(password)
        
        db.session.commit()

        return response.ok ('', 'Successfully update data!')
    
    except Exception as e:
        print(e)

def delete (id):
    try:
        user = User.query.filter_by(id=id).first()

        if not user:
            return response.badRequest([], 'Empty...')

        db.session.delete(user)
        db.session.commit()

        return response.ok ('', 'Successfully delete data!')
    
    except Exception as e:
        print(e)
























