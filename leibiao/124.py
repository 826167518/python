#!/usr/bin/env python
# -*- coding:utf-8 -*-

#friends = []
#friends.append('David')
#friends.append('Mary')
#print friends


letters=['a','2','a','b','c']
#'a' in letters
#letters.remove('a')
#print letters
#tmp = ['a','b','c']
tmp = raw_input().split()
for i in range(len(tmp)):
    if tmp[i] in letters:
	print "found %s in letters"%tmp[i]
    else:
	print "didn't find %s in letters"%tmp[i]
