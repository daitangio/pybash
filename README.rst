.. contents::
   :depth: 3
..

Runif
=====

Idempotent and *minimal* python 3 library for rapid scripting. Provide
support for creating file, adding data to them, patching and so on.

Why?
====

(Ba)sh scripting is very easy to setup. So we end up using it all the
time for simple procedural script.

Firing up python for a simple task seems too much but... what if a library 
will not only simplify scripting but offer some feature out of the box?

Sometimes is it useful to have idempotent script, like Ansible and
Saltstack teach us.

runif enable an idempotent, functional programming-way.

FEATURES
===========

- No dependency: it works with python library out of the box
- Python logging integration: debug, info level are tuned to provide you the right amount of information
- Battle tested on complex scenarios


HISTORY
========

I have the need for a idempotent script for a complex set of migration procedures. Bash was a pain.
Java was an overkill so runif popped out.

Try the examples running them from the root directory

The run() function is very handy to fire direct command, 
like running git pull or so on (as in a bash script)

Note: runif it is NOT a replacement for Gradle, GNU Make, Maven, etc.

Launch example
==============

Install the package with > python setup.py install

Here an example of what happen if you run twice the *same* script:

::

   $  python examples/stepByStep.py
   [INFO] runif.py.run_if_missed demo ===> step1
   [INFO] runif.py.run_if_missed demo/demofile.txt ===> step2
   [INFO] runif.py.run_if_missed demo/demofile2.c ===> step2
   [INFO] runif.py.run_if_unmarked demo/demofile.txt ===> Step3
   [INFO] runif.py.run_if_present demo/demofile.txt ===> <lambda>
   demo/demofile.txt present!
   [INFO] runif.py.run_each demo\demofile2.c ===> <lambda>
   ** demo\demofile2.c

   $  python examples/stepByStep.py
   [INFO] runif.py.run_if_present demo/demofile.txt ===> <lambda>
   demo/demofile.txt present!
   [INFO] runif.py.run_each demo\demofile2.c ===> <lambda>
   ** demo\demofile2.c

Unstable interfaces / Dev notes
===============================

::

   run_each               is still unstable
   run_if_modified        is brand new and not tested on a huge set of test cases. it is NOT thread safe

See ./CHANGELOG.md for the last modification

Tests
=====

Install py.test with

::

   pip install pytest

run with PYTHONPATH=. pytest

The PYTHONPATH variable is used to ensure you are using the current
version and not another possibly installed one on your env

See https://docs.pytest.org/en/latest/example/index.html for usage
examples

RELEASE HISTORY
===============

v1.0.4 - June Stable release
v0.0.x - May 2020 First public release
