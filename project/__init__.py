from flask import Flask
from flask_mail import Mail
from gmail_config import MAIL_USERNAME, MAIL_PASSWORD, SECRET_KEY
from pymongo import MongoClient

# set config mail server
DEBUG = True
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = MAIL_USERNAME
MAIL_PASSWORD = MAIL_PASSWORD
MAIL_DEFAULT_SENDER = MAIL_USERNAME
SECRET_KEY = SECRET_KEY

#initiate application
app = Flask(__name__)

#initiate config
app.config.from_object(__name__)

#initialize mail: note after config set
mail = Mail(app)

#initialize views
from project import views

#initiate MONGODB
client = MongoClient()

