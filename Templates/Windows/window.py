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

    def on_button2_clicked(self, widget):
