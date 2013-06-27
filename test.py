
import cython

if not cython.compiled:
    print "I'm interpreted"
##     from math import sin

def f(r):
    s = sin(r)
    return s
    
r=3.141592654/3.0
print f(r)