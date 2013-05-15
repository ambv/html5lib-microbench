#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import codecs
from setuptools import setup

PY3 = sys.version_info[0] == 3

if not PY3:
    reload(sys)
    sys.setdefaultencoding('utf8')

with codecs.open(
    os.path.join(os.path.dirname(__file__), 'README.rst'), 'r', 'utf8',
) as ld_file:
    long_description = ld_file.read()
# We let it die a horrible tracebacking death if reading the file fails.
# We couldn't sensibly recover anyway: we need the long description.

setup (
    name = 'html5lib-microbench',
    version = '0.7.0',
    author = 'Łukasz Langa',
    author_email = 'lukasz@langa.pl',
    description = "This is not a scientific benchmark.",
    long_description = long_description,
    url = 'https://github.com/ambv/html5lib-microbench',
    keywords = '',
    platforms = ['any'],
    license = 'MIT',
    py_modules = ['bench'],
    packages = ['data'],
    scripts = ['bin/html5lib_microbench'],
    include_package_data = True,
    zip_safe = False, # if only because of the readme file
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
