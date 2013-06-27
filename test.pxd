
cimport cython
import cython

from cmath cimport sin

@cython.locals(r=cython.double)
cpdef double f(double r)