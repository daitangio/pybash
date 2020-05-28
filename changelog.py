import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/src")
from runif import *

from pathlib import Path
import os, re,logging
import sys

def make_change_log(unused):
    run("git log -25 --decorate --oneline >CHANGELOG.md")
    run("git diff -w CHANGELOG.md")

def noop(unused=None, unused2=None):
    return True

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s]  %(threadName)s %(thread)d %(filename)s.%(funcName)s %(message)s',
                    level=logging.INFO)
    def check(fname):
        return run_if_modified(fname, noop)
    c=run_each(".","*.py", check)
    c=c+run_each(".","README.md", check)
    if (c >0 ):
        make_change_log(c)
        print("Changed files:",c )
    else:
        if run_if_missed("CHANGELOG.md", make_change_log):
            print("CREATED")            
        else:
            print("?NO MODIFICATION DONE")            
    if len(sys.argv) >=3:
        tag=sys.argv[1]
        comment=sys.argv[2]
        print("Tagging",tag, "Comment:",comment)
        run("git commit -a -m ",comment)
        run("git tag ",tag)
    #run_if_modified("src/runif.py",make_change_log)
