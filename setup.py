#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import smileys

setup(
    name='django-smileys',
    version=smileys.version(),
    description="Easily replace things like :) and B-) with smilies on your Django-powered site.",
    long_description=open('README.rst', 'r').read(),
    keywords='django, image, smiley, useless, fun',
    author='Josh VanderLinden',
    author_email='codekoala@gmail.com',
    url='http://bitbucket.org/codekoala/django-smileys/',
    license='BSD',
    package_dir={'smileys': 'smileys'},
    include_package_data=True,
    packages=find_packages(),
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
    ],
    zip_safe=False
)
