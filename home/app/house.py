# -*- coding: utf-8 -*-
# @File  : views.py
# @Author: KingJX
# @Date  : 2018/7/13 12:14
""""""
import os

from flask import Blueprint, request, session, render_template, jsonify

from app.models import User, Facility, Area, House, HouseImage
import status_code
from utils.functions import is_login
from utils.settings import UPLOAD_DIR

home = Blueprint('home', __name__)


@home.route('/index/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@home.route('/myhouse/', methods=['GET', 'POST'])
def myhouse():
    return render_template('myhouse.html')


@home.route('/newhouse/', methods=['GET', 'POST'])
def newhouse():
    if request.method == 'GET':
        return render_template('newhouse.html')

    if request.method == 'POST':

        house = House()
        house.user_id = session['user_id']
        house.title = request.form.get('title')
        house.price = request.form.get('price')
        house.area_id = request.form.get('area_id')
        house.address = request.form.get('address')
        house.room_count = request.form.get('room_count')
        house.acreage = request.form.get('acreage')
        house.unit = request.form.get('unit')
        house.capacity = request.form.get('capacity')
        house.beds = request.form.get('beds')
        house.deposit = request.form.get('deposit')
        house.min_days = request.form.get('min_days')
        house.max_days = request.form.get('max_days')
        house.add_update()

        facility = request.form.getlist('facility')
        for fac in facility:
            f = Facility.query.get(fac)
            house.facilities.append(f)
            house.add_update()
        house_id = house.id
        return jsonify(code=200, house_id=house_id)


@home.route('/my_house/', methods=['GET'])
@is_login
def my_house():
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    houses = House.query.filter(House.user_id == user_id).all()
    if user.id_card:
        id = []
        title = []
        price = []
        address = []
        index_image = []
        create_time = []
        for house in houses:
            id.append(house.id)
            title.append(house.title)
            price.append(house.price)
            address.append(house.address)
            index_image.append(house.index_image_url)
            create_time.append(house.create_time)

        return jsonify(code=status_code.ok, title=title,
                       price=price, address=address, id=id,
                       index_image=index_image, create_time=create_time)
    else:
        return jsonify(status_code.HOME_NO_ID_CARD)


@home.route('/new_house/', methods=['GET'])
def new_house():
    area_id = []
    area_address = []
    area = Area.query.all()
    facility = Facility.query.all()
    fac_id = []
    fac_name = []
    for item in area:
        area_id.append(item.id)
        area_address.append(item.name)
    for item in facility:
        fac_id.append(item.id)
        fac_name.append(item.name)
    return jsonify(code=200, area_id=area_id, area_address=area_address, fac_id=fac_id, fac_name=fac_name)


@home.route('/img/', methods=['POST'])
def img():
    house_id = request.form.get('house_id')
    img = request.files.get('house_image')
    file_path = os.path.join(UPLOAD_DIR, img.filename)
    img.save(file_path)
    house = House.query.filter(House.id == house_id).first()
    house_img = HouseImage()
    house_img.url = os.path.join('upload', img.filename)
    house_img.house_id = house_id
    house_img.add_update()
    if house.index_image_url:
        imges = HouseImage.query.filter(HouseImage.house_id == house_id).all()
        imgs = []
        for item in imges:
            imgs.append(item.url)
        return jsonify(code=status_code.ok, imgs=imgs)
    else:
        house.index_image_url = os.path.join('upload', img.filename)
        house.add_update()
        imgs = []
        imgs.append(house.index_image_url)
        return jsonify(code=status_code.ok, imgs=imgs)


@home.route('/detail/', methods=['GET', 'POST'])
def detail():
    if request.method == 'GET':
        return render_template('detail.html')

    if request.method == 'POST':
        pass


@home.route('/detail_get/<int:id>/', methods=['GET'])
def detail_get(id):
    house = House.query.filter(House.id == id).first()
    house_info = house.to_full_dict()
    facilities = house.facilities
    fac = [(item.name, item.css) for item in facilities]
    user = User.query.filter(User.id == session['user_id']).first()
    user_info = [user.avatar, user.name, house.title]
    house_img = HouseImage.query.filter(HouseImage.house_id == id).all()
    img = [item.url for item in house_img]
    return jsonify(code=status_code.ok, house_info=house_info,
                   facilities=fac, user_info=user_info, img=img)


@home.route('/booking/', methods=['GET'])
def booking():
    return render_template('booking.html')


@home.route('/booking/<int:house_id>/', methods=['GET'])
def booking_get(house_id):
    house = House.query.get(house_id)
    house_info = house.to_full_dict()
    house_img = house.index_image_url
    return jsonify(code=status_code.ok, house_info=house_info, house_img=house_img)


@home.route('/index/', methods=['POST'])
def index_post():
    pass