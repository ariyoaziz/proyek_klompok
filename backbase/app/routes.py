# from flask import render_template
from app import app
from app.controller import userController, paymentController,loanController
from flask import request


@app.route('/user', methods=['POST','GET'])
def users():
    if request.method == 'GET':
        return userController.index()
    else:
        return userController.store()

@app.route('/user/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return userController.show(id)
    elif request.method == 'PUT':
        return userController.update(id)
    elif request.method == 'DELETE':
        return userController.delete(id)

# @app.route('/payment', methods=['GET', 'POST'])
# def payment():
    # if request.method == 'GET':
        # return loanController.index()
    # else:
        # return loanController.store()
    

