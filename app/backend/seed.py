import random

from server import db
from models import *

users = []
#add db init code here (like filling the dateabase with a user or 2)
user = {"uid": '001', "email": 'mjenkins@email.com', "first_name":"micah", "last_name":"jeknins", "password":"password1"}
db.session.add(User(**user))
db.session.commit()
