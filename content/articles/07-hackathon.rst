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

Registration
============

.. html::
  <div style="width:100%; text-align:left;" >
    <iframe  src="//eventbrite.co.uk/tickets-external?eid=16162713110&ref=etckt" frameborder="0" height="320" width="100%" vspace="0" hspace="0" marginheight="5" marginwidth="5" scrolling="auto" allowtransparency="true"></iframe>
  </div>

Project ideas
=============

Participants and sponsors are welcome to propose any and all ideas relating to
computational semantics - please `get in touch`__ or submit a pull request with
your idea added to `this page`__! The list below shows some possibilities:

__ mailto:d.milajevs@qmul.ac.uk?subject=IWCS-Hackathon
__ https://github.com/iwcs2015/iwcs2015.github.io/blob/pelican/content/articles/07-hackathon.rst

A distributional semantic toolkit
---------------------------------

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

Compositionality for distributional semantic toolkits
-----------------------------------------------------

It has been shown that some type-logical grammars can be interpreted in vector
space semantics, so the challenge here would be to build a tool that connects
such a grammar to a distributional setting.

Ingredients are a representation of such grammars in terms of a
lexicon/derivation rules, a suitable interpretation of types and proofs into
tensor spaces and maps, and distributional data.

Given a lexicon and derivational rules, a theorem prover such as z3_ provides a
proof for a given input sentence which is later used to obtain distributional
representation.

.. _z3: http://rise4fun.com/z3

Wikidepia dump postprocessing
-----------------------------

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

It might be worth submitting the results to `10th Web as Corpus Workshop
(WaC-10)`_.

.. _`10th Web as Corpus Workshop (WaC-10)`: https://www.sigwac.org.uk/wiki/WAC10

NLTK corpus readers
-------------------

NLTK_ is a natural language toolkit that provides basic tools to deal with
textual information. `Corpus readers`__ are interfaces to access textual resources
(called corpora). The task is to provide interfaces to the following resources.

__ http://www.nltk.org/api/nltk.corpus.reader.html#module-nltk.corpus.reader

* **Groningen Meaning Bank**: the `Groningen Meaning Bank`__ is a free
  semantically annotated corpus that anyone can edit.

  __ http://gmb.let.rug.nl/

* **UkWaC**: `UkWaC <http://wacky.sslmit.unibo.it/doku.php>`_ is a 2 billion
  word corpus constructed from the Web   limiting the crawl to the .uk domain.

* **AMR**: the `AMR Bank`__ is a set of English sentences paired with simple,
  readable semantic representations.

  __ http://amr.isi.edu/index.html

Tweet paraphrase generator
--------------------------

Given a tweet, the system has to come up with a paraphrase. For example, by
substituting all the content words (nouns, verbs, adjectives and adverbs) with
similar words.

A twitter bot should monitor Twitter for tweets that contain `#iwcs
<https://twitter.com/search?q=%23iwcs>`_ and generate a paraphrase tweet. Also,
tweets directed to the bot should be replied with a paraphrase.

Twitter stream analysis
-----------------------

We are collection tweets about Easter, Cricket World Cup, IWCS, UKG Fest,
London, and London Marathon. In addition we are gathering geo located tweets
from the UK. The task is to give insights of what these streams are about.

Call for Sponsorship
====================

IWCS is the International Conference in Computational Semantics series: the bi-yearly
meeting of SIGSEM, the ACL special interest group on semantics. The areas
of interest for the conference include all computational aspects of meaning of
natural language within written, spoken, or multimodal communication. We are
organising the 11th IWCS conference; this will be held in Queen Mary University
of London on April 14-17th 2015. For more info see http://sigsem.org/iwcs2015.

This year we would like to organize a hackathon the weekend before the
conference on April 11th-12th. The goal of the event is to provide an
opportunity to discuss and develop tools that are used in Computational
Semantics. Moreover, we also would like to attract anyone interested in data
processing tools so they could contribute to open source projects represented at
the event. Currently, we are looking for sponsors to support the event. We aim
to invite core developers of relevant open source projects (e.g. `NLTK
<http://www.nltk.org/>`_ and `scikit- learn <http://scikit-learn.org/>`_) and
provide travel grants to everyone interested to attend the event.

We are also looking for experienced developers who can mentor participants and
assist with software engineering tools (version control systems, editor,
development environment set up and so on).

To support the event you could:

* Provide funding to cover catering, traveling and organisational costs.
* Propose project ideas that might be implemented during the hackathon.
* Invite experienced developers to mentor.
* Share relevant datasets.

In return we can:

* Work on your project.
* Put your logo on the hackathon web page http://iwcs2015.github.io/hackathon.html.
* Provide a space for a poster, promotional material, an information desk, etc.
  at the venue.

Contact information
-------------------

In case you are interested in supporting the event contact Dmitrijs Milajevs
<d.milajevs@qmul.ac.uk>.
