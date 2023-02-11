from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from secrets import token_hex
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.apitoken = token_hex(16)
        
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
        
    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()
        
    def to_dict(self):
        return {"id": self.id, 
                "username": self.username,
                "apitoken": self.apitoken}
        
class Candy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candyName = db.Column(db.String(100), nullable=False)
    imgUrl = db.Column(db.String, nullable=False)
    description = db.Column(db.String(1000))
    price = db.Column(db.Float, nullable=False)

    def __init__(self, candyName, imgUrl, caption, price):
        self.candyName = candyName
        self.imgUrl = img_url
        self.caption = caption
        self.price = price

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
        
    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()
        
    def to_dict(self):
        return {"id": self.id, 
                "title": self.title, 
                "img_url": self.img_url, 
                "caption": self.caption, 
                "price": self.price, 
                "quantity": self.quantity}