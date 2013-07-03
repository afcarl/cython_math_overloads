from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import sys

import Cython.Compiler.Options

#This will generate HTML to show where there are still pythonic bits hiding out
Cython.Compiler.Options.annotate = True

if len(sys.argv) == 1:
    sys.argv += ['build_ext','--inplace']

#Note: the name of the module MUST be the same as the name of the pure Python file
ext_modules = [Extension("test", ["test.py"]),
               ]

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

import timeit
print timeit.Timer('test.f(0.3)','import test').timeit(10000000)
print timeit.Timer('test.g(0.3)','import test').timeit(10000000)