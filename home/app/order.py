# -*- coding: utf-8 -*-
# @File  : order.py
# @Author: KingJX
# @Date  : 2018/10/15 10:19
""""""
from datetime import datetime

from flask import Blueprint, request, session, render_template, jsonify

import status_code
from app.models import User, Facility, Area, House, HouseImage, Order

order = Blueprint('order', __name__)


@order.route('/orders/', methods=['GET'])
def show():
    return render_template('orders.html')


@order.route('/orders/', methods=['POST'])
def orders_post():
    house_id = request.form.get('house_id')
    begin_date = datetime.strptime(request.form.get('begin_date'), '%Y-%m-%d')
    end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
    house = House.query.get(house_id)
    order = Order()
    order.house_id = house_id
    order.user_id = session['user_id']
    order.begin_date = begin_date
    order.end_date = end_date
    order.days = (end_date - begin_date).days + 1
    order.house_price = house.price
    order.amount = order.house_price * order.days
    order.add_update()
    return jsonify(status_code.SUCCESS)


@order.route('/my_orders/', methods=['GET'])
def orders_get():
    orders = Order.query.filter(Order.user_id == session['user_id'])
    orders_info = [order.to_dict() for order in orders]
    return jsonify(code=status_code.ok, orders_info=orders_info)

