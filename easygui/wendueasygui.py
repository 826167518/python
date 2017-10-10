#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import easygui
fahr = easygui.integerbox("输入华氏温度:")
cel = float(5) / 9 * (int(fahr) - 32)
easygui.msgbox("摄氏温度为:" + str(cel))
