#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "lx"

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.services import admin_service
from src.services import teacher_service
from src.services import student_service
from src.services import initialize_service



def show_role():
    msg = '''
    
\033[1;31m___ 选课系统 ___\033[0m
    
    0：初始化
    1：管理员
    2：老师
    3：学生
    4：退出'''
    print(msg)


if __name__ == '__main__':
    role_main = {
        '0':initialize_service.main,
        '1':admin_service.login,
        '2':teacher_service.main,
        '3':student_service.main,
        '4':exit
    }
    while True:
        show_role()
        choice = input('请输入角色:').strip()
        if choice not in role_main:continue
        role_main[choice]()



