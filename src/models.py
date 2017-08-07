#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "lx"


import time
import pickle
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
from src import identifier


SCORE_DB_DIR = os.path.join(BASE_DIR,'src','services','score','score')

class BaseModel:
    def save(self):
        file_path = os.path.join(self.db_path,str(self.nid))
        pickle.dump(self,open(file_path,'wb'))

    @classmethod
    def get_all_obj_list(cls):
        ret = []
        for filename in os.listdir(cls.db_path):
            file_path = os.path.join(cls.db_path,filename)
            ret.append(pickle.load(open(file_path,'rb')))
        return ret


class Admin(BaseModel):
    db_path = settings.ADMIN_DB_DIR
    def __init__(self,username,password):
        self.nid = identifier.AdminNid(self.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')

    @staticmethod
    def login():
        try:
            name = input('请输入用户名:').strip()
            pas = input('请输入密码:').strip()
            for obj in Admin.get_all_obj_list():
                if obj.username == name and obj.password == pas:
                    status = True
                    error = ''
                    data = '\033[45;1m登陆成功\033[0m'
                    break
                else:
                    raise Exception('\033[43;1m用户名或密码错误\033[0m' %name)
        except Exception as e:
            status = False
            error = str(e)
            data = ''
        return {'status':status,'error':error,'data':data}


class School(BaseModel):
    db_path = settings.SCHOOL_DB_DIR
    def __init__(self,name,addr):
        self.nid = identifier.SchoolNid(self.db_path)
        self.name = name
        self.addr = addr
        self.create_time = time.strftime('%Y-%m-%d %X')


class Teacher(BaseModel):
    db_path = settings.TEACHER_DB_DIR
    def __init__(self,name,password,level):
        self.nid = identifier.TeacherNid(self.db_path)
        self.name = name
        self.password = password
        self.level = level
        self.__account = 0
        self.create_time = time.strftime('%Y-%m-%d %X')



class Course(BaseModel):
    db_path = settings.COURSE_DB_DIR
    def __init__(self,name,price,period,school_nid):
        self.nid = identifier.CourseNid(self.db_path)
        self.name = name
        self.price = price
        self.period = period
        self.school_nid = school_nid


class Course_to_teacher(BaseModel):
    db_path = settings.COURSE_TO_TEACHER_DB_DIR
    def __init__(self,course_nid,teacher_nid,classes_nid):
        self.nid = identifier.Course_to_teacherNid(self.db_path)
        self.course_nid = course_nid
        self.teacher_nid = teacher_nid
        self.classes_nid = classes_nid

    def get_course_to_teacher_list(self):
        ret = self.get_all_obj_list()
        if ret:
            return [ret.course_nid.get_obj_by_uuid(),ret.classes_nid.get_obj_by_uuid()]
        return [None,None]


class Classes(BaseModel):
    db_path = settings.CLASSES_DB_DIR
    def __init__(self,name,tuition,course_nid):
        self.nid = identifier.ClassesNid(self.db_path)
        self.name = name
        self.tuition = tuition
        self.course_nid = course_nid


class Score(BaseModel):
    db_path = settings.SCORE_DB_DIR
    def __init__(self,score):
        self.nid = identifier.ScoreNid(self.db_path)
        self.score = score


class Student(BaseModel):
    db_path = settings.STUDENT_DB_DIR
    def __init__(self,name,password,age,qq,classes_nid,score_nid):
        self.nid = identifier.StudentNid(self.db_path)
        self.name = name
        self.password = password
        self.age = age
        self.qq = qq
        self.classes_nid = classes_nid
        self.score_nid = score_nid




