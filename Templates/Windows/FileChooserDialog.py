class FileChooserWindow(Gtk.FileChooserDialog):
    def __init__(self):
        super(FileChooserWindow, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkFileChooserDialog.html"""
