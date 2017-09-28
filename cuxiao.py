#!/usr/bin/env python
# -*- coding:utf-8 -*-
j = float(raw_input("购买总金额为: "))
if j > 10:
    z = j * 0.8
    print "折后金额为: ",z,"元"
else:
    z = j * 0.9
    print "折后金额为: ",z,"元"



##### python 3.0 ####
#j = float(input("购买总金额为："))
#if j > 10:
#    z = j * 0.8
#    print("折后价为：",z,"元")
#else:
#    z = j * 0.9
#    print("折后价为：",z,"元")
