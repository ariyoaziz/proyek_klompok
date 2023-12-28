# from flask import render_template
from app import app
from app.controller import userController
from flask import request


@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return userController.index()
    else:
        return userController.store()

@app.route('/user/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return userController.show(id)
    elif request.method == 'PUT':
        return userController.update(id)
    elif request.method == 'DELETE':
        return userController.delete(id)


