# -*- coding:utf-8 -*-
__author__ = 'calculusma'

from itertools import combinations
from gevent import queue

def generate_code():
    s = "0123456789abcdefghijklmnopqrstuvwxyz"
    return combinations(s,4)

def prepare():
    q = queue.Queue()
    g = generate_code()
    for i in g:
        q.put("".join(i))
    return q
