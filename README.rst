===============================
Langevin_dynamics
===============================

The first project of CHE477 2016:  Langevin project

.. image:: https://img.shields.io/pypi/v/Langevin_dynamics.svg
        :target: https://pypi.python.org/pypi/Langevin_dynamics

.. image:: https://img.shields.io/travis/hudalao/Langevin_dynamics.svg
        :target: https://travis-ci.org/hudalao/Langevin_dynamics

.. image:: https://readthedocs.org/projects/Langevin-dynamics/badge/?version=latest
        :target: https://Langevin-dynamics.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/hudalao/Langevin_dynamics/shield.svg
        :target: https://pyup.io/repos/github/hudalao/Langevin_dynamics/
        :alt: Updates
         
.. image:: https://coveralls.io/repos/github/hudalao/Langevin_dynamics/badge.svg
        :target: https://coveralls.io/github/hudalao/Langevin_dynamics

Langevin_dynamics


* Free software: MIT license
* Documentation: https://Langevin-dynamics.readthedocs.io.


Features
--------
Two Classes are included in this version:

1. This first clasee Langevin_dynamics() is the main class. Two function are included.
   The tran_input_float function() can read the input file with a line. The format of this file is  
   x0: initial position; v0: initial velocity; T: temperature; damp: dampling coefficient; 
   delta_t: time step; Time: total time ; m: the mass of the particle

   The dynamics() is used to calcualte the position and velocity at every time points. The velocity
   verlet integration has been used.

2. The second class Pot_Energy_Gen is the class to generate the potential energy surface described by   function (a-b*(x-L/2)^2)^2, where a and b are constants, L is the range of movement of the
   particle. Function space_grid() creates the space grid determined by the number of the grid N.
   Function pot() create a array contains potential energy at every space points. Function force()
   creates a array contains force at every space points.  


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

