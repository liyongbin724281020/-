#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "lx"
import os,sys
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from models import Score
from models import Teacher
from models import Student
from models import Course_to_teacher



SCORE_DB_DIR = os.path.join(BASE_DIR,'services','score','score')

def class_info(teacher_nid):
    '''查看班级信息'''
    classes_list = []
    for obj in Course_to_teacher.get_all_obj_list():
        if obj.teacher_nid.get_obj_by_uuid().name == teacher_nid.get_obj_by_uuid().name:
            obj = obj.classes_nid
            classes_list.append(obj.get_obj_by_uuid())
    return classes_list


def student_info(teacher_nid):
    '''查看学生信息'''
    classes_list = []
    student_list = []
    num = 0
    classes_lists = class_info(teacher_nid)
    for obj in classes_lists:
        classes_list.append(obj.name)
    for obj in Student.get_all_obj_list():
        if obj.classes_nid.get_obj_by_uuid().name in classes_list:
            student_list.append(obj)
            score_list = Score.get_all_obj_list()
            for objs in score_list:
                if str(objs.nid) == str(obj.score_nid):
                    print('\033[33;1m%s、学生[%s] age[%s] QQ[%s] 成绩[%s]\033[0m'.center(60, '-') \
                          % (num,obj.name, obj.age, obj.qq, objs.score))
                    break
    return student_list


def set_student_score(teacher_nid):
    '''设置学生分数'''

    print('set student')
    student_list = student_info(teacher_nid)
    choice = int(input('请选择学生:').strip())
    number = float(input('请输入分数:').strip())
    obj = Score(number)
    obj.save()
    student_list[choice].score_nid = obj.nid
    student_list[choice].save()
    print('------成绩设置成功------')


def action(obj):
    num = 0
    to_list = Course_to_teacher.get_all_obj_list()
    for to_obj in to_list:
        if to_obj.teacher_nid.get_obj_by_uuid().name == obj.name:
            teacher_nid = to_obj.teacher_nid
    while True:
        print('\n\033[1;31m____Teacher %s____\033[0m\n'%teacher_nid.get_obj_by_uuid().name)
        print('    1、查看班级信息\n    2、查看学生信息\n    3、设置学生分数\n    4、退出')
        choice = str(input('>>>').strip())
        if choice == '1':
            classes_list = class_info(teacher_nid)
            for obj in classes_list:
                print('\033[33;1m %s、课程[%s] 班级[%s] 学费[%s]\033[0m'.center(60, '-') \
                      % (num, obj.course_nid.get_obj_by_uuid().name, obj.name,
                         obj.tuition))
                num += 1
            input()
        elif choice == '2':
            student_info(teacher_nid)
            input()
        elif choice == '3':
            set_student_score(teacher_nid)
            input()
        elif choice == '4':
            break
        else:continue


def main():
    print('教师界面'.center(60, '-'))
    obj = login()
    if obj == 'fail':
        print('登陆失败！!')
    else:
        action(obj)


def login():
    while True:
        teacher_name = input('请输入姓名:').strip()
        teacher_password = input('请输入登陆密码:').strip()
        teacher_list = Teacher.get_all_obj_list()
        for obj in teacher_list:
            if teacher_name == obj.name and teacher_password == obj.password:
                return obj
        choice = input('登陆失败！是否重试？(y:是  n:否)').strip()
        if choice == 'y':
            continue
        elif choice == 'n':
            return 'fail'