IWCS 2015 website
=================

Writing an article
------------------

The content of the blog is hosted on `github <http://github.com>`__, a project
hosting service. There are two ways of adding the content to the website. The
simplest one is to use web interface, the most powerful is to use the ``git``
program.

To add an article using the web based interface follow these steps:

1. Get an account on `github <http://github.com>`__ and login.

2. `Create a file`_ in the ``content/articles/`` folder.

3. Name the file as ``nnn-slug.rst``, where

   * ``nnn`` is a number of the article. Articles are numbered sequentially, pick
     the next integer from the the `articles`_ directory.

   * ``slug`` is an informative but short identifier of the article.

   * ``.rst`` is the file format we are using. It allows to define basic
     formatting, such as headers, links or references. Refer to the
     `reStructuredText quick reference`_ for examples.

4. Apart form the article, the file should contain some meta information, such
   as the name of the author, the date the article was written, its tags and
   category. Here is an example, copy, paste and modify it:

   .. code-block:: rst

       ==========================================
       An example of an article in the rst format
       ==========================================

       .. Some metadata

       :date: 2014-04-02 15:00
       :tags: technology, example
       :category: blog
       :author: Dmitrijs Milajevs

       The first paragraph should introduce and possibly summarize the article.
       It should be relatively short: 2 - 3 sentences.

       .. Explicitly mark the end of the summary/introduction

       -- PELICAN_END_SUMMARY --

       .. Here goes the rest of the article.

       This is a header
       ================

       This is the second paragraph. You can mark some text as **bold** or `italic`.

5. Write the article!

6. Save the file by clicking a light green button in the bottom right corner of the page.

7. Now you are ready to create a `pull request`_!

   a) Go to ``https://github.com/YOUR_USERNAME/iwcs2015.github.io/``.

   b) Click on *create pull request*.

   c) Fill in all the relevant information.

   d) Send a pull request.

You article will be reviewed by other contributors. You might be given
suggestions on how the article can be improved. Once the suggestions are
implemented the article is be published!

.. _Create a file: https://github.com/iwcs2015/iwcs2015.github.io/new/pelican/content/articles
.. _articles: https://github.com/iwcs2015/iwcs2015.github.io/tree/pelican/content/articles
.. _reStructuredText quick reference: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _pull request: https://help.github.com/articles/creating-a-pull-request

Using git
---------

First of all, `set up an ssh key <https://help.github.com/articles/generating-ssh-keys>`_,
and `fork <https://help.github.com/articles/fork-a-repo>`_ the `original repo <https://github.com/iwcs2015/iwcs2015.github.io/>`_.
You also need to `configure git <https://help.github.com/articles/set- up-git>`_.
If you didn't use git before, check out `Github tutorial <http://try.github.io>`_,
a `tutorial provided by Software Carpentry <http://apawlik.github.io/2014-02-03-TGAC/lessons/tgac/version-control/tutorial.html>`_
or `Github guides <https://guides.github.com>`_ to get a general idea.


1. Before writing an article, clone the repo:

.. code-block:: bash

    git clone git@github.com:username/iwcs2015.github.io
    cd iwcs2015.github.io

2. Write an article!

3. Commit and push your changes:

.. code-block:: bash

    git status  # see what files have been changed
    git diff  # see the actual changes
    git add RELATED_FILES  # probably, something like content/articles/001-intro.rst
    git commit -m'An article describing the enterprise (R) power of Java.'
    git push  # send you changes to github

Create a `pull request <https://help.github.com/articles/creating-a-pull-request>`_.

Generating the site locally
---------------------------

We use `buildout <https://pypi.python.org/pypi/zc.buildout/>`_ to deploy
needed software. A typical biuldout deployment consists of two steps:
bootstrapping and building out.

Bootstraping is simple::

    make boostrap

An easy way to see rendered article files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use `restview <https://pypi.python.org/pypi/restview>`_ to see rendered
``.rst``  or `meow <https://pypi.python.org/pypi/meow/>`_ for ``.md`` files in
your browser. For example:

.. code-block:: bash

    bin/restview content/articles/001-intro.rst  # to see the intro article
    bin/meow content/articles/009-markdown.md  # to see the Markdown article

There are rumours, that you can feed a directory to restview and then select
files in the browser::

    bin/restview content

Generating the HTML version of a blog locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, you can get a local version of the blog:

.. code-block:: bash

    make devserver
    open http://localhost:8000  # gnome-open on Linux
    # make stopserver is a logical way to stop the server


Developing the theme and plugins
--------------------------------

Our blog uses a custom theme and plugins. The theme and the plugins are external
projects and don't belong to this git repository! However, during the
``buildout`` step they are cloned to the ``src/`` folder, thanks to `Mr.
Developer <https://pypi.python.org/pypi/mr.developer>`_. Here are the external
projects we depend on:

.. code-block:: bash

    tree -L 1 src/
    src/
    ├── pelican-plugins  # External plugins. Don't bother about it.
    ├── pelican_extended_authors # Our plugin that provided authors' metadata.
    └── pelicanium  # The theme we use.

Note that, by default ``pelicanium`` and ``pelican_extended_authors`` are clones
of https://github.com/iwcs2015, but if you want to make changes to these projects
you need to use your own fork! These are the steps you need to perform, to be
able to push to your own fork:

1. Fork ``pelicanium`` and ``pelican_extended_authors`` in github web interface.
   Refer to the ``[sources]`` section of ``buildout.cfg`` to see what projects
   you should fork. Such projects are located under ``https://github.com/iwcs2015/``.

2. Create ``.mr.developer-options.cfg`` with the following content:

.. code-block:: ini

    [rewrites]
    # Use your own forks instead of the upstream repos for the ``iwcs2015``projects.
    iwcs2015 =
        url ~ ^https://github.com/iwcs2015/
        git@github.com:YOUR_USERNAME/
        kind = git

    # Use ssh instead of https for all github repos.
    github =
        url ~ ^https://github.com/
        git@github.com:
        kind = git

3. Remove the ``src`` folder. Be sure that there are no any changes you want to
   keep. If there are, `change remote urls in git repo`_.

.. code-block:: bash

    rm src/ -rf  # Again, be vary careful!

4. Run ``bin/buildout``.

Change remote urls in git repo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you want to push to github after you run ``buildout``, you need to
change remote urls by yourself, for example:

.. code-block:: bash

    cd src/pelicanium
    git remote set-url origin git@github.com:YOUR_USERNAME/iwcs2015.github.io

Update dependencies
~~~~~~~~~~~~~~~~~~~

If you want to update the dependencies, run::

    bin/develop up

Add a remote
~~~~~~~~~~~~

In case you want to refer not only to your repo, but to others, you need to add
another remote:

.. code-block:: bash

    git remote add upstream git@github.com:iwcs2015/iwcs2015.github.io

Now you can merge with the recent ``pelican`` branch:

.. code-block:: bash

    git checkout pelican
    git fetch upstream
    git merge upstream/pelican

You can also checkout feature branches:

.. code-block:: bash

    git checkout -b theme upstream/theme  # Get the theme branch from upstream
    git push -u theme origin/theme  # Push it to your fork and set it as the default push destination

Updating the web site
---------------------

In case you are lucky and have write access to the main repo you can upload the
generated HTML version of the site, however you need to clone
``git@github.com:iwcs2015/iwcs2015.github.io``.

To upload the HTML just run::

    make deploy

License
-------

.. image:: http://i.creativecommons.org/l/by/4.0/80x15.png

This work is licensed under a `Creative Commons Attribution 4.0 International
License <http://creativecommons.org/licenses/by/4.0/deed.en_US>`_.
