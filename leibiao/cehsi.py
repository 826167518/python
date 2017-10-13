#!/usr/bin/env python
#! -*-coding:utf-8 -*-


#letters = []
#letters.append("Tony")
#letters.append("Paul")
#letters.append("Nick")
#letters.append("Michel")
#letters.append("Kevin")
#s = ''
#for i in letters:
#    s = s + ' ' + i
#print "The names are",s


#####python3.0####
#letters = []
#letters.append("Tony")
#letters.append("Paul")
#letters.append("Nick")
#letters.append("Michel")
#letters.append("Kevin")
#s = ''
#for i in letters:
#    s = s + ' ' +i
#print ("The names are",s)





letters = []
letters.append("Tony")
letters.append("Paul")
letters.append("Nick")
letters.append("Michel")
letters.append("Kevin")
print "Enter 5 names:"
for i in letters:
    print i
print "The names are",' '.join(letters)
tem = int(raw_input("Replace one name. Which one? (1-5):"))
if tem <= len(letters) and tem > 0:
    name = raw_input("New name: ")
    letters[tem-1] = name
    print "The names are",' '.join(letters)
else:
    print "输入错误!"

#####python3.0####
#letters = []
#letters.append("Tony")
#letters.append("Paul")
#letters.append("Nick")
#letters.append("Michel")
#letters.append("Kevin")
#print ("Enter 5 names:")
#for i in letters:
#    print(i)
#print("The names are",' '.join(letters))
#tem = int(input("Replace one name. Which one?(1-5): "))
#if tem <= len(letters) and tem > 0:
#    name = input("New name:")
#    letters[tem-1] = name
#    print("The names atr",' '.join(letters))
#else:
#    print("输入错误!")

