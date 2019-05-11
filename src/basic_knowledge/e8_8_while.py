#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: e8_8_while.py
@Time: 2019/5/12 1:42
@Desc: 用户的编辑
"""


def make_album(name, album):
    album_dictionary = {name.title(): album.title()}
    return album_dictionary


while True:
    print('\nPlease input star name and star album')
    s_name = input('Star Name: ')
    if s_name == 'q':
        break
    s_album = input('Star Album: ')
    if s_album == 'q':
        break

    star_album = make_album(s_name, s_album)
    print(star_album)
