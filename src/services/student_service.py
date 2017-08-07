#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "lx"

import os,sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from models import Score
from models import Student


def login():
    while True:
        student_name = input('请输入姓名:').strip()
        student_password = input('请输入登陆密码:').strip()
        students_list = Student.get_all_obj_list()
        for obj in students_list:
            if student_name == obj.name and student_password == obj.password:
                return obj
        choice = input('登陆失败！是否重试？(y:是  n:否)').strip()
        if choice == 'y':
            continue
        elif choice == 'n':
            return 'fail'


def info(obj):
    print('学生信息'.center(60,' '))
    print('\033[33;1m学生[%s] age[%s] QQ[%s]\033[0m'.center(60, '-') \
          % (obj.name, obj.age, obj.qq))


def score(obj):
    print('学生成绩'.center(60,' '))
    print('\033[33;1m学生[%s] score[%s]\033[0m'.center(60, '-') \
          % (obj.name, obj.score_nid.get_obj_by_uuid().score))


def action(obj):
    print('''
    1、查询学生信息
    2、查询成绩
        return 返回上一级''')
    action_dict = {
        '1':info,
        '2':score
    }
    while True:
        choice = input('>>>').strip()
        if choice in action_dict:
            action_dict[choice](obj)
            input()
        elif choice == 'return':
            break
        else:
            print('No this choice..')
            continue


def main():
    print('学生界面'.center(60,'-'))
    obj = login()
    if obj == 'fail':
        print('登陆失败！!')
    else:
        action(obj)