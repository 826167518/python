#!/usr/bin/env python
# -*- coding:utf-8 -*-


c = raw_input("Wich nultiplication table would you like: \n")
s = raw_input("How high do you want to go: \n")
print "Here's your table:"
for i in range (1,int(s)+1):
    print c,"x",i,"=",i * int(c)



#c = raw_input("Wich nultiplication table would you like: \n")
#s = raw_input("How high do you want to go: \n")
#print "Here's your table:"
#i = 1
#while i <= int(s):
#    print c,"x",i,"=",i * int(c)
#    i += 1
