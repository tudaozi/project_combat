#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: e8_12_sandwich.py
@Time: 2019/5/13 0:45
@Desc: 三明治
"""


def sandwich(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping.title())


sandwich('qingcan')
sandwich('qingcai', 'wuhuarou')
sandwich('qingqing', 'wuhuarou', 'naolao')
