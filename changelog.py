import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/src")
from pybash import *

from pathlib import Path
import os, re,logging


def make_change_log(changed_files):
    run("git log -10 --decorate --oneline >CHANGELOG.md")
    print("Changed files:",changed_files )

if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s]  %(threadName)s %(thread)d %(filename)s.%(funcName)s %(message)s',
                    level=logging.INFO)
    def check(fname):
        return run_if_modified(fname, lambda unused: True)
    c=run_each(".","*.py", check)
    c=c+run_each(".","README.md", check)
    if (c >0 ):
        make_change_log(c)
    else:
        print("?NO MODIFICATION DONE")
    #run_if_modified("src/pybash.py",make_change_log)
