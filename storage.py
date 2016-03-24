# -*- coding:utf-8 -*-
__author__ = 'calculusma'

import redis
from json import dumps

r = redis.Redis(host='localhost',decode_responses=True)
class session:
    @staticmethod
    def set(key,value):
        try:
            assert r.set(str(key),str(value)) == True
            return dumps({"result":"ok"})
        except AssertionError:
            return dumps({"result":"error"})

    @staticmethod
    def get(key):
        value = r.get(key)
        if isinstance(value,unicode):
            value.encode("utf-8")
        return value