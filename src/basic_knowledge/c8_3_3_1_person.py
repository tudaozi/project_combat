#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_3_3_person.py
@Time: 2019/5/11 23:05
@Desc: 返回字典
"""


def buil_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = buil_person('jimi', 'hendrix', age='12')
print(musician)
