class SelectAppWindow(Gtk.AppChooserDialog):
    def __init__(self):
        super(SelectApp, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkAppChooserDialog.html"""
