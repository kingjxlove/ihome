
from functools import wraps

from flask import session, render_template

from app.models import db
from utils.settings import MYSQL_DATABASES


def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        try:
            a = session['user_id']
            return func(*args, **kwargs)
        except:
            return render_template('login.html')
    return check_login


def init_ext(app):
    db.init_app(app)
    # sess = Session()
    # sess.init_app(app)


def get_mysqldb_url():

    DRIVER = MYSQL_DATABASES['DRIVER']
    DH = MYSQL_DATABASES['DH']
    ROOT = MYSQL_DATABASES['ROOT']
    PASSWORD = MYSQL_DATABASES['PASSWORD']
    HOST = MYSQL_DATABASES['HOST']
    PORT = MYSQL_DATABASES['PORT']
    NAME = MYSQL_DATABASES['NAME']
    return '{}+{}://{}:{}@{}:{}/{}'.format(DRIVER, DH, ROOT,
                                           PASSWORD, HOST, PORT, NAME)