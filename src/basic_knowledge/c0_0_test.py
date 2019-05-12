#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c0_0_test.py
@Time: 2019/5/13 0:22
@Desc: S
"""


def build_profile(first, last):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    return profile


user_profile = build_profile('albert', 'einstein')
print(user_profile)
