#!/usr/bin/env python
import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from pybash import *

from pathlib import Path
import os, re

def step1(dir_to_build):
    (Path(dir_to_build)).mkdir()


def step2(fname):
    with open(fname, "a") as f:
        f.write("Example\n")

def step3(fname,marker):
    with open(fname, "a") as f:
        f.write("demodata="+marker+"\n")
        f.write("# Marker inserted above\n")
        f.write("daitangio=rulez")

if __name__ == "__main__":
    run_if_missed("demo", step1)
    run_if_missed("demo/demofile.txt", step2)
    run_if_unmarked("demo/demofile.txt","Step3",step3)
    val=extract_var("demo/demofile.txt", "daitangio")
    assert val == "rulez"