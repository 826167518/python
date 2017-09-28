#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random, easygui
secret = random,randint(1,99)
guess = 0
tries = 0
easygui.msgbox("""AHOY! I'm teh Dread Pirate Roberts, and I have a secret! It is a number from 1 to 99. I'll give you 6 tries.""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("What's yer guess, matey?")
    if not guess: break
    if int(guess) < secret:
       easygui.msgbox(str(guess) + " is too low , ye scurvy dog!")
    elif int(guess) > secret:
       easygui.msgbox(str(guess) + " is too high, landlubber!")
    tries = tries + 1
if int(guess) == secret:
    easygui.msgbox("Avst ! Ye got it! Found my secret , ye did!")
else:
    easygui.msgbox("No more guesses! The number was " + str(cecret))
