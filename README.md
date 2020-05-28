
# Runif
Idempotent and *minimal* python 3 library for rapid scripting.
Provide support for creating file, adding data to them, patching and so on.

# Why?
(Ba)sh scripting is very easy to setup. So we end up using it all the time for simple procedural script.

Sometimes is it useful to have idempotent script, like Ansible and Saltstack teach use, this script should only do an action if needed.

I have this need for a complex set of migration procedures.
I was unable to do it bash
It was an overkilll using Java

So runif popped out

Try the examples running them from the root directory

The run() function is very handy to fire direct command, like you would do in a bash script, like running git pull or so on

Note: runif it is NOT a replacement for Gradle, GNU Make, Maven, etc.

# Launch example
Install the package with
    > python setup.py install

Here an example of what happen if you run twice the *same* script:

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

# Unstable interfaces / Dev notes

    run_each               is still unstable
    run_if_modified        is brand new and not tested on a huge set of test cases. it is NOT thread safe


See   ./CHANGELOG.md for the last modification

# Tests

Install py.test with

    pip install pytest

run with
    PYTHONPATH=. pytest

The PYTHONPATH variable is used to ensure you are using the current version and not another possibly installed one on your env

See 
 https://docs.pytest.org/en/latest/example/index.html
for usage examples

# RELEASE HISTORY

v1.0.0 - Jan 2020 First draft API, lot of work needed
       - Added setup.py (not yet on python package index) and py.test minimal example
