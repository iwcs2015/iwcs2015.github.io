========================
Instructions for Authors
========================

:date: 2014-09-01 19:00
:tags: instructions
:category: Submissions
:author: Matthew Purver

..

.. contents::

Formatting Instructions
=======================

Papers should be formatted with a Times font, size 11pt, typeset in one column, and with margins of 25mm all around. Papers should be submitted in PDF A4 paper format using the START electronic submission web page at https://www.softconf.com/iwcs2015/main. **Note that submissions must be anonymous.** Long paper submissions should not exceed 10 pages plus an additional page for references. Short paper submissions should not exceed 5 pages plus an additional page for references. The first page should include an abstract of c. 10 lines. Authors are strongly encouraged to prepare their submission using LaTeX.

Submission Deadline
===================

Authors must submit not later than **16th December 2014**; this submission must contain at least an abstract with enough information to allow assignment of suitable reviewers. Once submitted, we will accept revisions, but final versions must be submitted not later than **19th December 2014**.

LaTeX Submissions
=================

Users of LaTeX should use documentclass ``article`` with the options ``a4paper`` and ``11pt``, using the packages ``times`` and ``geometry`` to set font and margins. For citations please use the ``natbib`` package with ``chicago.bst`` as bibliography style. See below for an example LaTeX file:

.. code-block:: latex

 \documentclass[a4paper,11pt]{article}

 \usepackage{graphicx}  %%% for including graphics
 \usepackage{url}       %%% for including URLs
 \usepackage{times}
 \usepackage{natbib}
 \usepackage[margin=25mm]{geometry}

 \title{Example Paper for IWCS}
 \date{}

 \author{Example Author\\
        Affiliation\\
        \texttt{example@email.org}
   \and Someone Else\\
        Another Affiliation\\
        \texttt{another@email.org}
 }

 \begin{document}
 \maketitle
 \thispagestyle{empty}
 \pagestyle{empty}

 \section{Introduction}

 ....

 \bibliographystyle{chicago}
 \bibliography{mybib} 

 \end{document}
