#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: e8_14_car.py
@Time: 2019/5/13 0:56
@Desc: 汽车
"""


# TODO(STAURL.COM): 此处描写注释文字
def make_car(manufacturer, model, **accessories):
    buy_car = {}
    buy_car['manufacturer_attributes'] = manufacturer
    buy_car['model_attributes'] = model
    for key, value in accessories.items():
        buy_car[key] = value
    return buy_car


car = make_car('subaru', 'outback', color='blue', top_package='True')
print(car)
