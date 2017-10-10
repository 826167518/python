#!/usr/bin/env python
# -*- coding:utf-8 -*-
y = float(raw_input("您的邮箱多大L: "))
m = float(raw_input("您还剩多少油%: "))
s = float(raw_input("汽车每升可以走多远km： "))

#h= (m + 5) * s
h= y * (m / 100)  * s
print (h)
if h >= 200:
 #   print("Size of tank: ",s,"\n" )
    print "Size of tank: ",y,  "\n", "percent full: ", m, "\n", "km per liter: ", s, "\n",  "You can go another " , h, "km" , "\n", "The next gas station is 200 km away" , "\n" , "You can wait for the next station."
else:
    print "Size of tank: ", y , "\n",  "percent full: ", m, "\n", "km per liter: ", s, "\n",  "You can go another ",h, "km","\n", "The next gas station is 200 km away", "\n", "You must be at this station!"

