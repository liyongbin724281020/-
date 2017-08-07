#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "lx"



import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_DB_DIR = os.path.join(BASE_DIR,'db','admin')
SCHOOL_DB_DIR = os.path.join(BASE_DIR,'db','school')
TEACHER_DB_DIR = os.path.join(BASE_DIR,'db','teacher')
COURSE_DB_DIR = os.path.join(BASE_DIR,'db','course')
COURSE_TO_TEACHER_DB_DIR = os.path.join(BASE_DIR,'db','course_to_teacher')
CLASSES_DB_DIR = os.path.join(BASE_DIR,'db','classes')
STUDENT_DB_DIR = os.path.join(BASE_DIR,'db','student')
SCORE_DB_DIR = os.path.join(BASE_DIR,'db','score')