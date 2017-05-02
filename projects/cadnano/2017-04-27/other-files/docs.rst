.. cadnano docs

Docs
====

The cadnano2.5 documentation is built with `sphinx`_ and hosted at `readthedocs.io`_. We welcome pull requests that improve the docstring coverage of the API. Contributors will be credited on the `AUTHORS`_ page.

.. _`sphinx`: http://www.sphinx-doc.org/
.. _`readthedocs.io`: http://cadnano.readthedocs.io/
.. _`AUTHORS`: https://github.com/cadnano/cadnano2.5/blob/master/AUTHORS


Building the docs
-----------------

**Getting started**

Try setting up your own separate test `sphinx`_ project using sphinx-quickstart. Once you understand how sphinx works, read through the cadnano/docs Makefile and conf.py to understand our configuration. 

.. _`http://www.sphinx-doc.org/en/stable/rest.html`

**Install dependencies**

   $ pip3 install sphinx sphinx_rtd_theme recommonmark

**Building**

From the terminal, make sure you are in the docs directory.

   $ cd cadnano/docs

Clear out the old documentation, if any.

   $ make clean

Build the API. This generates sphinx rst sources in docs/api using `sphinx-autodoc`_.

.. _`sphinx-autodoc`: http://www.sphinx-doc.org/en/stable/man/sphinx-apidoc.html

   $ make buildapi


   $ make clean; make buildapi; make html


If successful, HTML pages should be placed in _build/html. You can open the index.html to inspect your edits.


Sphinx, reStructuredText, and Markdown
--------------------------------------

Sphinx uses `reStructuredText`_ (.rst) which is made for technical documentation and predates Markdown by about 2 years. It is possible to create documentation files in markdown using recommonmark. For the sake of consistency and easily leveraging sphinx features, we just learned the basics of rst and use it for most doc sources. However, markdown doc sources are supported by using [recommonmark](https://github.com/rtfd/recommonmark).

For an example markdown source document, see [scripting](scripting.html) and the corresponding source file `cadnano/docs/scripting.md`
