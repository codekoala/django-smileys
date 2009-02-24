#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import smileys
import sys, os

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
smileys_dir = 'smileys'

for path, dirs, files in os.walk(smileys_dir):
    # ignore hidden directories and files
    for i, d in enumerate(dirs):
        if d.startswith('.'): del dirs[i]

    if '__init__.py' in files:
        packages.append('.'.join(fullsplit(path)))
    elif files:
        data_files.append((path, [os.path.join(path, f) for f in files]))

setup(
    name='django-smileys',
    version=smileys.version(),
    url='http://code.google.com/p/django-smileys/',
    author='Josh VanderLinden',
    author_email='codekoala@gmail.com',
    license='BSD',
    packages=packages,
    data_files=data_files,
    description="Easily replace things like :) and B-) with smilies on your Django-powered site.",
    long_description="""
django-smileys is an application that allows your Django-powered site to display those annoying and useless smileys whenever the `smileys` filter a pattern that you specify.  This application serves a very simple purpose, but its uses can go beyond that of merely inserting smileys whenever a particular pattern (like ":)" or ";)").  It can replace whatever pattern you want with an image of your choosing.  There's gotta be something useful in that, right?

This application can make your blog, forums, photo galleries, user comments, etc a little more interesting, and it's very simple to install.  Free icon sets plague the Internet, and you can choose whatever icons you'd like to use!

==Features==

  * Strict pattern matching: you can specify very strict patterns for your smileys
  * Regular expression pattern matching: if you need a little more power in your pattern matching capabilities, you can specify that your patterns are regular expressions (on a per-smiley basis) and the filter should know what to do.
""",
    keywords='django, image, smiley, useless, fun',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Artistic Software',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics'
    ]
)
