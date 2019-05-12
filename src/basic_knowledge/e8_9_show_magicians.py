#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: e8_9_show_magicians.py
@Time: 2019/5/12 21:04
@Desc: 魔法师
"""


def show_magicians(list_magicians):
    for print_magicians in list_magicians:
        print('\nThis magician name is ' + print_magicians)


list_magician = ['liuzhipeng', 'guojiefang', 'liuhaoran']
show_magicians(list_magician)
