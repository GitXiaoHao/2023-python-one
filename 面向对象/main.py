#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：2023-python-one 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：小豪
@Date    ：2023/9/21 11:11 
"""
import random
from math import sqrt
from time import sleep


class Washer:
    __name: object = None

    def __init__(self) -> None:
        super().__init__()
        print("init")

    def wash(self):
        print(self.__name)


class Animal:
    name: str

    def __init__(self) -> None:
        super().__init__()
        print("animal")
        self.name = "animal"

    def pri(self):
        print("animal", self.name)


class School:
    name: str

    def __init__(self) -> None:
        super().__init__()
        print("school")
        self.name = 'school'

    @classmethod
    def pri(cls):
        print("school", cls.name)


class Pig(Animal, School):

    def __init__(self) -> None:
        print("pig")
        super().__init__()


if __name__ == '__main__':
    pig: Animal = Pig()
    # school
    # animal
    # animal animal
    pig.pri()
    print(Pig.__mro__)