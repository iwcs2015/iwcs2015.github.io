========================
Instructions for Authors
========================

:date: 2014-09-01 19:00
:tags: instructions
:category: Submissions
:author: Matthew Purver


Formatting Instructions
=======================

Papers should be formatted with a font size of 11pt, with times as font, typeset in one column, and with margins of 25mm all around. Papers should be submitted in PDF A4 paper format using the START electronic submission web page at https://www.softconf.com/iwcs2015/main. **Note that submissions must be anonymous.** Long paper submissions should not exceed 10 pages plus an additional page for references. Short paper submissions should not exceed 5 pages plus an additional page for references. The first page should include an abstract of c. 10 lines. Authors are strongly encouraged to prepare their submission using LaTeX.

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
