#!/usr/bin/env python
import sys, os

from runif import *

from pathlib import Path
import os, re,logging

def step1(dir_to_build):
    (Path(dir_to_build)).mkdir()


def step2(fname):
    with open(fname, "a") as f:
        f.write("Example file %s \n" % (fname))

def step3(fname,marker):
    with open(fname, "a") as f:
        f.write("demodata="+marker+"\n")
        f.write("# Marker inserted above\n")
        f.write("daitangio=rulez")

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(filename)s.%(funcName)s %(message)s',
                        level=logging.INFO)
    run_if_missed("demo", step1)
    run_if_missed("demo/demofile.txt", step2)
    run_if_missed("demo/demofile2.c", step2)
    run_if_unmarked("demo/demofile.txt","Step3",step3)
    val=extract_var("demo/demofile.txt", "daitangio")
    assert val == "rulez"
    run_if_present("demo/demofile.txt", lambda f: print(f+" present!"))
    run_if_present("demo/no_demofile.txt", lambda f: print(f+" ?present?"))
    run_if_present("demo/demofile.txt", lambda f:run("ls -l "+f) )