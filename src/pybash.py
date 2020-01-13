from pathlib import Path
import os, re, logging

log = logging.getLogger(__name__)


def run(cmd):
    log.info("Running: " + cmd)
    log.info(os.popen(cmd).read())
    log.info("=======================")


def run_if_present(fname: str, funx):
    if (Path("./" + fname)).exists():
        log.info("%s ===> %s" % (fname, str(funx.__name__)))
        funx(fname)
        return True
    else:
        # log.info ("%s does not exists skipped %s" % ( fname, str(funx.__name__)))
        return False


def run_if_missed(fname: str, funx):
    if not (Path("./" + fname)).exists():
        log.info("%s ===> %s" % (fname, str(funx.__name__)))
        funx(fname)
        return True
    else:
        # log.info ("%s exists skipped %s" % ( fname, str(funx.__name__)))
        return False


"""
Extract a var from a simple property file (with assignments)
Works only on a specific need
"""


def extract_var(fname, var_name):
    # Search for a simple assignment
    match_str = var_name + r"\s*=\s*(.*)"
    val_finder = re.compile(match_str)
    with open(fname, "r") as f:
        for l in f:
            fr = val_finder.findall(l)
            if len(fr) > 0:
                log.debug("Found ", var_name, fr[0])
                return fr[0]
    return None


def append_if_missed(fname, *args):
    for string_to_add in list(args):

        def appender(f):
            with open(f, "a") as fd:
                fd.write("\n" + string_to_add)

        run_if_unmarked(fname, string_to_add, appender)


def run_if_unmarked(fname, marker, fun_to_call_if_unmarked):
    # log.info("Mark search....",fname,marker)
    with open(fname, "r") as f:
        for line in f:
            if marker in line:
                # log.info(" %s Marker found, %s execution skipped" % (marker, fun_to_call_if_unmarked.__name__))
                return None
    log.info("%s ===> %s" % (fname, marker))
    return fun_to_call_if_unmarked(fname, marker)


def run_each(path, glob, func):
    """
    Scan files
    """
    import fnmatch

    for root, dirs, filenames in os.walk(path):
        for fname in fnmatch.filter(filenames, glob):
            fullpath = os.path.join(root, fname)
            log.info("%s ===> %s" % (fullpath, str(func.__name__)))
            func(fullpath)
