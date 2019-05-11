#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_1_1_greeter.py
@Time: 2019/5/11 15:50
@Desc: S
"""


def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")


greet_user("jesse")
greet_user("sarah")
