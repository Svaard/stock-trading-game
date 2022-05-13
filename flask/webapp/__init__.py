from flask import Flask
from webapp import config

app = Flask(__name__)
app.config["MONGO_URI"] = config.CONNECTION_STRING
app.config['SECRET_KEY'] = config.SECRET_KEY


from webapp import routes