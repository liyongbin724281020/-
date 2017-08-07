#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = "lx"


import uuid,hashlib
import time

def create_uuid():
    return str(uuid.uuid1())


def create_md5():
    md = hashlib.md5()
    md.update(bytes(str(time.time()),encoding='utf-8'))
    return md.hexdigest

