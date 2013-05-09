===============================
Trivial html5lib PyPy benchmark
===============================

This is the simplest test I could think of that tells me something about
the performance of PyPy 2.0. I took three big real world HTML documents:

- the WHATWG HTML specification:
  http://www.whatwg.org/specs/web-apps/current-work/

- the W3C HTML Templates specification:
  http://www.w3.org/TR/2013/WD-html-templates-20130214/

- a diff between CPython branches:
  http://hg.python.org/cpython/rev/122d42d5268e:7a45415956b9

and parsed them using the upcoming html5lib 1.0, a pure-python HTML
parser which parses markup like your Web browser. The relevant part is
this: for each of the three files I do:

.. code-block:: python

    etree_doc = html5lib.parse(f, treebuilder="etree")
    dom_doc = html5lib.parse(f, treebuilder="dom")
    assert etree_doc.tag == '{http://www.w3.org/1999/xhtml}html'
    assert len(dom_doc.toxml()) > 1024

How to run it
-------------

.. code-block:: bash

  $ pip install tox
  $ tox


Disclaimer
----------

.. image:: http://cdn.memegenerator.net/instances/400x/37208074.jpg


Test results
------------

Mac OS X 10.8.3; 2,4 GHz Intel Core i5; 8 GB RAM.

* Python 3.3: 874 seconds

* Python 2.7: 972 seconds

* PyPy 2.0: 195 seconds
