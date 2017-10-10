#!/usr/bin/env python
# -*- coding:utf-8 -*-
import easygui
#easygui.msgbox("Hell There!")
flavor = easygui.buttonbox("What is your favorite ice cream flavor?", choices = ['Vanilla','Chocolate','Strawberry'])
easygui.msgbox("You picked " + flavor)
