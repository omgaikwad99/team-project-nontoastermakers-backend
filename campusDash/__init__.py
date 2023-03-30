
##importing required modules
from flask import Flask                                             
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"                                             
## naming database


def create_app():
    app = Flask(__name__)
    return app