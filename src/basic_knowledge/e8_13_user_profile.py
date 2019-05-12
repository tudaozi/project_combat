#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_5_2_user_profile.py
@Time: 2019/5/13 0:04
@Desc: 使用任意数量的关键字实参
"""


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile


user_profile = build_profile('liu', 'zhipeng', xingbie='nan', zhuzhi='guangdong')
print(user_profile)
