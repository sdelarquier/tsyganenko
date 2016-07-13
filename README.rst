===================================
Tsyganenko Geomagnetic Field Model
===================================


Fortran files and their scientific content have been developed by N.A. Tsyganenko and colleagues.

Installation
============
sudo is NOT needed or desired::

    cd fortran
    make
    make install
    python setup.py develop

Use
====
To use this module, simply follow the example provided in the tsygTrace object docstring::

    import tsyganenko
    tsyganenko.tsygTrace?

You can also use ipython notbook to visualize a more detailed example::

    ipython notebook --pylab=inline

If you run the above command from this repository you should see a notebook called 'Tsyganenko - Python examples'. If you run the above command from anywhere on your computer, you can drag and drop the file called 'Tsyganenko - Python examples.ipynb' to the notebok dashboard.
