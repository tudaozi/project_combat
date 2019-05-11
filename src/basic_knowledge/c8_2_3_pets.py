#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_2_3_pets.py
@Time: 2019/5/11 16:35
@Desc: 传递实参--默认值，在调用函数时如果给形参提供了实参，使用被提供的实参，如果没有，使用默认值。在使用默认值时，
在形参列表中必须先列出没有默认值的形参，在列出有默认值的形参。折让python依然能够正确的解读位置实参。
"""


def describe_pet(pet_name, animal_type="dog"):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("my " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name="harry")
describe_pet("willie")
describe_pet(pet_name="harry", animal_type="hamster")
