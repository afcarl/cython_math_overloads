from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import sys

if len(sys.argv) == 1:
    sys.argv += ['build_ext', '--inplace']

#Note: the name of the module MUST be the same as the name of the pure Python file
ext_modules = [Extension("test", ["test.py"]),
               Extension("cmath", ["cmath.pyx"])
               ]

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)