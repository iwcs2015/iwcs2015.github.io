=================================
Computational Semantics Hackathon
=================================

:date: 2015-02-18 13:32
:category: Hackathon
:slug: hackathon
:template: hackathon
:news_headline: Hackathon announced
:not_sticky_toc: True

This year, IWCS will feature a **Computational Semantics Hackathon**, before the
main conference on **April 11th-12th** from 10:00 to 17:00.

We invite researchers, developers, students and users of semantic NLP tools to
participate. The goal of the event is to provide an opportunity to discuss and
develop tools that are used in Computational Semantics. Moreover, we also would
like to attract anyone interested in data processing tools so they could
contribute to open source projects represented at the event. *You don't need to
attend the conference to be able to participate at the hackathon.*

The event will take place at `Ground Cafe <http://www.qmsu.org/ground/>`_. It's
building 33 on the `QMUL campus map <{filename}/static/qm-campus-map.pdf>`_.
Please refer to the `location page <{filename}/articles/09-location.rst>`_ for
more information on how to get to the QMUL Mile End Campus.

The hackathon is organised by the Computational Linguistics lab at QMUL and
sponsored by the EPSRC_ grant `EP/J002607/1 — Foundational Structures for
Compositional Meaning`__ and `EECS`_. GitHub_ kindly offers subscription coupons
for the 3 winning teams.

__ http://gow.epsrc.ac.uk/NGBOViewGrant.aspx?GrantRef=EP/J002607/1

.. _EPSRC: http://www.epsrc.ac.uk/
.. _EECS: http://eecs.qmul.ac.uk/
.. _GitHub: https://github.com

.. contents::
    :depth: 2

Saturday morning
================

We are glad to welcome you to the hackathon! Saturday morning, the time before
the coffee break, is dedicated to introduction. It's also a great opportunity
for you to set up wifi, talk to people and decide on a project.

We will use a `Trello board <https://trello.com/b/AQIKkm6V/iwcs-
hackathon-2015>`_ to keep track of the progress. You should have received an
invitation email to the board, if not ask someone who is added to it to add you.
Each project is assigned a color, so you can see to which project a card
belongs. **If you are interested in a task, please add yourself to a
corresponding card**. Feel free to add your own projects in the Comments_.

From the software point of view, it's nice to have **Python installed** on your
laptop. We suggest to `install Miniconda`_ (there is a USB drive with the
installation scripts, just in case) and create a dedicated virtual environment
with common packages:

.. _`install Miniconda`: http://eecs.io/python-environment-for-scientific-computing.html

.. code-block:: bash

  # Create an environment
  ~/miniconda3/bin/conda create -n iwcs15-hack python=3.4 nltk pandas scikit-learn ipython-notebook

  # Activate it
  source ~/miniconda3/bin/activate iwcs15-hack

  # Install a package using conda (preferred)
  conda install flask

  # Install a package using pip if conda can't find it
  pip install more_itertools

Register on `github <https://github.com>`_ and `bitbucket
<https://bitbucket.org>`_. `Generate SSH keys`__ and the public key to the
services. Use the `iwcs15-hack organization`_ to store and share code. Share you
github account name in the comments_, so we could add you to the organization.

.. _`iwcs15-hack organization`: https://github.com/iwcs15-hack


Get a good text editor, for example `Atom <https://atom.io/>`_ or `SublimeText
<http://www.sublimetext.com/>`_.

__ https://help.github.com/articles/generating-ssh-keys/

Help others or ask for help! Use comments_ or a `dedicated channel`__ for
communication. Network. Have fun.

__ https://tlk.io/iwcs15-hack

A distributional semantic toolkit (Green)
=========================================

This project aims to provide researchers working in distributional semantics with
a set of core Python utilities. The following functionality is required:

* A space-efficient datastructure for storing distributed representations of words
  and phrases, e.g. through memory-mapped `numpy` arrays or `bcolz`-backed `pandas` data frames
* Efficient exact and approximate nearest neighbour search, e.g. through a `scikit-learn`'s
  KD-tree or random projections
* Efficient dimensionality reduction (SVD, NMF) and feature reweighting (PMI, PPMI)
* Converters to and from commonly used formats
* Easy evaluation against a set of word similarity datasets, such as Mitchel and Lapata (2008) or MEN

The project will involve merging and documenting existing pieces of software,
such as `DISSECT`_, `fowller.corpora`_ and `discoutils`_. Check out `a relevant
discussion on including word embedding algorithms to NLTK`__.

__ https://github.com/nltk/nltk/issues/798

.. _DISSECT: https://github.com/composes-toolkit/dissect
.. _fowller.corpora:  https://github.com/dimazest/fowler.corpora
.. _discoutils: https://github.com/MLCL/DiscoUtils

Compositionality for distributional semantic toolkits (Yellow)
==============================================================

It has been shown that some type-logical grammars can be interpreted in vector
space semantics, so the challenge here would be to build a tool that connects
such a grammar to a distributional setting.

Ingredients are a representation of such grammars in terms of a
lexicon/derivation rules, a suitable interpretation of types and proofs into
tensor spaces and maps, and distributional data.

Given a lexicon and derivational rules, a theorem prover such as z3_ provides a
proof for a given input sentence which is later used to obtain distributional
representation.

LG_ is a theorem prover by Jeroen Bransen, see `his MSc thesis`__. It's written
in C++, takes a ``.txt`` file (lexicon) as input and produces a tex/pdf as
output.

.. _z3: http://rise4fun.com/z3
.. _LG: {filename}/static/LGprover2.zip
__ http://dspace.library.uu.nl/handle/1874/179422

Wikipedia dump postprocessing (Orange)
======================================

Wikipedia provides `dumps`__ of all its content. However, to be used by NLP
tools (for example parsers) a dump has to be cleaned up from the wiki markup.
The postrocessing steps are rarely described in details in scientific
literature. A postprocessed Wikipedia dump from 2009 is often used in
current literature.

__ https://dumps.wikimedia.org/enwiki/

The goal of this task is to come up with a easy to deploy and well documented
pipeline of processing a Wikipdedia dump. There are two steps in the pipeline:
raw text extraction and parsing.

There are at least two ways of getting raw text out of a Wikipedia dump. Wiki
markup can be filtered out using regular expressions, as `it's done`__ in
`gensim`_ and `Wikipedia Extractor`_. Alternatively, text in the wiki markup can
be parsed using `Parsoid`_ to obtain (X)HTML, later this HTML is processed, for
example tables and images are removed (see `this notebook`__). `Pandoc`_ and
`Docverter`_ is a powerful document conversion solution that can be used to
convert a wiki dump to plain text.

.. _gensim: https://radimrehurek.com/gensim/
.. _Parsoid: https://www.mediawiki.org/wiki/Parsoid
.. _Pandoc: http://johnmacfarlane.net/pandoc/
.. _Docverter: https://github.com/docverter/docverter#docverter-server
.. _`Wikipedia Extractor`: https://github.com/bwbaugh/wikipedia-extractor


__ https://github.com/piskvorky/gensim/blob/develop/gensim/corpora/wikicorpus.py
__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/Wikipedia%20dump.ipynb

Later the raw text of a dump can be parsed by some of these parsers:

* `C&C tools <http://svn.ask.it.usyd.edu.au/trac/candc>`_
* `Illinois tools <http://cogcomp.cs.illinois.edu/page/software>`_
* `MaltParser <http://www.maltparser.org/>`_
* `Senna <http://ml.nec-labs.com/senna/>`_
* `Stanford CoreNLP <http://nlp.stanford.edu/software/corenlp.shtml>`_
* `TurboParser <http://www.ark.cs.cmu.edu/TurboParser/>`_
* `YaraParser <https://github.com/yahoo/YaraParser>`_

It might be worth submitting the results to `10th Web as Corpus Workshop
(WaC-10)`_.

.. _`10th Web as Corpus Workshop (WaC-10)`: https://www.sigwac.org.uk/wiki/WAC10

There is work in progress on making HTML dumps available, see T93396_ and
T17017_.

.. _T93396: https://phabricator.wikimedia.org/T93396
.. _T17017: https://phabricator.wikimedia.org/T17017

NLTK corpus readers (Red)
=========================

`NLTK <http://www.nltk.org/>`_ is a natural language toolkit that provides basic
tools to deal with textual information. `Corpus readers`__ are interfaces to
access textual resources (called corpora). The task is to provide interfaces to
the following resources.

__ http://www.nltk.org/api/nltk.corpus.reader.html#module-nltk.corpus.reader

* **Groningen Meaning Bank**: the `Groningen Meaning Bank`__ is a free
  semantically annotated corpus that anyone can edit.

  __ http://gmb.let.rug.nl/

* **UkWaC**: `UkWaC <http://wacky.sslmit.unibo.it/doku.php>`_ is a 2 billion
  word corpus constructed from the Web   limiting the crawl to the .uk domain.

* **AMR**: the `AMR Bank`__ is a set of English sentences paired with simple,
  readable semantic representations.

  __ http://amr.isi.edu/index.html

Tweet paraphrase generator (Violet)
===================================

Given a tweet, the system has to come up with a paraphrase. For example, by
substituting all the content words (nouns, verbs, adjectives and adverbs) with
similar words.

A twitter bot should monitor Twitter for tweets that contain `#iwcs or #iwcs2015
<https://twitter.com/search?q=%23iwcs%20OR%20%23iwcs2015>`_ and generate a paraphrase tweet. Also,
tweets directed to the bot should be replied with a paraphrase.

Twitter stream analysis (Blue)
==============================

We are collecting tweets about Easter, Cricket World Cup, IWCS, UKG Fest,
London, and the London Marathon. In addition we are gathering geo located tweets
from the UK. The task is to give insights of what these streams are about. Some
limited statistics about the collected tweets::

  du -hs *
  632M  cricket
  816M  easter
  13M ep14
  199M  heartbleed
  56K iwcs
  8.1G  london
  2.1M  london-marathon
  2.0G  uk
  1.9M  ukg-fest

Poultry_ is a tweet collection manager that might be handy that provides a
`simple access to a tweet collection`__.

.. _Poultry: http://poultry.readthedocs.org/en/latest/
__ http://poultry.readthedocs.org/en/latest/#integration-with-other-tools

Dialog system (Light Blue)
==========================

Matthew Stone provided a series of IPython Notebooks (`github repo`__, `rendered
notebooks`__) that implement and extend the original Eliza program, and build a
dialog move classifier using NLTK and use information retrieval to put together
relevant responses.

__ https://github.com/iwcs15-hack/dialog_system
__ http://nbviewer.ipython.org/github/iwcs15-hack/dialog_system/tree/master/

Other resources
===============

* `Distributional vectors`__ for 23586 words extracted from Google Books Ngrams.

  __ http://www.eecs.qmul.ac.uk/~dm303/cvsc14.html#experiment-data

* `GoogleNews-vectors-negative300.bin.gz`_ ``word2vec`` vectors use
  `gensim.models.word2vec`_ to access the word vectors and perform similarity
  queries.

* SimLex999_ is a gold standard resource for the evaluation of models that learn
  the meaning of words and concepts.

.. _SimLex999: http://www.cl.cam.ac.uk/~fh295/simlex.html

.. _`GoogleNews-vectors-negative300.bin.gz`: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing

.. _`gensim.models.word2vec`: http://radimrehurek.com/gensim/models/word2vec.html

More project ideas
==================

Participants and sponsors are welcome to propose any and all ideas relating to
computational semantics - please `get in touch`__, submit a pull request with
your idea added to `this page`__, or just write it down in the comments_ below

__ mailto:d.milajevs@qmul.ac.uk?subject=IWCS-Hackathon
__ https://github.com/iwcs2015/iwcs2015.github.io/blob/pelican/content/articles/07-hackathon.rst

Contact information
===================

In case you are interested in supporting the event contact Dmitrijs Milajevs
<d.milajevs@qmul.ac.uk>.

Comments
========

.. html::

  <div id="disqus_thread"></div>
  <script type="text/javascript">
      /* * * CONFIGURATION VARIABLES * * */
      var disqus_shortname = 'iwcs2015';

      /* * * DON'T EDIT BELOW THIS LINE * * */
      (function() {
          var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
          dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
          (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
      })();
  </script>
  <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
