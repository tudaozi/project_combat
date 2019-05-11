#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_3_2_formatted_name.py
@Time: 2019/5/11 20:20
@Desc: 返回值--让实参变成可选的,可以给对应的可选形参赋值为空
"""


def get_formatted_name(first_name, last_name, middle_name=" "):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("john", "lee", "hooker")
print(musician)
musician = get_formatted_name("john", "hooker")
print(musician)
