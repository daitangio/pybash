ALPHA QUALITY v1.0.0
*This library is still alpha quality software*

# pybash
Idempotent and *minimal* python 3 library for rapid scripting.
Provide support for creating file, adding data to them, patching and so on.

# Why?
Bash scripting is very easy to setup. So we end up using it all the time for simple procedural script.

Sometimes is it useful to have idempotent script, like Ansible and Saltstack teach use, this script should only do an action if needed.

I have this need for a complex set of migration procedures.
I was unable to do it bash
It was an overkilll using Java

So pybash popped out

Try the examples running them from the root directory

The run() function is very handy to fire direct command, like you would do in a bash script, like running git pull or so on

Note: For complex tasks, take alook at GNU Make

# Launch example

Here an example of what happen if you run twice the *same* script:

    $  python examples/stepByStep.py
    [INFO] pybash.py.run_if_missed demo ===> step1
    [INFO] pybash.py.run_if_missed demo/demofile.txt ===> step2
    [INFO] pybash.py.run_if_missed demo/demofile2.c ===> step2
    [INFO] pybash.py.run_if_unmarked demo/demofile.txt ===> Step3
    [INFO] pybash.py.run_if_present demo/demofile.txt ===> <lambda>
    demo/demofile.txt present!
    [INFO] pybash.py.run_each demo\demofile2.c ===> <lambda>
    ** demo\demofile2.c
    
    $  python examples/stepByStep.py
    [INFO] pybash.py.run_if_present demo/demofile.txt ===> <lambda>
    demo/demofile.txt present!
    [INFO] pybash.py.run_each demo\demofile2.c ===> <lambda>
    ** demo\demofile2.c

# Unstable interfaces / Dev notes

    run_each               is still unstable
    run_if_modified        is brand new and not tested on a huge set of test cases. it is NOT thread safe


See   ./CHANGELOG.md for the last modification