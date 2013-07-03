
cimport cython

from libc.math cimport sin, cos, log, M_PI as pi, M_E as e, sqrt

@cython.locals(r=cython.double)
cpdef double f(double r)