# -*- coding:utf-8 -*-
import random
secret = random.randint(1,99)
guess = 0
tries = 0
print ("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
print ("It is a number form 1 to 99. I'll give you 6 tries.")
while guess != secret and tries < 6 :
    guess = input("What's yer guess? ")
    if int(guess) < secret :
        print ("Too low, ye scurvy dog!")
    elif int(guess) > secret :
        print ("Too higg, landlubber!")

    tries = tries + 1

if int(guess) == secret :
    print ("Avast! Ye got it! Found my secret, ye did！")
else :
    print ("No more guesses! Better luck next time, matey！")
    print ("The secret number was", secret)
import sys
    try:
        input("输入回车结束")
    except:
        sys.exit(0)
#raw_input("输入回车结束")
# print(type(secret))
# print(type(guess))
# print(type(tries))
