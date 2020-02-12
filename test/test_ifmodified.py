import pytest

from pybash import *

def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


def test_checksum(tmpdir):
    print(tmpdir)
    with open(tmpdir+"/test.txt","w+") as f:
        f.write("Test")
    def checker(fname):        
        print("Modified::",fname)
    #run_if_modified(tmpdir+"/test.txt",checker,cache_file=str(tmpdir+"/test-cache-file.txt"))
    assert run_if_modified(str(tmpdir+"/test.txt"),checker)
    assert run_if_modified(str(tmpdir+"/test.txt"),checker) == False

