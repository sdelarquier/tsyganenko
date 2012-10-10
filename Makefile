#!/bin/bash

DIR := tsyganenko/

all:
	# f2py --overwrite-signature  ${DIR}geopack08.for ${DIR}T96.f ${DIR}T02.f -m tsygFort -h ${DIR}geopack08.pyf
	gfortran -w -O2 -fbacktrace -fno-automatic -fPIC -c ${DIR}geopack08.for ${DIR}T96.f ${DIR}T02.f
	f2py --f77flags="-w" -c ${DIR}geopack08.pyf ${DIR}geopack08.for ${DIR}T96.f ${DIR}T02.f
	python setup.py install

clean:
	find . -type f -name "*.o" | xargs rm -f
	find . -type f -name "*.so" | xargs rm -f
	# find ${DIR} -type f -name "*.pyf" | xargs rm -f
