#!/usr/bin/env python
from numpy.distutils.core import setup, Extension

ext = Extension('tsyganenko.tsygFort',
  sources=['tsyganenko/geopack08.pyf','tsyganenko/geopack08.for','tsyganenko/T96.f','tsyganenko/T02.f'])

setup (name = "Tsyganenko",
       version = "0.1",
       description = "wrapper to call fortran routines from the Tsyganenko models",
       author = "Sebastien de Larquier",
       author_email = "sdelarquier@vt.edu",
       url = "",
       long_description =
        """
For more information on the Tsyganenko gemagnetic field models, go to 
http://ccmc.gsfc.nasa.gov/models/modelinfo.php?model=Tsyganenko%20Model
        """,
       packages = ['tsyganenko'],
       ext_modules = [ext],
       keywords=['Scientific/Space'],
       classifiers=[
                   "Programming Language :: Python/Fortran"
                   ]
        )

