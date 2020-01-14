#!/usr/bin/env python
"""
This example show how to 
compile a bunch of python files using parallel pool.



"""
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from pybash import *

from pathlib import Path
import os, re,logging

def demo_python_builder(fname):
    with open(fname,"w") as f:
        f.writelines([
               "def testme(str):\n",
               "\tprintln('Message from "+fname+" '+str)\n",
               "\n",
               "testme('whooa')\n"
        ])

def compile_dep1(filename):
    """
    Runs in a separate thread: it need to re-init the logging (?)
    """    
    log = logging.getLogger("compiler")
    log.info("Compiling %s" % (filename))
    import py_compile
    py_compile.compile(filename)

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s]  %(threadName)s %(thread)d %(filename)s.%(funcName)s %(message)s',
                        level=logging.INFO)
    run_if_missed("demo2", lambda dir_to_build:  (Path(dir_to_build)).mkdir() )
    for x in range(4):
        run_if_missed("demo2/demo"+str(x)+".py", demo_python_builder)        
    # Compile only if NEEDED
    def fx(f):
        return run_if_modified(f, compile_dep1)
    run_each("demo2","*.py", fx )
    m=run_if_modified("demo2/demo1.py", lambda f: print("Modified:",f))
    if not m:
        print("demofile no modified")
    else:
        print("demofile modified")