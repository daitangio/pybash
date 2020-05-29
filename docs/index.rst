.. runif documentation master file, created by
   sphinx-quickstart on Fri May 29 09:18:02 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to runif's documentation!
=================================

.. toctree::
   :maxdepth: 3
   :caption: Contents:



Welcome to Run...if
=====================


Runif is an idempotent and *minimal* python 3 library for rapid scripting. Provide
support for creating file, adding data to them, patching and so on.

run if in a slogan:
- Execute idempotent scripts based on file contents.
- Battle tested on over 60 conversions
- No dependency: it works with python library out of the box


Simple usage: first example
===============================

.. code-block:: python

    from runif import *

    def demo_python_builder(fname):
        with open(fname,"w") as f:
            f.writelines([
                "def testme(str):\n",
                "\tprintln('Message from "+fname+" '+str)\n",
                "\n",
                "testme('whooa')\n"
            ])

    run_if_missed("workdir", lambda dir_to_build:  (Path(dir_to_build)).mkdir() )
    for x in range(4):
        run_if_missed("workdir/demo"+str(x)+".py", demo_python_builder)

Create workdir if missed.


Runif functions
=================

.. automodule:: runif
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


