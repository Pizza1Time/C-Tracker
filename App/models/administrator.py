from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class Administrator(User):
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.user_type = "admin"

    def add_student(self, fname, lname):
        try:
            student = Student(owner.id, game.gameId, condition, price)
            db.session.add(...)
            db.session.commit()
            return listing
        except Exception as e:
            print('error creating ...', e)
            db.session.rollback()
            return None
    

