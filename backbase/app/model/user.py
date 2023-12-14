from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, chek_password_hash


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    phone= db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.name)
    
def setPassword(self,password):
    self.password = generate_password_hash(password)

def checkPassword(self,password):
    return chek_password_hash(self.password,password)