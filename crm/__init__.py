from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from models import Lead, Touch

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from crm import routes