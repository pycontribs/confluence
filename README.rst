Confluence Python API
=====================


.. image:: https://img.shields.io/pypi/v/confluence.svg
        :target: https://pypi.python.org/pypi/confluence/

.. image:: https://img.shields.io/pypi/l/confluence.svg
        :target: https://pypi.python.org/pypi/confluence/

.. image:: https://img.shields.io/pypi/dm/confluence.svg
        :target: https://pypi.python.org/pypi/confluence/

.. image:: https://img.shields.io/pypi/wheel/confluence.svg
        :target: https://pypi.python.org/pypi/confluence/
        
.. image:: https://travis-ci.org/pycontribs/confluence.svg?branch=develop
    :target: https://travis-ci.org/pycontribs/confluence

If you want to interfere with Confluence from Python, this is what you are looking for.

While this library is quite new it has the basic functionality for retrieving and storing pages in Confluence 3.x-5.x, hiding most API differences between these versions.

That's open source and I will welcome any contributions, including bug reports ;)

How to use it
-------------

You should read the documentation from `pythonhosted.org/confluence/
<http://pythonhosted.org/confluence/>`_ or just look inside the source code as you may find some new features that are not yet documented.

.. code-block:: python

  from confluence import Confluence
  conf = Confluence(profile='confluence')
  conf.getPage("page","space")
  conf.storePageContent("page","space","hello world!")

Also create a `config.ini` file like this and put it in current directory, user home directory or PYTHONPATH.

.. code-block:: ini

  [confluence]
  url=https://confluence.atlassian.com
  # only the `url` is mandatory
  user=...
  pass=...

Development
-----------

Development takes place on GitHub_, where the git-flow_ branch structure is used:

* ``master`` - contains the latest released code.
* ``develop`` - (default branch) is used for development of the next release.
* ``feature/XXX`` - feature branches are used for development of new features before they are merged to ``develop``.

.. _GitHub: https://github.com/pycontribs/confluence
.. _git-flow: http://nvie.com/posts/a-successful-git-branching-model/

How to report bugs and request improvements
-------------------------------------------

We use the GitHub issue_ tracker. Before you submit your issue, take a look at the list of current issues to see if someone already found something similar.

.. _issue: https://github.com/pycontribs/confluence/issues

