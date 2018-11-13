import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
UPLOAD_DIR = os.path.join(os.path.join(STATIC_DIR, 'media'), 'upload')


MYSQL_DATABASES = {
    'DRIVER': 'mysql',
    'DH': 'pymysql',
    'ROOT': 'root',
    'PASSWORD': 'root',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'NAME': 'ihome',
}