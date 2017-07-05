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


class Execute_Commande(object):
    def __init__(self, string):

        try:
            global user_cmd
            user_cmd = string.split()
        except Exception as err:
            return err

        self.commands = {"create": Create,
                         "new": New,
                         "help": "help",
                         "ls": "ls",
                         "cd": "cd"
                         }
        self.argv = 0

    def Exe_cmd(self):

        try:
            if len(user_cmd) < 1 or user_cmd[0] == "help":
                return "command is not exist \"help\""

            elif len(user_cmd) > 1 + self.argv:
                self.x = self.commands[user_cmd[0 + self.argv]]()
                return self.x.Response()

            elif len(user_cmd) == 1 + self.argv:
                try:
                    self.x = self.commands[user_cmd[0 + self.argv]]()
                    return self.x.Response()
                except:
                    return "command not exist"
        except Exception as err:
            return err


class Create(Execute_Commande):
    def __init__(self):
        super(Execute_Commande, self).__init__()
        Execute_Commande.__init__(self, user_cmd)
        self.argv = 1
        self.commands = {"window": Window,
                         "aboutdialog": AboutDialog,
                         "appchooserdialog": AppChooserDialog,
                         "assistant": Assistant,
                         "colorchoosedialog": ColorChooseDialog,
                         "filechoosedialog": FileChooseDialog,
                         "recentchoosedialog": RecentChooseDialog
                         }

    def Response(self):
        try:
            return self.Exe_cmd()
        except Exception as err:
            return err


class New(Execute_Commande):
    def __init__(self):
        super(Execute_Commande, self).__init__()
        Execute_Commande.__init__(self, user_cmd)
        self.argv = 1
        self.commands = {"app": App
                         }

    def Response(self):
        try:
            return self.Exe_cmd()
        except Exception as err:
            return err


class App():
    def __init__(self):
        pass

    def response(self):
        return None


class Command(object):
    def __init__(self):

        self.atribute = {}
        self.response = self.name + " created"
        self.template = "Templates/Windows/" + self.name + ".py"
        self.message = self.name + " is created in "
        self.message1 = "create " + self.name + " \"filename\""
        self.message2 = "actually, just create 1 " + self.name + " in 1 file"

    def Condition(self):
        if len(user_cmd) == 3:
            try:
                with open(user_cmd[2], "a") as filename:
                    with open(self.template, "r") as code:
                        filename.write(code.read())
                return self.message + user_cmd[2]
            except Exception as err:
                return err
        elif len(user_cmd) <= 2:
            return self.message1
        else:
            return self.message2

    def Response(self):
        return self.Condition()


class AboutDialog(Command):
    def __init__(self):
        self.name = "AboutDialog"
        super(Command, self).__init__()
        Command.__init__(self)


class AppChooserDialog(Command):
    def __init__(self):
        self.name = "AppChooserDialog"
        super(Command, self).__init__()
        Command.__init__(self)


class Assistant(Command):
    def __init__(self):
        self.name = "Assistant"
        super(Command, self).__init__()
        Command.__init__(self)


class ColorChooseDialog(Command):
    def __init__(self):
        self.name = "ColorChooseDialog"
        super(Command, self).__init__()
        Command.__init__(self)


class FileChooseDialog(Command):
    def __init__(self):
        self.name = "FileChooseDialog"
        super(Command, self).__init__()
        Command.__init__(self)


class RecentChooseDialog(Command):
    def __init__(self):
        self.name = "RecentChooseDialog"
        super(Command, self).__init__()
        Command.__init__(self)


class Terminal(Command):
    def __init__(self):
        self.name = "Terminal"
        super(Command, self).__init__()
        Command.__init__(self)


class Window(Command):
    def __init__(self):
        self.name = "Window"
        super(Command, self).__init__()
        Command.__init__(self)
