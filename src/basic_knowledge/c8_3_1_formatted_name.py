#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_3_1_formatted_name.py
@Time: 2019/5/11 20:11
@Desc: 返回值--调用返回值的函数时，需要提供一个变量，用于存储返回的值。
"""


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
