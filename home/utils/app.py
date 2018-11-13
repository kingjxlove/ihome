from flask import Flask

from app.house import home
from app.order import order
from app.user import users
from utils.config import Config
from utils.functions import init_ext
from utils.settings import STATIC_DIR, TEMPLATES_DIR


def create_app():
    app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATES_DIR)

    app.config.from_object(Config)

    app.register_blueprint(blueprint=users, url_prefix='/users')
    app.register_blueprint(blueprint=home, url_prefix='/house')
    app.register_blueprint(blueprint=order, url_prefix='/order')

    init_ext(app)

    return app
