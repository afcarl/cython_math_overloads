
import cython

if not cython.compiled:
    print "I'm interpreted"
    exec('from math import sin,cos, log')

from math import log as py_log

def f(r):
    s = log(r)
    return s
    
def g(r):
    """ Always using the python version """
    s = py_log(r)
    return s
    
if __name__=='__main__':
    r=3.141592654/3.0
    print f(r)