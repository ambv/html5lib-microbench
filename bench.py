#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import html5lib
import os
import time


files = {}

for file_name in ('spec.html', 'template.html', 'py33_py34.html'):
    with open(os.path.join('data', file_name), 'rb') as f:
        files[file_name] = f.read()
    print(file_name)


def bench(files):
    etree_doc = html5lib.parse(files['spec.html'])
    dom_doc = html5lib.parse(files['spec.html'], treebuilder="dom")
    assert etree_doc.tag == '{http://www.w3.org/1999/xhtml}html'
    assert len(dom_doc.toxml()) > 1024
    print('spec')

    etree_doc2 = html5lib.parse(files['template.html'])
    dom_doc2 = html5lib.parse(files['template.html'], treebuilder="dom")
    assert etree_doc2.tag == '{http://www.w3.org/1999/xhtml}html'
    assert len(dom_doc2.toxml()) > 1024
    print('template')

    etree_doc3 = html5lib.parse(files['py33_py34.html'])
    dom_doc3 = html5lib.parse(files['py33_py34.html'], treebuilder="dom")
    assert etree_doc3.tag == '{http://www.w3.org/1999/xhtml}html'
    assert len(dom_doc3.toxml()) > 1024
    print('py33_py34')


start = time.time()
for i in range(1):
    bench(files)
print(time.time() - start)
