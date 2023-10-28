from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class Student(db.Model):
    __tablename__ = 'student'
    studentId = db.Column(db.Integer, primary_key=True)
    fname =  db.Column(db.String, nullable=False, unique=True)
    lname = db.Column(db.String, nullable=False)
    karma_score = db.Column(db.Integer, nullable=False)
    reviewlist = db.relationship('Review', backref='student')

    def __init__(self, username, password):
        self.studentId = studentId
        self.fname = fname
        self.lname = lname
        self.karma_score = karma_score

    def __repr__(self):
        return f'<Student "{self.fname} , {self.lname}">'

    

    
        