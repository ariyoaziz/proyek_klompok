from flask import Flask
# from app.model import loan, payment,user
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.model import user,payment,loan

from app import routes  # Mengimport routes setelah inisialisasi app dan db
