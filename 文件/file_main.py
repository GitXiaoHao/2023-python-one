#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：2023-python-one 
@File    ：file_main.py
@IDE     ：PyCharm 
@Author  ：小豪
@Date    ：2023/9/20 21:12 
"""

if __name__ == '__main__':
    with open("1.txt", mode='r+') as f:
        res = f.readlines()
        f.write("6646")
        print(res)
