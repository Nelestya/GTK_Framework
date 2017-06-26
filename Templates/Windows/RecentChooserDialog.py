class RecentChooserWindow(Gtk.RecentChooserDialog):
    def __init__(self):
        super(RecentChooserWindow, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkRecentChooserDialog.html"""
