#!/usr/bin/env python
# -*- coding:utf-8 -*-
dog_cal = 140
bun_cal = 120
mus_cal = 20
ket_cal = 80
onion_cal = 40
print ("\tDog\tBun\tKetchup\tMustard\tOnions\tCalories")
count = 1
for dog in [0,1]:
    for bun in [0,1]:
        for ketchup in [0,1]:
            for mustard in [0,1]:
                for onions in [0,1]:
                    total_cal = (bun * bun_cal)+(dog * dog_cal)+ \
                       (ketchup * ket_cal)+(mustard * mus_cal)+ \
                           (onions * onion_cal)
                    print "#",count,"\t",
                    print dog,"\t",bun,"\t",ketchup,"\t",
                    print mustard,"\t",onions,
                    print "\t",total_cal

                    count = count + 1
#dog_cal = 140
#bun_cal = 120
#mus_cal = 20
#ket_cal = 80
#onion_cal = 40
#print (",Dog,Bun,Ketchup,Mustard,Onions,Calories")
#count = 1
#for dog in [0,1]:
#    for bun in [0,1]:
#        for ketchup in [0,1]:
#            for mustard in [0,1]:
#                for onions in [0,1]:
#		    total_cal = (bun * bun_cal)+(dog * dog_cal)+ \
#			(ketchup * ket_cal)+(mustard * mus_cal)+ \
#			    (onions * onion_cal)
#                    print "#",count,",",
#                    print dog,",",bun,",",ketchup,",",
#                    print mustard,",",onions,
#		    print ",",total_cal
#                    count = count + 1
