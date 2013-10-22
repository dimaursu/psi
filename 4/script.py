#! /usr/bin/env python
from gi.repository import Gtk
import locale

LOCALE_DIR="locale"
TRANSLATION_DOMAIN = "default"

class GUI(Gtk.Window):
    def __init__(self):
        title="A localized gui program"
        # localisation stuff
        locale.bindtextdomain(TRANSLATION_DOMAIN, LOCALE_DIR)
        locale.setlocale(locale.LC_ALL, "")
        # import the glade file
        builder = Gtk.Builder()
        builder.set_translation_domain(TRANSLATION_DOMAIN)
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
