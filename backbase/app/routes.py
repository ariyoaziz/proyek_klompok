# from flask import render_template
from app import app
from app.controller import userController
from flask import request

@app.route("/user")
def users():
    return userController.index()


def usersDetail(id):
    print(id)
    return userController.show(id)
