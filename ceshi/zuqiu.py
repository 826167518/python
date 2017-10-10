#!/usr/bin/env python
# -*- conding:utf-8 -*-
x = str(raw_input("Enter sex m/f: "))
if x == "f"  or x == "F":
    n = float(raw_input("Enter age : "))
    if n >= 10 and n <= 12:
	print "Congratulations, you can join the team!!!"
    else:
	print "Unfortunately, you do not meet the requirements!"
else:
    print "Unfortunately, you do not meet the requirements!"
