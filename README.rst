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

------------
If you want to interfere with Confluence from Python, this is what you are looking for.

While this library is quite new it has the basic functionality for retrieving and storing pages in Confluence 3.x-5.x, hiding most API differences between these versions.

That's open source and I will welcome any contributions, including bug reports ;)

How to use it
-------------

You should read the documentation from [pythonhosted.org/confluence/](http://pythonhosted.org/confluence/) or just look inside the source code as you may find some new features that are not yet documented.

    from confluence import Confluence
    conf = Confluence(profile='confluence')
    conf.getPage("page","space")
    conf.storePageContent("page","space","hello world!")

How to report bugs
------------------

Cheers,
Sorin Sbarnea
