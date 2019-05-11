#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: e8_7_make_album.py
@Time: 2019/5/12 1:31
@Desc: 编辑
"""


def make_album(name, album):
    album_dictionary = {name.title(): album.title()}
    return album_dictionary


star_album = make_album('liuzhipeng', 'pingan')
print(star_album)
star_album = make_album('liuhaoran', 'kuaile')
print(star_album)
star_album = make_album('guojiefang', 'shushi')
print(star_album)
