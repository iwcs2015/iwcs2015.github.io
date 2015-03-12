================
Invited Speakers
================

:date: 2015-02-20 12:16
:category: Invited speakers
:slug: speakers

.. contents::
    :depth: 1


`Regina Barzilay <http://people.csail.mit.edu/regina/>`_
========================================================

`Massachusetts Institute of Technology`

**Semantics of Language Grounding**

In this talk, I will address the problem of natural language grounding. We
assume access to natural language documents that specify the desired behavior of
a control application. Our goal is to generate a program that will perform the
task based on this description. The programs involve everything from changing
the privacy settings on your browser, playing computer games, performing complex
text processing tasks, to even solving math problems. Learning to perform tasks
like these is complicated because the space of possible programs is very large,
and the connections between the natural language and the resulting programs can
be complex and ambiguous.  I will present methods that utilize semantics of the
target domain to reduce natural language ambiguity.  On the most basic level,
executing the induced programs in the corresponding environment and observing
their effects can be used to verify the validity of the mapping from language to
programs.  We leverage this validation process as the main source of supervision
to guide learning in settings where standard supervised techniques are not
applicable. Beyond validation feedback, we demonstrate that using semantic
inference in the target domain (e.g., program equivalence) can further improve
the accuracy of natural language understanding.


`Yoshua Bengio <http://www.iro.umontreal.ca/~bengioy/yoshua_en/index.html>`_
============================================================================

`Université de Montréal`


**Deep Learning of Semantic Representations**

The core ingredient of deep learning is the notion of distributed
representation. This talk will start by explaining its theoretical advantages,
in comparison with non-parametric methods based on counting frequencies of
occurrence of observed tuples of values (like with n-grams). The talk will then
explain how having multiple levels of representation, i.e., depth, can in
principle give another exponential advantage. Neural language models have been
extremely successful in recent years but extending their reach from language
modelling to machine translation is very appealing because it forces the learned
intermediate representations to capture meaning, and we found that the resulting
word embeddings are qualitatively different. Recently, we introduced the notion
of attention-based neural machine translation, with impressive results on
several language pairs, and these results will conclude the talk.


`Ann Copestake <http://www.cl.cam.ac.uk/~aac10/>`_
==================================================

`University of Cambridge`

**Is There Any Logic in Logical Forms?**

Formalising the notion of compositionality in a way that makes it meaningful is
notoriously complicated. The usual way of formally describing compositional
semantics is via a version of Montague Grammar but, in many ways, MG and its
successors are inconsistent with the way semantics is used in computational
linguistics.  As computational linguists we are rarely interested in
model-theory or truth-conditions.  Our assumptions about word meaning, and
distributional models in particular, are very different from the MG
idealisation.  However, computational grammars have been constructed which
produce empirically useful forms of compositional representation and are much
broader in coverage than any grammar fragments from the linguistics literature.
The methodology which underlies this work is predominantly syntax-driven (e.g.,
CCG, LFG and HPSG), but the goal has been to abstract away from the
language-dependent details of syntax.  The question, then, is whether this is
'just engineering' or whether there is some theoretical basis which is more
consistent with CL than the broadly Montogovian approach.

In this talk, I will start by outlining some of the work on compositional
semantics with large-scale computational grammars and in particular work using
Minimal Recursion Semantics (MRS) in DELPH-IN.  There are grammar fragments for
which MRS can be converted into a logical form with a model-theoretic
interpretation but I will argue that attempting to use model theory to justify
the MRS structures in general is inconsistent with the goals of grammar
engineering.  I will outline some alternative approaches to integrating
distributional semantics with this framework and show that this also causes
theoretical difficulties.  In both cases, we could consider inferentialism as an
alternative theoretical grounding whereby classical logical properties are
treated as secondary rather than primary. In this view, it is important that our
approaches to compositional and lexical semantics are consistent with uses of
language in logical reasoning, but it is not necessary to try and reduce all
aspects of semantics to logic.
