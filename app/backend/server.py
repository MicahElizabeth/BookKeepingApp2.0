import sys

from time import sleep # Wait for the DB to be ready.

from flask import Flask, send_file, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask.ext.seasurf import SeaSurf
from werkzeug.security import generate_password_hash, check_password_hash

from flask.ext.seasurf import SeaSurf
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask.ext.sqlalchemy import SQLAlchemy  # Database management
from flask.ext.marshmallow import Marshmallow  # Data serialization

sleep(5)  # Delay is required for allowing the Database to startup


app = Flask(__name__)
app.secret_key = "ASECRETKEYGOESHERE"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://pgdbuser:pgdbpassword@db/bookkeepingdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
# csrf = SeaSurf(app)
lm = LoginManager()

from models import *

# CREATE DATABASE
db.create_all()

# INITIALIZE LOGIN MANAGEMENT
lm.init_app(app)
# ROUTES


@app.route('/api/')
def index():
    obj = {}
    obj['status'] = "running"
    print(obj, file=sys.stdout)
    return jsonify(**obj)


@app.route('/api/current_user', methods=['GET'])
def current():
    #subbject to change
    user_schema = UserSchema()

    try:
        if current_user.is_authenticated():
            result = user_schema.dump(current_user)
        else:
           return jsonify({'error': "no user logged in ... not authenticated"}), 500 #error
    except:
        return jsonify({'error': "no user logged in"}), 500 #error

    return jsonify({'result': result.data}), 200 #successful


@app.route('/api/login', methods=['POST'])
def login():
    body = request.json
    print(body)
    user = db.session.query(User).filter_by(email=body['email']).first()
    user_schema = UserSchema(many=False)

    if user is None:
        return jsonify({'error': 'could not find user'}), 500

    if user.check_password(body['password']):
        login_user(user, remember=False)
        result = user_schema.dump(current_user)
        return jsonify({'result': result})


    return jsonify({'error': 'could not find user'}), 500

# @app.route('/api/message', methods=['POST'])
# def sendMessage():
#     body = request.json
#
#     user = db.session.query(User).filter_by(uid=body['id']).first()
#
#     if user is None:
#         return jsonify({'error': 'That user does not exist'}), 500
#
#     msg = {'uid': body['id'], 'message': str(body['mess']), 'pushTime': body['pushTime']}
#     msg = Message(**msg)
#     db.session.add(msg)
#     db.session.commit()
#
#     #if user is None:
#         #return jsonify({'error': 'cuold not find id'}), 500
#
#     return jsonify({'result': str(body['mess'])}), 200
#
# @app.route('/api/readmessages', methods=['GET'])
# def checkMessages():
#     message_schema = MessageSchema(many=True)
#     try:
#         msgs = db.session.query(Message).filter_by(uid = current_user.id).all()
#         result = message_schema.dump(msgs)
#         #result['data'] = ["one", "two", "three"]
#     except:
#         s = '<h1>ERROR GET Messages </h1>'
#         return s
#
#     return jsonify({'result': result.data})
#
# @app.route('/api/question', methods=['POST'])
# def sendQuestion():
#     body = request.json
#
#     user = db.session.query(User).filter_by(uid=body['id']).first()
#
#     if user is None:
#         return jsonify({'error': 'That user does not exist'}), 500
#
#     qst = {'uid': body['id'], 'question': str(body['quest']), 'qtype': body['qtype'], 'pushTime': body['pushTime']}
#     qst = Question(**qst)
#     db.session.add(qst)
#     db.session.commit()
#
#     #if user is None:
#         #return jsonify({'error': 'cuold not find id'}), 500
#
#     return jsonify({'result': str(body['quest'])}), 200
#
# @app.route('/api/readquestions', methods=['GET'])
# def checkQuestions():
#     question_schema = QuestionSchema(many=True)
#     try:
#         qsts = db.session.query(Question).filter_by(uid = current_user.id).all()
#         result = question_schema.dump(qsts)
#         #result['data'] = ["one", "two", "three"]
#     except:
#         s = '<h1>ERROR GET Questions </h1>'
#         return s
#
#     return jsonify({'result': result.data})

@app.route('/api/logout', methods=['GET'])
def logout():
    logout_user()
    return jsonify({'result': 'successful logout'}), 200


@app.route('/api/register', methods=['POST'])
def create_user():
    # {'username': '', email: '' }
    print ("my request: ")
    print (request)

    user = User(**request.json)

    print(user)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()
        return "<h1>ERROR</h1>"

    return request.data


# Need for testing, not for production
@app.route('/api/users', methods=['GET'])
def get_users():
    """ THIS SHOULD NOT MAKE IT TO PRODUCTION """
    users_schema = UserSchema(many=True)
    result = {}
    try:
        users = db.session.query(User).all()
        result = users_schema.dump(users)
        #result['data'] = ["one", "two", "three"]
    except Exception as inst:
        s = '<h1>ERROR GET USERS .{0}. .{1}. .{2}.</h1>'.format(type(inst), inst.args, inst)
        return s

    return jsonify({'result': result.data})

# Need for testing, not for production
# @app.route('/api/messages', methods=['GET'])
# def get_messages():
#     """ THIS SHOULD NOT MAKE IT TO PRODUCTION """
#     message_schema = MessageSchema(many=True)
#     result = {}
#     try:
#         msgs = db.session.query(Message).all()
#         result = message_schema.dump(msgs)
#         #result['data'] = ["one", "two", "three"]
#     except Exception as inst:
#         s = '<h1>ERROR GET Messages .{0}. .{1}. .{2}.</h1>'.format(type(inst), inst.args, inst)
#         return s
#
#     return jsonify({'result': result.data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
