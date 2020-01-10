
from pathlib import Path
import os,re

def run(cmd):
    print("Running: ",cmd)
    print(os.popen(cmd).read())
    print("=======================")

def run_if_present(fname: str, funx):
    if ( (Path("./"+fname)).exists()):
        print("%s ===> %s" % (   fname, str(funx.__name__)))
        funx(fname)
        return True
    else:
        #print ("%s does not exists skipped %s" % ( fname, str(funx.__name__))) 
        return False

def run_if_missed(fname: str, funx):
    if ( not (Path("./"+fname)).exists()):
        print("%s ===> %s" % ( fname, str(funx.__name__)  ))
        funx(fname)
        return True
    else:
        #print ("%s exists skipped %s" % ( fname, str(funx.__name__)))
        return False

"""
Extract a var from a simple property file (with assignments)
Works only on a specific need
"""
def extract_var(fname,var_name):
    # Search for a simple assignment 
    match_str=var_name+r"\s*=\s*(.*)"    
    val_finder=re.compile(match_str)
    with open(fname,"r") as f:
        for l in f:        
            fr=val_finder.findall(l)
            if(len(fr)>0):
                print("Found ",var_name,fr[0])
                return fr[0]
    return None

def append_if_missed(fname,*args):
    for string_to_add in list(args):
        def appender(f):
            with open(f,"a") as fd:
                fd.write("\n"+string_to_add)
        run_if_unmarked(fname,string_to_add, appender)


def run_if_unmarked(fname,marker,fun_to_call_if_unmarked):
    #print("Mark search....",fname,marker)
    with open(fname,"r") as f:
        for line in f:
            if marker in line:
                #print(" %s Marker found, %s execution skipped" % (marker, fun_to_call_if_unmarked.__name__))
                return None    
    print("%s mrk %s" % (fname, marker))
    return fun_to_call_if_unmarked(fname,marker)
