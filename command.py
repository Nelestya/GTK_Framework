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


def exe_cmd(string):
    global cmd
    cmd = string.split()
    commands = {"create": create, "hello": "test"}
    try:
        if len(cmd) >= 1:
            if commands.has_key(cmd[0]):
                return commands[cmd[0]]()
    except Exception as err:
        return 0


def create():
    """
    Create command function
    for create a new window
    """
    commands = {"window": window,
                "aboutdialog": aboutdialog,
                "appchooserdialog": appchooserdialog,
                "assistant": assistant,
                "colorchoosedialog": colorchoosedialog,
                "filechooserdialog": filechooserdialog,
                "recentchooserdialog": recentchooserdialog}
    try:
        if len(cmd) == 1:
            return "help create"
        elif len(cmd) >= 2:
            if commands.has_key(cmd[1]):
                return commands[cmd[1]]()
            else:
                return "help create"
    except Exception as err:
        return err


def window():
    """
    Create a new window
    """
    template = "Templates/Windows/Window.py"
    name_function = "window"

    if len(cmd) == 3:
        try:
            with open(cmd[2], "a") as filename:
                with open(template, "r") as code:
                    filename.write(code.read())
            return name_function + " is created in " + str(cmd[2])
        except Exception as err:
            return err
    elif len(cmd) <= 2:
        return "create " + name_function + " \"filename\""
    else:
        return "actually, just create 1 " + name_function + " in 1 file"


def aboutdialog():
    """
    Create a new aboutdialog
    """
    template = "Templates/Windows/AboutDialog.py"
    name_function = "aboutdialog"

    if len(cmd) == 3:
        try:
            with open(cmd[2], "a") as filename:
                with open(template, "r") as code:
                    filename.write(code.read())
            return name_function + " is created in " + str(cmd[2])
        except Exception as err:
            return err
    elif len(cmd) <= 2:
        return "create " + name_function + " \"filename\""
    else:
        return "actually, just create 1 " + name_function + " in 1 file"


def appchooserdialog():
    """
    Create a new AppChooserDialog
    """
    template = "Templates/Windows/AppChooserDialog.py"
    name_function = "AppChooserDialog"

    if len(cmd) == 3:
        try:
            with open(cmd[2], "a") as filename:
                with open(template, "r") as code:
                    filename.write(code.read())
            return name_function + " is created in " + str(cmd[2])
        except Exception as err:
            return err
    elif len(cmd) <= 2:
        return "create " + name_function + " \"filename\""
    else:
        return "actually, just create 1 " + name_function + " in 1 file"


def assistant():
    """
    Create a new assistant
    """
    template = "Templates/Windows/Assistant.py"
    name_function = "assistant"

    if len(cmd) == 3:
        try:
            with open(cmd[2], "a") as filename:
                with open(template, "r") as code:
                    filename.write(code.read())
            return name_function + " is created in " + str(cmd[2])
        except Exception as err:
            return err
    elif len(cmd) <= 2:
        return "create " + name_function + " \"filename\""
    else:
        return "actually, just create 1 " + name_function + " in 1 file"


def colorchoosedialog():
    """
    Create a new colorchoosedialog
    """
    template = "Templates/Windows/ColorChooseDialog.py"
    name_function = "colorchoosedialog"

    if len(cmd) == 3:
        try:
            with open(cmd[2], "a") as filename:
                with open(template, "r") as code:
                    filename.write(code.read())
            return name_function + " is created in " + str(cmd[2])
        except Exception as err:
            return err
    elif len(cmd) <= 2:
        return "create " + name_function + " \"filename\""
    else:
        return "actually, just create 1 " + name_function + " in 1 file"


def filechooserdialog():
    """
    Create a new filechooserdialog
    """
    template = "Templates/Windows/FileChooserDialog.py"
    name_function = "filechooserdialog"

    if len(cmd) == 3:
        try:
            with open(cmd[2], "a") as filename:
                with open(template, "r") as code:
                    filename.write(code.read())
            return name_function + " is created in " + str(cmd[2])
        except Exception as err:
            return err
    elif len(cmd) <= 2:
        return "create " + name_function + " \"filename\""
    else:
        return "actually, just create 1 " + name_function + " in 1 file"


def recentchooserdialog():
    """
    Create a new recentchooserdialog
    """
    template = "Templates/Windows/RecentChooserDialog.py"
    name_function = "recentchooserdialog"

    if len(cmd) == 3:
        try:
            with open(cmd[2], "a") as filename:
                with open(template, "r") as code:
                    filename.write(code.read())
            return name_function + " is created in " + str(cmd[2])
        except Exception as err:
            return err
    elif len(cmd) <= 2:
        return "create " + name_function + " \"filename\""
    else:
        return "actually, just create 1 " + name_function + " in 1 file"

    ################################################################################
    # TEST PHASE


if __name__ == '__main__':

    print(exe_cmd("create window test.py"))
