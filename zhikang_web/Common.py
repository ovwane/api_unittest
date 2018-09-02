# -*- coding:uft-8 -*-


def singleton(cls, *args, **kw):
    instances = {}

    def singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return singleton