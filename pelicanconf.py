#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'The chairs of IWCS 2015'
SITENAME = u'IWCS 2015'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

THEME = 'src/conferencium/'

PLUGIN_PATHS = ('src/pelican-plugins', )
PLUGINS = (
    'extract_toc',
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Menu
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    # ('Blog', 'archives.html'),
    # ('People', 'authors.html'),
)


# Blogroll
LINKS = (
    ('IWCS 2013', 'http://www.ling.uni-potsdam.de/iwcs2013//'),
    # ('Python.org', 'http://python.org/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
    # ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    # ('You can add links in your config file', '#'),
    # ('Another social link', '#'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
