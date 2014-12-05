==============  ===============  =========  ============
VERSION         DOWNLOADS        TESTS      COVERAGE
==============  ===============  =========  ============
|pip version|   |pip downloads|  |travis|   |coveralls|
==============  ===============  =========  ============

Small utility to help moving from Jekyll/Octopress Textile file to standard ReStructured Text.

Installation
------------

.. code:: bash

          pip install textile2rst

Usage
-----

.. code::  bash

           python -m textile2rst filename.textile

What does it do?
----------------

#. Replaces ``<!-- more -->`` by ``.. more``
#. Replaces ``<br/>`` by ``----``
#. Replaces section titles
#. Replaces Jekyll/Octopress code style with directive ``highlight`` into RST format with ``.. code::``
#. Replaces inline links by RST links, gathering them all at the end.

What doesn't it do?
-------------------

#. If you used underscores to set bold or italic, it won't translate it and RST parsers will fail.
#. It doesn't change the metadata in YAML
#. Change the internal references with Jekyll directive ``post_url``
#. Manage any other directive.

.. |travis| image:: https://travis-ci.org/magmax/textile2rst.png
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://coveralls.io/repos/magmax/textile2rst/badge.png
  :target: `Coveralls`_
  :alt: Coveralls results

.. |pip version| image:: https://pypip.in/v/textile2rst/badge.png
    :target: https://pypi.python.org/pypi/textile2rst
    :alt: Latest PyPI version

.. |pip downloads| image:: https://pypip.in/d/textile2rst/badge.png
    :target: https://pypi.python.org/pypi/textile2rst
    :alt: Number of PyPI downloads

.. _Travis: https://travis-ci.org/magmax/textile2rst
.. _Coveralls: https://coveralls.io/r/magmax/textile2rst
