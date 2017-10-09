#!/usr/bin/env python
# -*- coding:utf-8 -*-


#numStars = int(raw_input ("How many stars do you want? "))
#for i in range (1, numStars + 1):
#    print '*',

#####python3.x####
#numStars = int(input("How many stars do you want? "))
#for i in range (1,numStars + 1):
#    print ('*',end=' ')




#numBlocks = int(raw_input('How many blocks of stars do you want? '))
#numLines = int(raw_input('How many lines of stars do you want? '))
#numStars = int(raw_input('How mant stars per line? '))
#for block in range(0,numBlocks):
#    for line in range(0, numLines):
#        for star in range(0,numStars):
#	    print '*',
#        print
#    print

#####python3.x####
#numBlocks = int(input('How many blocks of stars do you want? '))
#numLines = int(input('How many lines of stars do you want? '))
#numStars = int(input('How mant stars per line? '))
#for block in range(0,numBlocks):
#    for line in range(0,numLines):
#        for star in range(0,numStars):
#	    peint ('*',end=' ')
#        print()
#    print()




numBlocks = int(raw_input('How many blocks of stars do you want? '))
for block in range(1,numBlocks +1):
    for line in range(1,block * 2):
	for star in range(1,(block + line) * 2):
	    print '*',
	print ' line = ',line,'star = ',star
    print


#####python3.x####
#numBlocks = int(input('How many blocks of stars do you want? '))
#for block in range(1,numBlocks +1):
#    for line in range(1,block * 2):
#	for star in range(1,(block + line) * 2):
#	    print('*',end=' ')
#	print(' line = ',line,'star = ',star)
#    print()
