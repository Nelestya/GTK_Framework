import os
# Verifier si l'utilisateur est dans le dossier pour installer
# vérifier si l'utilisateur est en super utilisateur ou en utilisateur normal
# Si l'utilisateur a les droit et est dans le dossier alors créer le fichier .desktop


class VerifUser():
    def __init__(self):
        self.verif = False
        self.user = 'root'
        self.dirapp = 'GTK_KILLER'

        # Verify si on est dans le bon dossier

    def where_am_i(self):
        """verify if user is in good directory"""
        self.curdir = os.getcwd().split("/")
        if self.curdir[len(self.curdir) - 1] == self.dirapp:
            self.verif = True
            return self.verif
        else:
            return False

    def userroot(self):
        """verify if user is login in superuser"""
        if os.getuid() == 0:
            return "root"
        else:
            return "I cannot run as a mortal. Sorry."

    def gtk_is_here(self):
        """verify gtk is installed"""
        return None


class Launcher():
    def __init__(self):
        self.pathicon = 'path/icon'
        self.type = 'Application'
        self.encoding = 'UTF-8'
        self.name = 'StreaosGTK'
        self.genericname = 'genericname'
        self.comment = 'Commentaire'
        self.execapp = 'commande qui execute la commande'
        self.startupnotify = False
        # Exemple: Categories=Application;Game;ArcadeGame
        self.categories = 'Application;Software'

    def add_launcher_linux():
        try:
            with open('/usr/share/applications/' + self.name + '.desktop', "w") as launcher:
                launcher.write("[Desktop Entry]\nType=" +
                               self.type + "\nEncoding=" +
                               self.encoding + "\nName=" +
                               self.name + "\nGenericName=" +
                               self.genericname + "\nComment=" +
                               self.comment + "\nIcon=" +
                               self.pathicon + "\nExec=" +
                               self.execapp + "\nTerminal=" +
                               str(self.startupnotify) + "\nCategories=" +
                               self.categories)
            return "The launcher is created"
        except:
            return "you have not permission for create the launcher, use command su or sudo"


class main():
    def __init__(self):
        print("You are in the good directory?")
        if VerifUser().where_am_i() == True:
            print("It' Ok!")
            print("You are Superuser?")
            if VerifUser().userroot() == "root":
                print("It's Ok")
                Launcher().add_launcher_linux()
            else:
                print("It's not Ok, you are not superuser")
        else:
            print("It's not Ok, you are not in the good directory")


if __name__ == '__main__':
    main()
