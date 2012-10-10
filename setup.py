#!/usr/bin/env python
from numpy.distutils.core import setup, Extension

ext = Extension('tsyganenko.tsygFort',sources=['geopack08.pyf','geopack08.for','T96.f','T02.f'])

setup (name = "Tsyganenko",
       version = "0.1",
       description = "wrapper to call fortran routines from the Tsyganenko models",
       author = "Sebastien de Larquier",
       author_email = "sdelarquier@vt.edu",
       url = "",
       long_description =
        """
This module provides a high level class to calculate traces along
geomagnetic field lines. Calculations are performed by the Tsyganenko
geomagnetic field models, and all fortran subroutines are accessible 
outside the wrapper class.

For more information on the Tsyganenko gemagnetic field models, go to 
http://ccmc.gsfc.nasa.gov/models/modelinfo.php?model=Tsyganenko%20Model
        """,
       packages = ['tsyganenko'],
       keywords=['Scientific/Space'],
       classifiers=[
                   "Programming Language :: Python/Fortran"
                   ]
        )

