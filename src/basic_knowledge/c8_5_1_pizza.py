#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_5_1_pizza.py
@Time: 2019/5/12 23:50
@Desc: 结合使用位置实参和任意数量的实参
"""


def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print('-' + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
