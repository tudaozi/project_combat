#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_6_1_pizza.py
@Time: 2019/5/12 23:38
@Desc: 导入整个模块
"""


def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)
