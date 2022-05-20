from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

from static.logger_config import custom_logger

db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger('gunicorn.error')
logger = custom_logger(logger)
cors = CORS()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uwdjtrurwspgbt:984e3601a1cb58943523698ef22ffcd6605a99df519a35e3e389f725983fa20b@ec2-54-165-90-230.compute-1.amazonaws.com:5432/deetubhngj2cju'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from static.todoApp.model.todo_list_model import Todo
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

    from static.todoApp import todo_list

    app.register_blueprint(todo_list, url_prefix='/api/v1')

    return app
