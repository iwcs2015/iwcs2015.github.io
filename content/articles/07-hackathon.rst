=========
Hackathon
=========

:date: 2015-02-03 13:32
:category: Hackathon

.. :news_headline: Hackathon announcement

Hackathon is a sattelite event to the IWCS conference open to everyone that
provides place to work on semantics related software.


.. contents::
    :depth: 2

Call for Sponsorship
====================

IWCS is the International Conference in Computational Semantics series: the bi-
yearly meeting of SIGSEM, the ACL special interest group on semantics. The areas
of interest for the conference include all computational aspects of meaning of
natural language within written, spoken, or multimodal communication. We are
organising the 11th IWCS conference; this will be held in Queen Mary University
of London on April 14-17th 2015. For more info see http://sigsem.org/iwcs2015.

This year we would like to organize a hackathon right after the conference on
**April 18th-19th**. The goal of the event is to provide an opportunity to
discuss and develop tools that are used in Computational Semantics. Moreover, we
also would like to attract anyone interested in data processing tools so they
could contribute to open source projects represented at the event. Currently, we
are looking for sponsors to support the event. We aim to invite core developers
of relevant open source projects (e.g. `NLTK <http://www.nltk.org/>`_ and
`scikit- learn <http://scikit-learn.org/>`_) and provide travel grants to
everyone interested to attend the event.



We are also looking for experienced developers who can mentor participants and
assist with software engineering tools (version control systems, editor,
development environment set up and so on).

To support the event you could:

* Provide funding to cover catering, travelling and organisational costs.
* Propose project ideas that might be implemented during the hackathon.
* Invite experienced developers to mentor.
* Share relevant datasets.

In return we can:

* Work on your project.
* Put your logo on the hackathon web page http://iwcs2015.githib.io/hackathon.
* Provide a space for a poster, promotional material, an information desk, etc.
  at the venue.

Contact information
-------------------

In case you are interested in supporting the event contact Dmitrijs Milajevs
<d.milajevs@qmul.ac.uk>.

Project ideas
=============

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

Groningen Meaning Bank
~~~~~~~~~~~~~~~~~~~~~~

`Groningen meaning bank`__ is a free semantically annotated corpus that anyone
can edit.

__ http://gmb.let.rug.nl/

UkWaC
~~~~~

UkWaC__ is a 2 billion word corpus constructed from the Web limiting the crawl
to the .uk domain

__ http://wacky.sslmit.unibo.it/doku.php

Wikipedia
~~~~~~~~~

Wikipedia provides dumps__ of all its content. However, to be used as a corpus a
dump has to be cleaned up from the wiki markup.

__ https://dumps.wikimedia.org/enwiki/

AMR
~~~

The `AMR Bank`__ is a set of English sentences paired with simple, readable semantic
representations.

__ http://amr.isi.edu/index.html