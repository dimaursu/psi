#! /usr/bin/env python
from gi.repository import Gtk

class GUI(Gtk.Window):
    def __init__(self):
        title="A gui program"
        builder = Gtk.Builder()
        # import the glade file
        builder.add_from_file("gui.glade")
        # connect the handlers
        builder.connect_signals(Handler())
        window = builder.get_object("MainWindow")
        window.show_all()

class Handler:
    def on_quit(self, *args):
        Gtk.main_quit(*args)

    def on_Cut_clicked(self, button):
        print("Hello World!")

GUI()
Gtk.main()
