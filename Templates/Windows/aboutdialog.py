class AboutWindow(Gtk.AboutDialog):
    """Fenetre a propos"""

    def __init__(self):
        super(AboutWindow, self).__init__()
        self.set_program_name("Nom Du programme")
        self.set_version("0.0.1")
        self.set_authors("Tristan Dlugosz")
        self.set_copyright("GNU LICENCE")
        self.set_comments("Commentaire")
        self.set_website("https://github.com/Nelestya")
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkAboutDialog.html"""
