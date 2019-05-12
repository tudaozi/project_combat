#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_4_greet_users.py
@Time: 2019/5/12 16:36
@Desc: 传递列表
"""


def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + '!'
        print(msg)


user_names = ['hannah', 'ty', 'margot']
greet_users(user_names)
