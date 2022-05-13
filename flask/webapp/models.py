from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from flask_login import LoginManager
from webapp import app, config

mongodb = PyMongo(app)
login = LoginManager(app)
login.login_view = 'login'

class User:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)

    @login.user_loader
    def load_user(username):
        user = mongodb.db.Users.find_one({'Name': username})
        if not user:
            return None
        return User(username=user['Name'])