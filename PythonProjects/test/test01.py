#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
class A():

    def __init__(self):

     if __name__ == '__main__':
        print('入口')
        self.b('1111')


     def a(self, ip):
        print(ip)

     def b(self, ip):
        self.a(ip)

a = A()
# class A():
#     i = '123'
#
#     def __init__(self):
#         self.f
#
#     def f(self):
#         print('hello world')
#
#
# a = A()
