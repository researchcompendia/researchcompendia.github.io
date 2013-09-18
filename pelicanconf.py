#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Research Compendia Contributors'
SITENAME = u'Research Compendia'
SITEURL = ''

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/codersquid'),
        ('github', 'http://github.com/researchcompendia'),)

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
TYPOGRIFY = True
DISQUS_SITENAME = 'researchcompendia'
