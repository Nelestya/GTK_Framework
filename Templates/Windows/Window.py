#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class MyWindow(Gtk.Window):

    def __init__(self):
        # Create the window
        Gtk.Window.__init__(self, title="window name")
        # MAIN BOX connect with the window
        self.MainBox = Gtk.Box(spacing=0)
        self.add(self.MainBox)

        # Box connect with the MAIN BOX
        # Documentation : https://developer.gnome.org/gtk3/stable/GtkBox.html
        self.BoxHor = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.MainBox.pack_end(self.BoxHor, False, False, 0)

        #


if __name__ == '__main__':
    win = Mywindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
