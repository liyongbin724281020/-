#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "lx"

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)


from models import Score
from models import Admin
from models import School
from models import Teacher
from models import Course
from models import Classes
from models import Student
from models import Course_to_teacher





def create_school():
    try:
        name = input('请输入学校名字:').strip()
        addr = input('请输入学校地址:').strip()
        school_name_list = [(obj.name,obj.addr) for obj in School.get_all_obj_list()]
        if (name,addr) in school_name_list:
            raise Exception('\033[43;1m[%s] [%s]校区已经存在，不可重复创建，你有那么多学生吗？\033[0m' % (name,addr))
        obj = School(name,addr)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m[%s] [%s]校区创建成功\033[0m' % (obj.name,obj.addr)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status':status,'error':error,'data':data}

def show_school():
    for obj in School.get_all_obj_list():
        print('\033[45;1m学校[%s] 地址[%s] 创建日期[%s]\033[0m'.center(60,'-') \
              %(obj.name,obj.addr,obj.create_time))

def create_teacher():
    try:
        name = input('请输入老师姓名:').strip()
        password = input('请输入登陆密码:').strip()
        level = input('请输入老师级别:').strip()
        teacher_name_list = [obj.name for obj in Teacher.get_all_obj_list()]
        if name in teacher_name_list:
            raise Exception('\033[43;1m老师[%s] 已存在，不可重复创建\033[0m' % name)
        obj = Teacher(name,password,level)
        obj.save()
        status = True
        error = ''
        data ='\033[33;1m老师[%s] 级别[%s] 时间[%s] 创建成功 \033[0m' % (obj.name,obj.level,obj.create_time)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status':status,'error':error,'data':data}

def show_teacher():
    for obj in Teacher.get_all_obj_list():
        print('\033[33;1m老师[%s] 级别[%s] 录取时间[%s]\033[0m'.center(60,'-')\
              %(obj.name,obj.level,obj.create_time))

def create_course():
    try:
        print('创建课程'.center(60,'-'))
        school_list = School.get_all_obj_list()
        for k,obj in enumerate(school_list):
            print(k,obj,obj.addr)
        sid = int(input('请选择学校:'))
        school_obj = school_list[sid]

        name = input('请输入课程名:').strip()
        price = input('请输入课程价格:').strip()
        period = input('请输入课程周期:').strip()

        course_name_list = [(obj.name,obj.school_nid.uuid) for obj in Course.get_all_obj_list()]
        if (name,school_obj.nid.uuid) in course_name_list:
            raise Exception('\033[43;1m课程[%s] 已存在，不可重复创建\033[0m' % name)
        obj = Course(name,price,period,school_obj.nid)
        obj.save()
        status = True
        error =''
        data = '\033[33;1m课程[%s] 价格[%s] 周期[%s] 创建成功\033[0m' % (obj.name,obj.price,obj.period)
    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status':status,'error':error,'data':data}

def show_course():
    for obj in Course.get_all_obj_list():
        print('\033[33;1m[%s] [%s]校区 [%s]课程 价格[%s] 周期[%s]\033[0m'.center(60,'-') % (obj.school_nid.get_obj_by_uuid().name,obj.school_nid.get_obj_by_uuid().addr,obj.name,obj.price,obj.period))

def create_course_to_teacher():


    print('课程导师'.center(60, '='))
    course_list = Course.get_all_obj_list()
    for k, obj in enumerate(course_list):
        print(k, obj, obj.name)
    sid = int(input('请选择课程: '))
    course_obj = course_list[sid]

    teacher_list = Teacher.get_all_obj_list()
    for k, obj in enumerate(teacher_list):
        print(k, obj, obj.name)
    sid = int(input('请选择关联导师: '))
    teacher_obj = teacher_list[sid]

    classes_list = Classes.get_all_obj_list()
    for k, obj in enumerate(classes_list):
        print(k, obj, obj.name)
    sid = int(input('请选择负责班级: '))
    classes_obj = classes_list[sid]

    obj = Course_to_teacher(course_obj.nid,teacher_obj.nid,classes_obj.nid)
    obj.save()
    status = True
    error = ''
    data = '\033[33;1m课程[%s] 班级[%s] 导师[%s] 分配成功\033[0m' % (course_obj.name, classes_obj.name, teacher_obj.name)
    return {'status': status, 'error': error, 'data': data}


def create_classes():
    try:
        print('创建班级'.center(60, '-'))
        course_list = Course.get_all_obj_list()
        for k, obj in enumerate(course_list):
            print(k, obj, obj.name)
        sid = int(input('请选择课程:'))
        course_obj = course_list[sid]
        name = input('请输入班级名:').strip()
        tuition = input('请输入学费:').strip()

        classes_name_list = [obj.name for obj in Classes.get_all_obj_list()]
        if name in classes_name_list:
            raise Exception('\033[43;1m班级[%s] 已存在，不可重复创建\033[0m' % name)
        obj = Classes(name, tuition, course_obj.nid)
        obj.save()
        status = True
        error = ''
        data = '\033[33;1m班级[%s] 学费[%s] 创建成功\033[0m' % (obj.name, obj.tuition)

    except Exception as e:
        status = False
        error = str(e)
        data = ''
    return {'status': status, 'error': error, 'data': data}


def show_classes():
    for obj in Classes.get_all_obj_list():
        print('\033[33;1m [%s]课程 班级[%s] 学费[%s]\033[0m'.center(60,'-') \
              %(obj.course_nid.get_obj_by_uuid().name,obj.name,obj.tuition))


def create_student():

    print('新生入学'.center(60, '-'))
    classes_list = Classes.get_all_obj_list()
    for k, obj in enumerate(classes_list):
        print(k, obj, obj.name)
    sid = int(input('请选择班级:'))
    classes_obj = classes_list[sid]

    name = input('请输入学生姓名:').strip()
    password = input('请输入登陆密码:').strip()
    age = input('请输入学生年龄:').strip()
    qq = input('请输入学生QQ:').strip()
    score_obj = Score(0)
    score_obj.save()
    obj = Student(name,password,age,qq,classes_obj.nid,score_obj.nid)
    obj.save()
    status = True
    error = ''
    data ='\033[33;1m学生[%s] age[%s] QQ[%s] 录取成功 \033[0m' % (obj.name,obj.age,obj.qq)

    return {'status':status,'error':error,'data':data}


def show_student():
    for obj in Student.get_all_obj_list():
        print('\033[33;1m学生[%s] age[%s] QQ[%s]\033[0m'.center(60,'-')\
              %(obj.name,obj.age,obj.qq))


def show():
    msg = '''
        0：选项
        1：创建学校
        2：查看学校
        3：创建老师
        4：查看老师
        5：创建课程
        6：查看课程
        7：关联老师与课程
        8：创建班级
        9：查看班级
        10：创建学生
        11：查看学生
            return 返回上一级
        '''
    print(msg)


def main():
    choice_dic = {
        '0':show,
        '1':create_school,
        '2':show_school,
        '3':create_teacher,
        '4':show_teacher,
        '5':create_course,
        '6':show_course,
        '7':create_course_to_teacher,
        '8':create_classes,
        '9':show_classes,
        '10':create_student,
        '11':show_student,
    }
    while True:
        show()
        choice = input('请输入选项:').strip()
        if choice not in choice_dic and choice != 'return':
            continue
        elif choice == 'return':
            break
        else:
            ret = choice_dic[choice]()
            if ret:
                if ret['status']:
                    print(ret['data'].center(60,'-'))
                else:
                    print(ret['error'].center(60, '-'))


def login():
    ret = Admin.login()
    if ret:
        if ret['status']:
            print(ret['data'].center(60,'-'))
            main()
        else:
            print(ret['error'].center(60,'-'))

