#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: basic_knowledge
@File: c8_2_2_pets.py
@Time: 2019/5/11 16:35
@Desc: 传递实参--关键字实参，位置已经不重要，可以调换位置顺序，因为已经将实参赋值给对应的形参，输出结果是一样的。
"""


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("my " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")
