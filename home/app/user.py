import os
import re
import random

from flask import Blueprint, render_template, request, session, jsonify
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import User, db
import status_code
from utils.functions import is_login
from utils.settings import UPLOAD_DIR

users = Blueprint('users', __name__)
login_manager = LoginManager()


@users.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        pwd = request.form.get('passwd')
        user = User.query.filter(User.phone == mobile).first()
        if not user:
            return jsonify(status_code.USER_LOGIN_EXIST)
        user_pwd = user.pwd_hash
        if check_password_hash(user_pwd, pwd):
            session['user_id'] = user.id
            return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.USER_LOGIN_PWD)


@users.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        pwd = request.form.get('passwd')
        code = request.form.get('code')
        imagecode = request.form.get('imagecode')

        if code != imagecode:
            return jsonify(status_code.USER_REGISTER_CODE)
        # 判断输入的电话号码是否合法
        if not re.match('^1[3578]\d{9}$', mobile):
            return jsonify(status_code.USER_REGISTER_PHONE)
        if len(pwd) < 6:
            return jsonify(status_code.USER_REGISTER_PWD)
        user = User.query.filter(User.phone == mobile).first()
        # 判断用户是否已存在
        if user:
            return jsonify(status_code.USER_REGISTER_EXIST)
        else:
            user = User()
            user.name = mobile
            user.phone = mobile
            user.pwd_hash = generate_password_hash(pwd)
            db.session.add(user)
            db.session.commit()
            return jsonify(status_code.SUCCESS)


@users.route('/code/', methods=['POST'])
def code():
    str_code = 'qwertyuiopasdfghjklzxcvbnm7896541230'
    code = ''
    for i in range(4):
        code += random.choice(str_code)
    return jsonify({'code': code})


@users.route('/my/', methods=['GET'])
@is_login
def my():
    if request.method == 'GET':
        return render_template('my.html')


@users.route('/my_get/', methods=['GET'])
def my_get():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    name = user.name
    phone = user.phone
    avatar = user.avatar
    return jsonify(code=status_code.ok, name=name, phone=phone, avatar=avatar)


@users.route('/profile/', methods=['GET', 'POST', 'PATCH'])
@is_login
def profile():
    if request.method == 'GET':
        return render_template('profile.html')

    if request.method == 'POST':
        icon = request.files.get('avatar')
        file_path = os.path.join(UPLOAD_DIR, icon.filename)
        icon.save(file_path)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        user.avatar = os.path.join('upload', icon.filename)
        user.add_update()
        icon = user.avatar
        return jsonify(code=200, icon=icon)


@users.route('/change_name/', methods=['POST'])
def change_name():
    name = request.form.get('name')
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    user.name = name
    user.add_update()
    return jsonify(status_code.SUCCESS)


@users.route('/pro/', methods=['GET'])
def pro():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    icon = user.avatar
    name = user.name
    return jsonify(code=status_code.ok, icon=icon, name=name)


@users.route('/auth/', methods=['GET'])
def auth():
    return render_template('auth.html')


@users.route('/auth_info/', methods=['POST'])
def auth_info():
    user_id = session['user_id']
    id_name = request.form.get('real_name')
    id_card = request.form.get('id_card')
    r = r'^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$'
    if not re.match(r, id_card):
        return jsonify(status_code.USER_AUTH_INFO)
    user = User.query.filter(User.id_card == id_card).all()
    if user:
        return jsonify(status_code.USER_AUTH_ID_EXIST)
    user = User.query.filter(User.id == user_id).first()
    user.id_name = id_name
    user.id_card = id_card
    user.add_update()
    return jsonify(status_code.SUCCESS)


@users.route('/auth_get/', methods=['GET'])
def auth_get():
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    if user.id_card:
        id_card = user.id_card
        id_name = user.id_name
        return jsonify(code=status_code.ok, id_card=id_card, id_name=id_name)
    else:
        return jsonify(code=2001)


@users.route('/logout/', methods=['GET'])
def logout():
    session.pop('user_id')
    return jsonify(code=status_code.ok)
