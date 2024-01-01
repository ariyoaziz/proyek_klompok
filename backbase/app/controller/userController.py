from app.model.user import User
from app import response, app, db
from flask import request

def index():
    try:
        users = User.query.all()
        data = transform(users)
        return response.ok(data, "success")
    except Exception as e:
        print(e)

def transform(users):
    array = []
    for i in users:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email,
            'phone': i.phone
        })
    return array

def show(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Empty....')

        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def singleTransform(user):
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'phone': user.phone
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

        return response.ok('', 'Successfully create data!')
    except Exception as e:
        print(e)

def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        password = request.json['password']

        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Empty....')

        user.name = name
        user.email = email
        user.phone = phone
        user.setPassword(password)

        db.session.commit()

        return response.ok('', 'Successfully update data!')
    except Exception as e:
        print(e)

def delete(id):
    try:
        user = User.query.filter_by(id=id).first()

        if not user:
            return response.badRequest([], 'Empty...')

        db.session.delete(user)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)

def login():
    try:
        email = request.json['email']
        password = request.json['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Empty....')

        if not user.checkPassword(password):
            return response.badRequest([], 'Invalid credentials')

        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)

