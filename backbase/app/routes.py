# from flask import render_template
from app import app
from app.controller import userController, paymentController,loanController
from flask import request


@app.route('/user', methods=['POST','GET'])
def users():
    if request.method == 'GET':
        return userController.index()
    elif request.method == 'POST':
        return userController.store()
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
    


@app.route('/loan', methods=['POST','GET'])
def loan():
    if request.method == 'GET':
        return loanController.index()
    elif request.method == 'POST':
        return loanController.store()
    else:
        return loanController.store()

@app.route('/loan/<int:loan_id>', methods=['PUT', 'GET', 'DELETE'])
def loanDetail(loan_id):
    if request.method == 'GET':
        return loanController.show(loan_id)
    elif request.method == 'PUT':
        return loanController.update(loan_id)
    elif request.method == 'DELETE':
        return loanController.delete(loan_id)


@app.route('/payment', methods=['GET', 'POST'])
def payments():
    if request.method == 'GET':
        return paymentController.index()
    elif request.method == 'POST':
        return paymentController.store()
    else:
        return paymentController.store()

@app.route('/payment/<int:payment_id>', methods=['GET', 'PUT', 'DELETE'])
def paymentDetail(payment_id):
    if request.method == 'GET':
        return paymentController.show(payment_id)
    elif request.method == 'PUT':
        return paymentController.update(payment_id)
    elif request.method == 'DELETE':
        return paymentController.delete(payment_id)






    

