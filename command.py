#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import sys
import os

# Rappel open
# r, pour une ouverture en lecture (READ).
# w, pour une ouverture en écriture (WRITE), à chaque ouverture le contenu du fichier est écrasé. Si le fichier n'existe pas python le crée.
# a, pour une ouverture en mode ajout à la fin du fichier (APPEND). Si le fichier n'existe pas python le crée.
# b, pour une ouverture en mode binaire.
# t, pour une ouverture en mode texte.
# x, crée un nouveau fichier et l'ouvre pour écriture

################################################################################


################################################################################
# for execute a command
################################################################################

class Command(object):

    def __init__(self, string):
        global cmd
        cmd = string.split()
        global response
        response = None

    def Exe_Cmd(self):
        try:
            MyClass = cmd[0] + "()"
            eval(MyClass)
            return response
        except:
            return response

################################################################################
# Main Commands
################################################################################


class Create():
    def __init__(self):
        if len(cmd) == 1:
            return ""
        elif len(cmd) >= 2:
            try:
                MyClass = cmd[1] + "()"
                eval(MyClass)
            except:
                return None


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


class Window():
    def __init__(self):
        self.code = "Templates/Windows/window.py"
        if len(cmd) >= 3:
            try:
                with open(cmd[2], "a") as filename:
                    with open(self.code, "r") as code:
                        filename.write(code.read())
                global response
                response = "Windows is created in " + str(cmd[2])
            except:
                return 0
        elif len(cmd) < 2:
            return 0
        else:
            return 0


class Assistant():
    def __init__(self):
        self.code = "Templates/Windows/Assistant.py"
        if len(cmd) >= 3:
            try:
                with open(cmd[2], "a") as filename:
                    with open(self.code, "r") as code:
                        filename.write(code.read())
            except:
                return 0
        elif len(cmd) < 2:
            return 0
        else:
            return 0


class Aboutdialog():
    def __init__(self):
        self.code = "Templates/Windows/Assistant.py"
        if len(cmd) >= 3:
            try:
                with open(cmd[2], "a") as filename:
                    with open(self.code, "r") as code:
                        filename.write(code.read())
            except:
                return 0
        elif len(cmd) < 2:
            return 0
        else:
            return 0


class Appchooserdialog():
    def __init__(self):
        self.code = "Templates/Windows/AppChooserDialog.py"
        if len(cmd) >= 3:
            try:
                with open(cmd[2], "a") as filename:
                    with open(self.code, "r") as code:
                        filename.write(code.read())
            except:
                return 0
        elif len(cmd) < 2:
            return 0
        else:
            return 0


class Colorchoosedialog():
    def __init__(self):
        self.code = "Templates/Windows/ColorChooseDialog.py"
        if len(cmd) >= 3:
            try:
                with open(cmd[2], "a") as filename:
                    with open(self.code, "r") as code:
                        filename.write(code.read())
            except:
                return 0
        elif len(cmd) < 2:
            return 0
        else:
            return 0


class Filechooserdialog():
    def __init__(self):
        self.code = "Templates/Windows/FileChooserDialog.py"
        if len(cmd) >= 3:
            try:
                with open(cmd[2], "a") as filename:
                    with open(self.code, "r") as code:
                        filename.write(code.read())
            except:
                return 0
        elif len(cmd) < 2:
            return 0
        else:
            return 0


class Recentchooserdialog():
    def __init__(self):
        self.code = "Templates/Windows/RecentChooserDialog.py"
        if len(cmd) >= 3:
            try:
                with open(cmd[2], "a") as filename:
                    with open(self.code, "r") as code:
                        filename.write(code.read())
            except:
                return 0
        elif len(cmd) < 2:
            return 0
        else:
            return 0

################################################################################
# TEST PHASE


if __name__ == '__main__':
    r = Command("Create Window test.py")
    print(r.Exe_Cmd())
