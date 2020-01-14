from pathlib import Path
import os, re, logging,hashlib

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


def internal_checksum(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def run_if_modified(fname: str, funx, cache_file=".pybash_cache"):
    import json
    if not (Path(cache_file)).exists():
        # run for sure
        log.info("%s = (md5) => %s" % (fname, str(funx.__name__)))
        funx(fname)
        db={}
        # checksum    
        db[fname]=internal_checksum(fname)         
        data2serialize=json.dumps(db, indent=True, sort_keys=True)
        with open(cache_file, "w") as f:
            f.write(data2serialize)
        return True
    else:
        # DB Exists: load it
        with open(cache_file, "r") as f:
             content=f.read()
        db=json.loads(content)
        new_checksum=internal_checksum(fname)
        if  (fname not in db) or (db[fname]!= new_checksum):
            db[fname]=new_checksum
            log.info("%s = (md5*) => %s" % (fname, str(funx.__name__)))
            funx(fname)
            data2serialize=json.dumps(db, indent=True, sort_keys=True)
            with open(cache_file, "w") as f:
                f.write(data2serialize)
            return True
        else:
            log.debug("%s = (md5) =STOP= %s" % (fname, str(funx.__name__)))
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


def run_each(path: str, glob: str, func):
    """
    Scan files and run in a sequential fashion.
    The func must return True if make some changes
    

    """
    import fnmatch
    counter=0
    for root, dirs, filenames in os.walk(path):
        for fname in fnmatch.filter(filenames, glob):
            fullpath = os.path.join(root, fname)                                
            r=func(fullpath)
            if r== True:
                counter=counter+1    
    log.info("File-func changes: %s" %(counter))
    return counter

def run_each_async(path: str, glob: str, func, pool_size:int =max(1,os.cpu_count()-1)):
    """
    Scan files and run in a multi-process fashion.
    The func must return True if make some changes 

    The function must AVOID calling not hread-safe function like  run_if_modified

    Spawn overhead is low but parallelism is not high because of ThreadPoolExecutor

    """
    import fnmatch
    from  concurrent.futures import ThreadPoolExecutor
    log.info("Processes: %s" %( pool_size))
    executor= ThreadPoolExecutor(max_workers=pool_size, thread_name_prefix=path+"_")
    futures=[]
    counter=0
    for root, dirs, filenames in os.walk(path):
        for fname in fnmatch.filter(filenames, glob):
            fullpath = os.path.join(root, fname)                                
            futures.append(executor.submit(func, fullpath))        
    for fut in futures:
        if fut.result(timeout=3) == True:
            counter=counter+1
    executor.shutdown(wait=True)
    log.info("File-func changes: %s" %(counter))
    return counter
       