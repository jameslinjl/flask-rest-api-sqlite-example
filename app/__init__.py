from flask import Flask

app = Flask(__name__)

from app import db, file_controller, views

# initial setup of db
db.db_up()
