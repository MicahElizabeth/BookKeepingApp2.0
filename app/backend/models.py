import datetime
import hashlib

from server import db, ma, lm
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy import events

# MODELS AKA database stuff
string_maximum = 255

#needs optimization for example, add message ids, and question ids to reduce repeated strings
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(100), unique=False)
    last_name = db.Column(db.String(100), unique=False)
    password_hash = db.Column(db.String(1000), unique=False)
    role = db.Column(db.String(120), default="user")

    def __init__(self, uid=0, email="", first_name="", last_name="", password="", role=""):
        self.uid = uid
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password_hash = self.set_password(password)

        if role:
            self.role = role

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True  # If it's assigned to here, they are authenticated.

    def is_anonymous(self):
        return False

# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
#     message = db.Column(db.String(120), default="")
#     timeStamp = db.Column(db.DateTime, default=datetime.datetime.now) #could be used for read time
#     pushTime = db.Column(db.DateTime, default=datetime.datetime.now)
#     read = db.Column(db.Integer, default = 0) #0 for unread 1 for web read
#         #(later can change fro mobile read)
#     def mark_read(self):
#         self.read = 1
#         return True
#     def is_read(self):
#         return self.read == 1
#
# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
#     question = db.Column(db.String(120), default="")
#     qtype = db.Column(db.String(15), default ="text")
#     timeStamp = db.Column(db.DateTime, default=datetime.datetime.now) #could be used for read time
#     pushTime = db.Column(db.DateTime, default=datetime.datetime.now)
#     read = db.Column(db.Integer, default = 0) #0 for unread 1 for web read
#
# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     qid = db.Column(db.Integer, db.ForeignKey('question.id')) #only one answer per question
#     response = db.Column(db.String(120), default="")
#     timeComplete = db.Column(db.DateTime, default=datetime.datetime.now)

@lm.user_loader
def user_loader(id):
    user = db.session.query(User).filter_by(id=id).first()

    if user is None:
        return

    return user


@lm.unauthorized_handler
def unauthorized_handler():
    return '<h1>UNAUTHORIZED</h1>'

#schema
class UserSchema(ModelSchema):
    class Meta:
        fields = ('uid', 'email', 'first_name', 'last_name')
# class MessageSchema(ModelSchema):
#     class Meta:
#         fields = ('uid','message', 'timeStamp', 'pushTime', 'read')
# class QuestionSchema(ModelSchema):
#     class Meta:
#         fields = ('uid', 'id', 'question', 'qtype', 'timeStamp', 'pushTime', 'read')
# class AnswerSchema(ModelSchema):
#     class Meta:
#         fields = ('qid', 'response', 'timeComplete')
