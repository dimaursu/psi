#! /usr/bin/env python
import locale
import gettext
import os

current_locale, encoding = locale.getdefaultlocale()

locale_path = 'locale/'
language = gettext.translation ('default', locale_path, ["ro"] )
language.install()
print(_('Hello'))
