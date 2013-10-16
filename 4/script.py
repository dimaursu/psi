#! /usr/bin/env python
from gi.repository import Gtk
import locale, gettext

LOCALE_DIR="locale"

class GUI(Gtk.Window):
    def __init__(self):
        title="A localized gui program"
        builder = Gtk.Builder()
        # localisation stuff
        language = gettext.translation ('default', LOCALE_DIR, ["ro"])
        language.install()
        builder.set_translation_domain('default')
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
        print(_("Hello World!"))

GUI()
Gtk.main()
