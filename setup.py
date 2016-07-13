#!/usr/bin/env python
import setuptools #needed to enable develop
import subprocess

try:
    subprocess.call(['conda','install','--file','requirements.txt'])
except Exception as e:
    pass

from numpy.distutils.core import setup,Extension

ext = Extension('tsyganenko.tsygFort',
            sources=['fortran/'+f for f in ('geopack08.for','T96.f','T02.f')],
            f2py_options=['--quiet'])

setup (name = "Tsyganenko",
       version = "0.1.1",
       description = "wrapper for the Tsyganenko geomagnetic models",
       author = "Sebastien de Larquier, Michael Hirsch",
       author_email = "sdelarquier@vt.edu",
       url = "",
       long_description =
        """
For more information on the Tsyganenko gemagnetic field models, go to 
http://ccmc.gsfc.nasa.gov/models/modelinfo.php?model=Tsyganenko%20Model
        """,
       packages = ['tsyganenko'],
#       ext_modules = [ext],
       keywords=['Scientific/Space'],
       classifiers=[
                   "Programming Language :: Python/Fortran"
                   ]
        )

