import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
################################################################################
# Documentation:
"""https://developer.gnome.org/gtk3/stable/"""

import os
import sys
import pickle

commands_line = [
    "help",
    "add-window",
    "add-actionbar",
    "add-aboutwindow",
    "add-aboutdialog",
    "add-assistant",
    "add-colorchooserdialog",
    "add-filechooserwindow",
    "add-appchooserdialog",
]


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

            self.label_User = Gtk.Label(">>>")
            self.BoxHor.pack_start(self.label_User, True, True, 0)
            self.entry = Gtk.Entry()
            self.entry.connect("activate", self.on_activate_pressed)
            self.BoxHor.pack_start(self.entry, True, True, 0)

            self.MainBox.pack_end(self.BoxHor, True, True, 0)
        except Exception as err:
            print(err)

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

        print(self.entry.get_text())
        ########################################################################
        # Bug
        # (main.py:9385): Gtk-CRITICAL **: gtk_box_pack: assertion 'gtk_widget_get_parent (child) == NULL' failed
        # is resolve if label initialised in variable
        try:
            self.registerLabel.append(Gtk.Label(">>> " + self.entry.get_text() + "\n" + "response"))
            for align_label in self.registerLabel:
                align_label.set_alignment(0, 0)
                self.MainBox.pack_start(align_label, True, True, 0)
            self.show_all()
        except Exception as err:
            print(err)
        #######################################################################
        # Reférence :
        # http://www.pygtk.org/pygtk2reference/class-gtkbox.html#method-gtkbox--set-child-packing


class MyWindow(Gtk.Window):

    def __init__(self):
        # Create the window
        Gtk.Window.__init__(self, title="window name")

        self.box = Gtk.Box(spacing=0)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        PaletteColorWindow()

    def on_button2_clicked(self, widget):
        ass = AssistantWindow()
        ass.show_all()
################################################################################
#            Container
################################################################################


class ActionBar(Gtk.ActionBar):
    def __init__(self):
        super(ActionBar, self).__init__()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkActionBar.html"""

################################################################################
#            Window
################################################################################


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


class AssistantWindow(Gtk.Assistant):
    def __init__(self):
        super(AssistantWindow, self).__init__()
        self.set_title("Assistant")
        self.set_default_size(400, -1)
        self.connect("apply", self.on_apply_clicked)
        self.connect("close", self.on_close_clicked)
        self.connect("cancel", self.on_cancel_clicked)

        self.run()

    def run(self):
        box = Gtk.VBox()
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.INTRO)
        self.set_page_title(box, "Page 1: Introduction")
        label = Gtk.Label("An 'Intro' page is the first page of an Assistant. It is used to provide information about what configuration settings need to be configured. The introduction page only has a 'Continue' button.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        box = Gtk.VBox()
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.CONTENT)
        self.set_page_title(box, "Page 2: Content")
        label = Gtk.Label("The 'Content' page provides a place where widgets can be positioned. This allows the user to configure a variety of options as needed. The page contains a 'Continue' button to move onto other pages, and a 'Go Back' button to return to the previous page if necessary.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        box = Gtk.VBox()
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.CONTENT)
        self.set_page_title(box, "Page 2: Show")
        label = Gtk.Label("The 'Content' page provides a place where widgets can be positioned. This allows the user to configure a variety of options as needed. The page contains a 'Continue' button to move onto other pages, and a 'Go Back' button to return to the previous page if necessary.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        self.complete = Gtk.VBox()
        self.append_page(self.complete)
        self.set_page_type(self.complete, Gtk.AssistantPageType.PROGRESS)
        self.set_page_title(self.complete, "Page 3: Progress")
        label = Gtk.Label("A 'Progress' page is used to prevent changing pages within the Assistant before a long-running process has completed. The 'Continue' button will be marked as insensitive until the process has finished. Once finished, the button will become sensitive.")
        label.set_line_wrap(True)
        self.complete.pack_start(label, True, True, 0)
        checkbutton = Gtk.CheckButton(label="Mark page as complete")
        checkbutton.connect("toggled", self.on_complete_toggled)
        self.complete.pack_start(checkbutton, False, False, 0)

        box = Gtk.VBox()
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.CONFIRM)
        self.set_page_title(box, "Page 4: Confirm")
        label = Gtk.Label("The 'Confirm' page may be set as the final page in the Assistant, however this depends on what the Assistant does. This page provides an 'Apply' button to explicitly set the changes, or a 'Go Back' button to correct any mistakes.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        box = Gtk.VBox()
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.SUMMARY)
        self.set_page_title(box, "Page 5: Summary")
        label = Gtk.Label("A 'Summary' should be set as the final page of the Assistant if used however this depends on the purpose of your Assistant. It provides information on the changes that have been made during the configuration or details of what the user should do next. On this page only a Close button is displayed. Once at the Summary page, the user cannot return to any other page.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

    def on_apply_clicked(self, *args):
        print("The 'Apply' button has been clicked")

    def on_close_clicked(self, *args):
        print("The 'Close' button has been clicked")
        Gtk.main_quit()

    def on_cancel_clicked(self, *args):
        print("The Assistant has been cancelled.")
        Gtk.main_quit()

    def on_complete_toggled(self, checkbutton):
        assistant.set_page_complete(self.complete, checkbutton.get_active())
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkAssistant.html"""
        ########################################################################
        # Error
        # AttributeError: 'AssistantWindow' object has no attribute 'run'
        # référence:
        # https://github.com/Programmica/pygtk-tutorial/blob/master/examples/assistant.py
        # Creation run Function but next Error is
        #   AttributeError: 'gi.repository.Gtk' object has no attribute 'ASSISTANT_PAGE_INTRO'
        # Problem resolve
        # It's not Gtk.ASSISTANT_PAGE_PROGRESS, it's Gtk.AssistantPageType.INTRO
        # Ref:
        # https://people.gnome.org/~gcampagna/docs/Gtk-3.0/Gtk.Assistant.set_page_type.html
        ########################################################################


class PaletteColorWindow(Gtk.ColorChooserDialog):
    def __init__(self):
        super(PaletteColorWindow, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkColorChooserDialog.html"""


class FileChooserWindow(Gtk.FileChooserDialog):
    def __init__(self):
        super(FileChooserWindow, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkFileChooserDialog.html"""


class SelectAppWindow(Gtk.AppChooserDialog):
    def __init__(self):
        super(SelectApp, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkAppChooserDialog.html"""


class RecentChooserWindow(Gtk.RecentChooserDialog):
    def __init__(self):
        super(RecentChooserWindow, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        """https://developer.gnome.org/gtk3/stable/GtkRecentChooserDialog.html"""


"""
class PageSetupDialog(Gtk.PageSetupUnixDialog):
    def __init__(self):
        super(PageSetupDialog, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        # https://developer.gnome.org/gtk3/stable/GtkPageSetupUnixDialog.html
        ########################################################################
        # Error
        # AttributeError: 'gi.repository.Gtk' object has no attribute 'PageSetupUnixDialog'
        ########################################################################


class PrintWindow(Gtk.PrintUnixDialog):
    def __init__(self):
        super(PrintWindow, self).__init__()
        self.run()
        self.destroy()
        ########################################################################
        # Documentation:
        # https://developer.gnome.org/gtk3/stable/GtkPrintUnixDialog.html
        ########################################################################
        # Error
        # AttributeError: 'gi.repository.Gtk' object has no attribute 'PageSetupUnixDialog'
        ########################################################################
        ########################################################################
        # Dependencies :
        # gtk3-print-backends
        # Référence :
        # https://bbs.archlinux.org/viewtopic.php?id=218439
"""


################################################################################
# Launcher
# Test Phase
if __name__ == '__main__':
    win = Terminal()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
