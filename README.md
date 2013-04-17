# Tsyganenko Geomagnetic Field Model: Python wrappers

## Licence

Though edits had to be made to the fortran code to accomodate f2py compilation, all fortran files and their scientific content have been developped by N.A. Tsyganenko and colleagues.

I am only responsible for the python wrappers, which provide a convenient python class as an interface with the fortran subroutines.

## Installation

To install the Tsyganenko python module, from this directory run:  

    cd tsyganenko
    make clean
    make
    cd ..
    sudo python setup.py install

## Use

To use this module, simply follow the example provided in the tsygTrace object docstring.

    import tsyganenko
    tsyganenko.tsygTrace?

You can also use ipython notbook to visualize a more detailed example.

    ipython notebook --pylab=inline

If you run the above command from this repository you should see a notebook called 'Tsyganenko - Python examples'. If you run the above command from anywhere on your computer, you can drag and drop the file called 'Tsyganenko - Python examples.ipynb' to the notebok dashboard.
