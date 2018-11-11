#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Alert'
SITENAME = 'The Learning Alert'
SITESUBTITLE = ''
SITEURL = '' # 'ChrisAlertus.github.io'

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'English'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('The Learning Alert' , 'ChrisAlertus.github.io'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Facebook','https://www.facebook.com/christopher.alert'),
          ('Twitter', 'https://twitter.com/4lertus'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## CHRIS ADDED: Nov 10 2018
# THEME
THEME = "SoMA"

# THEME VARIABLES
GITHUB_URL = "https://github.com/ChrisAlertus/chrisalertus.github.io"
TWITTER_USERNAME = "@4lertus"
PROFILE_IMG = '\\img\\bday_headshot_26.jpg'
ABOUT_ME = '/pages/about-me.html'
DISQUS_SITENAME = 'chrisalertus-github-io.disqus.com/'
# CSS_FILE = "prism.css"
# end

# PLUGINS
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['neighbors','i18n_subsites']

STATIC_PATHS = ['img', 'pdf']

