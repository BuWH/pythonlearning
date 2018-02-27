# -*- coding: utf-8 -*-
import time, functools


def log(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('begin call')
        c=fn(*args,**kw)
        print('end call')
        return c
    print("1")
    return wrapper

@log
def printf():
    print("a")

printf()