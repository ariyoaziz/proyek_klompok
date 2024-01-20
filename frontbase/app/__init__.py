from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "e5a90bab05538f57d6a4f2d230f07b08"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'peminjaman_db'

mysql = MySQL(app)
bcrypt = Bcrypt(app)

from app import routes

# from app import routes