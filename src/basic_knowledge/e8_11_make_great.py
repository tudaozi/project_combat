#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: e8_9_show_magicians.py
@Time: 2019/5/12 21:04
@Desc: 不变的魔法师
"""

# TODO(STAURL.COM): 此处描写注释文字

list_magician = ['liuzhipeng', 'guojiefang', 'liuhaoran']


def show_magicians(list_magicians):
    for print_magicians in list_magicians:
        print('\n' + print_magicians.title())
        return print_magicians


def make_great(magicians_name, typeface='the Great'):
    for magician in magicians_name[:]:
        print('\n' + magician.title() + ' ' + typeface)
        return magicians_name


show_magicians(list_magician)

make_great(list_magician)
print(list_magician)
