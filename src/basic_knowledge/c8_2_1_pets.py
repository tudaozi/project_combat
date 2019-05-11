#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_2_1_pets.py
@Time: 2019/5/11 16:35
@Desc: 传递实参--位置实参,位置顺序很重要，需要将实参对应形参的位置，避免出现错误
"""


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("my " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")
describe_pet("dog", "willie")
describe_pet("harry", "hamster")  # 位置实参顺序调换，结构将是出乎意料的
