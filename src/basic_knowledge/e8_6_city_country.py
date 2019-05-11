#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: e8_6_city_country.py
@Time: 2019/5/12 1:23
@Desc: 城市名
"""


def city_country(city, country):
    cc = city + "," + country
    return cc


mcc = city_country('shenzhen', 'china')
print(mcc.title())
mcc = city_country('shanghai', 'china')
print(mcc.title())
mcc = city_country('beijing', 'china')
print(mcc.title())
