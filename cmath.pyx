
from libc.math cimport exp as _exp, log, M_PI as pi, M_E as e, sqrt, sin as _sin

cpdef double sin(double t):
    return _sin(t)