class PaletteColorWindow(Gtk.ColorChooserDialog):
    def __init__(self):
        super(PaletteColorWindow, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkColorChooserDialog.html"""
