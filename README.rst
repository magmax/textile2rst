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
