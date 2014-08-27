#!/usr/bin/env python

## 
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "mesh20x20periodic.py"
 #
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #  Author: Benny Malengier  <bm@cage.ugent.be>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 # ###################################################################
 ##

r"""

This example solves a diffusion problem and demonstrates the use of
applying boundary condition patches.

.. index:: PeriodicGrid2D

>>> from fipy import *

>>> nx = 20
>>> ny = nx
>>> dx = 1.
>>> dy = dx
>>> L = dx * nx
>>> mesh = PeriodicGrid2D(dx=dx, dy=dy, nx=nx, ny=ny)

We create a :class:`~fipy.variables.cellVariable.CellVariable` and initialize it to
a left corner region with value 1., and zero outside, for a total of 25 mass.
Under diffusion, this should evolve to 0.0625
    
>>> phi = CellVariable(name = "solution variable",
...                    mesh = mesh,
...                    value = 1.)
>>> xc, yc = mesh.getCellCenters()
>>> phi.setValue(0., where=(xc > 5) | (yc > 5))

and then create a diffusion equation.  This is solved by default with an
iterative conjugate gradient solver.  

>>> D = 1.
>>> eq = TransientTerm() == DiffusionTerm(coeff=D)

There is no need to apply boundary conditions. Same final result should be 
obtained with no flux boundary however.

We create a viewer to see the results

.. index::
   module: fipy.viewers

>>> if __name__ == '__main__':
...     viewer = Viewer(vars=phi)
...     viewer.plot()

and solve the equation by repeatedly looping in time:

>>> timeStepDuration = 10 * 0.9 * dx**2 / (2 * D)
>>> steps = 17
>>> for step in range(steps):
...     if __name__ == '__main__':
...         if step%2==0:
...             print 'Time', step*timeStepDuration, 'shown. '
...             raw_input('Press <return> to proceed...')
...     eq.solve(var=phi,
...              dt=timeStepDuration)
...     if __name__ == '__main__':
...         viewer.plot()

We can test the value of the center cell.

>>> if __name__ == '__main__':
...     print 'Equilibrium value=', phi(((L/2,), (L/2,)))
>>> print numerix.allclose(phi(((L/2,), (L/2,))), 0.0625, atol = 1e-3)
1

>>> if __name__ == '__main__':
...     raw_input("Implicit steady-state diffusion. Press <return> to proceed...")

-----

We can also solve the steady-state problem directly
>>> phi2 = CellVariable(name = "solution variable",
...                    mesh = mesh,
...                    value = 1.)
>>> xc, yc = mesh.getCellCenters()
>>> phi2.setValue(0., where=(xc > 5) | (yc > 5))
>>> if __name__ == '__main__':
...     viewer = Viewer(vars=phi2)
...     viewer.plot()

>>> DiffusionTerm().solve(var=phi2)
>>> if __name__ == '__main__':
...     viewer.plot()

and test the value of the bottom-right corner cell.

>>> if __name__ == '__main__':
...     print 'Steady State Equilibrium value=', phi2(((L/2,), (L/2,)))
>>> print numerix.allclose(phi2(((L/2,), (L/2,))), 0.0625, atol = 1e-3)
1

>>> if __name__ == '__main__':
...     raw_input("Finished. Press <return> to close...")
"""

__docformat__ = 'restructuredtext'


if __name__ == '__main__':
    import fipy.tests.doctestPlus
    exec(fipy.tests.doctestPlus._getScript())

