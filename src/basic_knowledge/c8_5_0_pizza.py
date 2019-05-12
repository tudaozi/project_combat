#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_5_0_pizza.py
@Time: 2019/5/12 23:38
@Desc: 传递任意数量的实参--使用循环遍历toppings
"""


def make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
