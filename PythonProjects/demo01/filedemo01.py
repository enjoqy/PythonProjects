#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import codecs
import MySQLdb

# fo = codecs.open("H://JavaTmpFile//test.txt", "r+", "utf-8")
with codecs.open("H://JavaTmpFile//test.txt", "r+", "utf-8") as fo:
    str = fo.read()
    print(str)
    fo.write("你好\n")




