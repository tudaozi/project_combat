#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_1_1_greeter.py
@Time: 2019/5/11 15:50
@Desc: 向函数传递信息--实参和形参
"""


def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")


greet_user("jesse")
greet_user("sarah")
