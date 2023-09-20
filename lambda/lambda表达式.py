#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：2023-python-one 
@File    ：lambda表达式.py
@IDE     ：PyCharm 
@Author  ：小豪
@Date    ：2023/9/20 20:51 
"""

if __name__ == '__main__':
    students = [
        {'name': 'tom', 'age': 20},
        {'name': 'kk', 'age': 19},
        {'name': 'des', 'age': 200},
        {'name': 'rose', 'age': 201},
        {'name': 'jack', 'age': 241}
    ]
    students.sort(key=lambda x: x['age'], reverse=True)
    print(students)
