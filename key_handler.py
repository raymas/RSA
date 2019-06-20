#!/usr/bin/env python3

import os
import codecs

def readFile(path):
    res = ""
    with open(path, 'r') as f:
        res = f.readlines()
    f.close()
    return res


def writeFile(path, data):
    f = None
    if type(data) == "str":
        f = codecs.open(path, "w", "utf-8-sig")
        f.write(data)
    elif type(data) == "list":
        f = open(path, "wb")
        f.write(data)
    if f != None:
        f.close()
