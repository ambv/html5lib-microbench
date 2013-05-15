#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import time

import html5lib
import lxml.html


def typical_bench_html5lib_etree(files):
    print('html5lib etree:')
    for i in range(1, 201):
        sys.stdout.write('.')
        sys.stdout.flush()
        etree_doc = html5lib.parse(files['wiki{}.html'.format(i)])
        assert etree_doc.tag == '{http://www.w3.org/1999/xhtml}html'
    print('  done.')


def typical_bench_html5lib_dom(files):
    print('html5lib dom:')
    for i in range(1, 201):
        sys.stdout.write('.')
        sys.stdout.flush()
        dom_doc = html5lib.parse(files['wiki{}.html'.format(i)], treebuilder="dom")
        assert len(dom_doc.toxml()) > 1024
    print('  done.')


def typical_bench_html5lib_lxml(files):
    print('html5lib lxml:')
    for i in range(1, 201):
        sys.stdout.write('.')
        sys.stdout.flush()
        lxml_doc = html5lib.parse(files['wiki{}.html'.format(i)], treebuilder="lxml")
        assert lxml_doc.getroot().tag == '{http://www.w3.org/1999/xhtml}html'
    print('  done.')


def typical_bench_lxml(files):
    print('lxml.html:')
    for i in range(1, 201):
        sys.stdout.write('.')
        sys.stdout.flush()
        lxml_doc = lxml.html.document_fromstring(files['wiki{}.html'.format(i)])
        assert len(lxml.html.tostring(lxml_doc)) > 1024
    print('  done.')


def huge_bench_html5lib_etree(files):
    etree_doc = html5lib.parse(files['template.html'])
    assert etree_doc.tag == '{http://www.w3.org/1999/xhtml}html'
    print('  template done;')

    etree_doc2 = html5lib.parse(files['spec.html'])
    assert etree_doc2.tag == '{http://www.w3.org/1999/xhtml}html'
    print('  spec done;')

    etree_doc3 = html5lib.parse(files['py33_py34.html'])
    assert etree_doc3.tag == '{http://www.w3.org/1999/xhtml}html'
    print('  py33_py34 done.')


def huge_bench_html5lib_dom(files):
    print('html5lib dom:')
    dom_doc = html5lib.parse(files['template.html'], treebuilder="dom")
    assert len(dom_doc.toxml()) > 1024
    print('  template done;')

    dom_doc2 = html5lib.parse(files['spec.html'], treebuilder="dom")
    assert len(dom_doc2.toxml()) > 1024
    print('  spec done;')

    dom_doc3 = html5lib.parse(files['py33_py34.html'], treebuilder="dom")
    assert len(dom_doc3.toxml()) > 1024
    print('  py33_py34 done.')


def huge_bench_html5lib_lxml(files):
    print('html5lib lxml:')
    lxml_doc = html5lib.parse(files['template.html'], treebuilder="lxml")
    assert lxml_doc.getroot().tag == '{http://www.w3.org/1999/xhtml}html'
    print('  template done;')

    lxml_doc2 = html5lib.parse(files['spec.html'], treebuilder="lxml")
    assert lxml_doc2.getroot().tag == '{http://www.w3.org/1999/xhtml}html'
    print('  spec done;')

    lxml_doc3 = html5lib.parse(files['py33_py34.html'], treebuilder="lxml")
    assert lxml_doc3.getroot().tag == '{http://www.w3.org/1999/xhtml}html'
    print('  py33_py34 done.')


def huge_bench_lxml(files):
    print('lxml.html:')
    lxml_doc = lxml.html.document_fromstring(files['template.html'])
    assert len(lxml.html.tostring(lxml_doc)) > 1024
    print('  template done;')

    lxml_doc2 = lxml.html.document_fromstring(files['spec.html'])
    assert len(lxml.html.tostring(lxml_doc2)) > 1024
    print('  spec done;')

    lxml_doc3 = lxml.html.document_fromstring(files['py33_py34.html'])
    assert len(lxml.html.tostring(lxml_doc3)) > 1024
    print('  py33_py34 done.')


def main():
    files = {}
    cwd = os.path.dirname(__file__)
    print('prereading files:')
    for file_name in ('template.html', 'spec.html', 'py33_py34.html'):
        with open(os.path.join(cwd, 'data', file_name), 'rb') as f:
            files[file_name] = f.read()
        print(' ', file_name)
    for i in range(1, 201):
        file_name = 'wiki{}.html'.format(i)
        with open(os.path.join(cwd, 'data', file_name), 'rb') as f:
            files[file_name] = f.read()
    print('  200 Wiki pages as wiki*.html')

    print("*" * 10, "Typical pages", "*" * 10)
    start = time.time()
    for i in range(1):
        typical_bench_html5lib_etree(files)
    print(time.time() - start)

    start = time.time()
    for i in range(1):
        typical_bench_html5lib_dom(files)
    print(time.time() - start)

    start = time.time()
    for i in range(1):
        typical_bench_html5lib_lxml(files)
    print(time.time() - start)

    start = time.time()
    for i in range(1):
        typical_bench_lxml(files)
    print(time.time() - start)

    print("*" * 10, "Huge pages", "*" * 10)
    start = time.time()
    for i in range(1):
        huge_bench_html5lib_etree(files)
    print(time.time() - start)

    start = time.time()
    for i in range(1):
        huge_bench_html5lib_dom(files)
    print(time.time() - start)

    start = time.time()
    for i in range(1):
        huge_bench_html5lib_lxml(files)
    print(time.time() - start)

    start = time.time()
    for i in range(1):
        huge_bench_lxml(files)
    print(time.time() - start)


if __name__ == '__main__':
    main()
