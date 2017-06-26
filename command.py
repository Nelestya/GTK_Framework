#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import sys
import os

################################################################################
#                             Exemple Command
################################################################################

################################################################################
"""
Createwindow pathfilename
add_container pathfilename

    "help",
    "add-window",
    "add-actionbar",
    "add-aboutwindow",
    "add-aboutdialog",
    "add-assistant",
    "add-colorchooserdialog",
    "add-filechooserwindow",
    "add-appchooserdialog",

"""


################################################################################


################################################################################
# for execute a command
################################################################################

class Command(object):

    def __init__(self, string):
        global cmd
        cmd = string.split()

    def Exe_Cmd(self):
        try:
            MyClass = cmd[0] + "()"
            eval(MyClass)
        except:
            return None


class Create():
    def __init__(self):
        self.doc = "doc/window.txt"
        self.code = "Window/window.py"
        if len(cmd) == 1:
            return ""
        else if len(cmd) >= 2:
            return 0


class Add():
    def __init__(self):
        self.doc = "doc/window.txt"
        self.code = "Window/window.py"
        print(cmd)


class help():
    def __init__(self):
        self.doc = "doc/help.txt"
        self.Control()

    def Control(self):
        if len(cmd) == 1:
            with open(self.doc, "r") as text:
                x = text.read()
                return x
        else:
            return "Bug generate in help function"
            ################################################################################
            # Window template


if __name__ == '__main__':
    r = Command("help")
    r.Exe_Cmd()
