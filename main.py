#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import command
################################################################################
# Documentation:
"""https://developer.gnome.org/gtk3/stable/"""


class Terminal(Gtk.Window):
    # Terminal Control
    def __init__(self):
        Gtk.Window.__init__(self, title="StreaOS GTKiller")
        self.set_name('Terminal')
        self.i = 0
        self.registerLabel = []

        try:
            # Main Box
            self.MainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            self.add(self.MainBox)

            # Box for Interaction User
            self.BoxHor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
            self.MainBox.pack_end(self.BoxHor, False, False, 0)
            # self.Box_Resp_Term = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            # self.MainBox.pack_start(self.Box_Resp_Term, True, True, 0)

            # contents in BoxHor
            self.label_User = Gtk.Label(">>>")
            self.BoxHor.pack_start(self.label_User, False, True, 0)
            self.entry = Gtk.Entry()
            self.entry.connect("activate", self.on_activate_pressed)
            self.BoxHor.pack_start(self.entry, True, True, 0)

            # content on Box_Resp_Term

            self.Revealer = Gtk.Revealer()
            self.Revealer.set_reveal_child(True)

            # create a window scroll
            self.TerminalScroll = Gtk.ScrolledWindow()
            self.Revealer.add(self.TerminalScroll)
            Gtk.Widget.show(self.TerminalScroll)
            self.MainBox.pack_start(self.Revealer, True, True, 0)
            self.Box_Resp_Term = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            self.TerminalScroll.add_with_viewport(self.Box_Resp_Term)

        except Exception as err:
            print("Error in the __init__ Terminal ")
            print(err)

        # CSS For the Terminal
        # Réf: http://wolfvollprecht.de/blog/gtk-python-and-css-are-an-awesome-combo/
        style_provider = Gtk.CssProvider()
        with open("terminal.css", "rb") as filecss:
            css_data = filecss.read()
        style_provider.load_from_data(css_data)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def on_activate_pressed(self, widget):
        self.cmd_user = command.Execute_Commande(self.entry.get_text())

        ########################################################################
        # Bug
        # (main.py:4805): Gtk-CRITICAL **: gtk_box_pack: assertion 'gtk_widget_get_parent (child) == NULL' failed
        #

        try:
            # Return Command and the response
            self.registerLabel.append(
                Gtk.Label(">>> " + self.entry.get_text() + "\n" + self.cmd_user.Exe_cmd()))

            for align_label in self.registerLabel:
                align_label.set_alignment(0, 0)
                self.Box_Resp_Term.pack_start(align_label, False, True, 0)
                align_label.show()

        except Exception as err:
            print("Error in on_activate_pressed in Terminal Class")
            print(err)
        #######################################################################
        # Reférence :
        # http://www.pygtk.org/pygtk2reference/class-gtkbox.html#method-gtkbox--set-child-packing


################################################################################
# Launcher
# Test Phase
if __name__ == '__main__':
    win = Terminal()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
