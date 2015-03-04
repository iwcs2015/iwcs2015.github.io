=================================
Computational Semantics Hackathon
=================================

:date: 2015-02-18 13:32
:category: Hackathon
:slug: hackathon

:news_headline: Hackathon announced

This year, IWCS will feature a **Computational Semantics Hackathon**, before the
main conference on **April 11th-12th** from 10:00 to 17:00.

We invite researchers, developers, students and users of semantic NLP tools to
participate. The goal of the event is to provide an opportunity to discuss and
develop tools that are used in Computational Semantics. Moreover, we also would
like to attract anyone interested in data processing tools so they could
contribute to open source projects represented at the event. *You don't need to
attend the conference to be able to participate at the hackathon.* Registration
to the hackathon will be opened soon.

The event will take place at `Ground Cafe <http://www.qmsu.org/ground/>`_. It's
building 33 on the `QMUL campus map <{filename}/static/qm-campus-map.pdf>`_.
Please refer to the `location page <{filename/articles/09-location.rst}>`_ for
more information on how to get to QM Mile End campus.

The hackathon is organised by the Computational Linguistics lab at QMUL and
sponsored by the `EPSRC`__ grant `EP/J002607/1 — Foundational Structures for
Compositional Meaning`__.

__ http://www.epsrc.ac.uk/
__ http://gow.epsrc.ac.uk/NGBOViewGrant.aspx?GrantRef=EP/J002607/1

.. contents::
    :depth: 2

Project ideas
=============

Participants and sponsors are welcome to propose any and all ideas relating to
computational semantics - please `get in touch`__ or submit a pull request with
your idea added to `this page`__! The list below shows some possibilities:

__ mailto:d.milajevs@qmul.ac.uk?subject=IWCS-Hackathon
__ https://github.com/iwcs2015/iwcs2015.github.io/blob/pelican/content/articles/07-hackathon.rst

Tweet paraphrase generator
--------------------------

Given a tweet, the system has to come up with a paraphrase. For example, by
substituting all the content words (nouns, verbs, adjectives and adverbs) with
similar words.

A twitter bot should monitor Twitter for tweets that contain `#iwcs
<https://twitter.com/search?q=%23iwcs>`_ and generate a paraphrase tweet. Also,
tweets directed to the bot should be replied with a paraphrase.

NLTK corpus readers
-------------------

NLTK_ is a natural language toolkit that provides basic tools to deal with
textual information. `Corpus readers`__ are interfaces to access textual resources
(called corpora). The task is to provide interfaces to the following resources.

__ http://www.nltk.org/api/nltk.corpus.reader.html#module-nltk.corpus.reader

* **Groningen Meaning Bank**: the `Groningen Meaning Bank`__ is a free semantically annotated corpus that anyone can edit.
* **UkWaC**: UkWaC__ is a 2 billion word corpus constructed from the Web limiting the crawl to the .uk domain.
* **Wikipedia**: Wikipedia provides dumps__ of all its content. However, to be used as a corpus a dump has to be cleaned up from the wiki markup.
* **AMR**: the `AMR Bank`__ is a set of English sentences paired with simple, readable semantic representations.

__ http://gmb.let.rug.nl/
__ http://wacky.sslmit.unibo.it/doku.php
__ https://dumps.wikimedia.org/enwiki/
__ http://amr.isi.edu/index.html

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

The project will involve merging and documenting existing pieces of software, such as
`DISSECT`__, `foller.corpora`__ and `discoutils`__.

__ https://github.com/composes-toolkit/dissect
__ https://github.com/dimazest/fowler.corpora
__ https://github.com/MLCL/DiscoUtils

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
