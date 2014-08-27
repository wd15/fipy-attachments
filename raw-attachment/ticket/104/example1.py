#!/usr/bin/env python

r"""

This section will present an example of using Fipy to model the
superfill process. The example will be fairly simple and use unly one
additive preadsorbed onto the interface. All the code for the problem
will be included in this example. The example demonstrates how to
build the mesh, create the required variables, set up a level set
equation and view the results.
The following notation:

    >>> print 'something'
    something

indicates a python command prompt. This script can be run uisng python
and FiPy. To check that you have python, type trh following at the
command prompt:

   $ python
   Python 2.4.3 (#1, Oct  4 2006, 18:56:48) 
   [GCC 4.0.1 (Apple Computer, Inc. build 5363)] on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 

or something like this, The ">>>" notation indicates a python command
prompt. You can type python commands at teh command prompt,

    >>> print 'something'
    something

where the line after ''>>>'' is the expected output. Also, version 1.1
of FiPy or better will be required to run this problem. To check that
FiPy is installed type

    >>> from fipy import *
    >>> print __version__ 
    1.1

First, the geometry for the problem for the problem needs to be created
We can choose our paramters values as follows,

    >>> PF = PhysicalField
    >>> trenchDepth = PF("1.0mu")

Here we have set a parameter ''ternchDepth'', set its value to 1 and
given it units of $\mu$m. We will define more if these units,

    >>> trenchWidth = PF("0.5mu")
    >>> trenchSpacing = PF("1.0mu")
    >>> boundaryLayerDepth = PF("1.0mu")
    >>> spaceBelowTrench = 0.1 * trenchDepth
    
A reduced boundary layer depth is used here to simplify the mesh.  The
parameters above can be used to create a mesh of the required size.

    >>> delta = trenchWidth / 50
    >>> nx = (spaceBelowTrench + trenchDepth + boundaryLayerDepth) / delta
    >>> ny = trenchSpacing / delta
    >>> mesh = Grid2D(dx=delta, dy=delta, nx=nx, ny=ny)

Create the distance variable,

    >>> narrowBandWidth = numberOfCellsInNarrowBand * cellSize
    >>> phi = DistanceVariable(mesh=mesh,
    ...                        value=-1,
    ...                        narrowBandWidth=narrowBandWidth,
    ...                        hasOld=1)
    >>> y = mesh.getCellCenters()[...,1]
    >>> phi.setValue(1, where=y > (trenchDepth + spaceBelowTrench))
    >>> phi.setValue(1, where=(y > spaceBelowTrench) &
                              (x > (trenchSpacing - trenchWidth) / 2.0) &
                              (x < (trenchSpacing + trenchWidth) / 2.0))
    >>> distanceVar.calcDistanceFunction(narrowBandWidth=1e10)
    
    >>> from fipy.models.levelSet.surfactant.surfactantVariable import \
    ...     SurfactantVariable
    >>> catalystVar = SurfactantVariable(
    ...     value=initialCoverage,
    ...     distanceVar=distanceVar)







physical constants,

   >>> faradaysConstant = 9.6e4
   >>> gasConstant = 8.314
   >>> transferCoefficient = 0.5

properties associated with the catalyst species,

   >>> rateConstant0 = 1.76
   >>> rateConstant3 = -245e-6
   >>> catalystDiffusion = 1e-9
   >>> siteDensity = 9.8e-6
   
properties of the cupric ions,

   >>> molarVolume = 7.1e-6
   >>> charge = 2
   >>> metalDiffusionCoefficient = 5.6e-10

parameters dependent on experimental constraints,

   >>> temperature = 298.
   >>> overpotential = -0.3
   >>> bulkMetalConcentration = 250.
   >>> catalystConcentration = 5e-3
   >>> catalystCoverage = 0.
      
parameters obtained from experiments on flat copper electrodes,

   >>> currentDensity0 = 0.26
   >>> currentDensity1 = 45.

general simulation control parameters,

   >>> cflNumber = 0.2
   >>> numberOfCellsInNarrowBand = 10
   >>> cellsBelowTrench = 10
   >>> cellSize = 0.1e-7
   
parameters required for a trench geometry,

   >>> trenchDepth = 0.5e-6
   >>> aspectRatio = 2.
   >>> trenchSpacing = 0.6e-6
   >>> boundaryLayerDepth = 0.3e-6
   
The hydrodynamic boundary layer depth (`boundaryLayerDepth`) is
intentionally small in this example to keep the mesh at a reasonable
size.

Build the mesh:


   >>> from fipy.tools.parser import parse
   >>> numberOfElements = parse('--numberOfElements', action='store',
   ...     type='int', default=-1)
   >>> numberOfSteps = parse('--numberOfSteps', action='store',
   ...     type='int', default=5)


   >>> from fipy.tools.numerix import sqrt, exp, max
   >>> if numberOfElements != -1:
   ...     pos = trenchSpacing * cellsBelowTrench / 4 / numberOfElements
   ...     sqr = trenchSpacing * (trenchDepth + boundaryLayerDepth) \
   ...           / (2 * numberOfElements)
   ...     cellSize = pos + sqrt(pos**2 + sqr)
   ... else:
   ...     cellSize = 0.1e-7

   >>> yCells = cellsBelowTrench \
   ...          + int((trenchDepth + boundaryLayerDepth) / cellSize)
   >>> xCells = int(trenchSpacing / 2 / cellSize)


   >>> from fipy.meshes.grid2D import Grid2D
   >>> mesh = Grid2D(dx=cellSize,
   ...               dy=cellSize,
   ...               nx=xCells,
   ...               ny=yCells)

A `distanceVariable` object,

.. raw :: latex

    $\phi$, is  required to store  the  position of the interface  .

The `distanceVariable` calculates its value so that it is a distance
function 

.. raw:: latex

   (\emph{i.e.} holds the distance at any point in the mesh from the electrolyte/metal
   interface at $\phi$ = 0) and $|\nabla\phi| = 1$.

   First, create the $\phi$ variable, which is initially set to -1 everywhere. 
   Create an initial variable,

..

   >>> narrowBandWidth = numberOfCellsInNarrowBand * cellSize
   >>> from fipy.models.levelSet.distanceFunction.distanceVariable import \
   ...     DistanceVariable        
   >>> distanceVar = DistanceVariable(
   ...    name='distance variable',
   ...    mesh= mesh,
   ...    value=-1,
   ...    narrowBandWidth=narrowBandWidth,
   ...    hasOld=1)

The electrolyte region will be the positive region of the domain while the metal
region will be negative.

   >>> bottomHeight = cellsBelowTrench * cellSize
   >>> trenchHeight = bottomHeight + trenchDepth
   >>> trenchWidth = trenchDepth / aspectRatio
   >>> sideWidth = (trenchSpacing - trenchWidth) / 2
   
   >>> x, y = mesh.getCellCenters()[...,0], mesh.getCellCenters()[...,1]
   >>> distanceVar.setValue(1, where=(y > trenchHeight) 
   ...                               | ((y > bottomHeight) 
   ...                                  & (x < xCells * cellSize - sideWidth)))

   >>> distanceVar.calcDistanceFunction(narrowBandWidth=1e10)

The `distanceVariable` has now been created to mark the interface. Some other
variables need to be created that govern the concentrations of various species.

.. raw:: latex

    Create the catalyst surfactant coverage, $\theta$, variable.
    This variable influences the deposition rate.

 ..

   >>> from fipy.models.levelSet.surfactant.surfactantVariable import \
   ...     SurfactantVariable
   >>> catalystVar = SurfactantVariable(
   ...     name="catalyst variable",
   ...     value=catalystCoverage,
   ...     distanceVar=distanceVar)

.. raw:: latex

    Create the bulk catalyst concentration, $c_{\theta}$,
    in the electrolyte,

..

   >>> from fipy.variables.cellVariable import CellVariable
   >>> bulkCatalystVar = CellVariable(
   ...     name='bulk catalyst variable',
   ...     mesh=mesh,
   ...     value=catalystConcentration)
   
Create the bulk metal ion concentration,

.. raw:: latex

    $c_m$,

in the electrolyte.
        
   >>> metalVar = CellVariable(
   ...     name='metal variable',
   ...     mesh=mesh,
   ...     value=bulkMetalConcentration)

The following commands build the `depositionRateVariable`,

.. raw:: latex

    $v$.

The `depositionRateVariable` is given by the following equation.

.. raw:: latex

    $$ v = \frac{i \Omega}{n F} $$

    where $\Omega$ is the metal molar volume, $n$ is the metal ion
    charge and $F$ is Faraday's constant. The current density is given
    by

    $$ i = i_0 \frac{c_m^i}{c_m^{\infty}} \exp{ \left( \frac{- \alpha F}{R T} \eta \right) } $$

    where $c_m^i$ is the metal ion concentration in the bulk at the
    interface, $c_m^{\infty}$ is the far-field bulk concentration of
    metal ions, $\alpha$ is the transfer coefficient, $R$ is the gas
    constant, $T$ is the temperature and $\eta$ is the
    overpotential. The exchange current density is an empirical
    function of catalyst coverage,

    $$ i_0(\theta) = b_0 + b_1 \theta $$

The commands needed to build this equation are,

   >>> expoConstant = -transferCoefficient * faradaysConstant \
   ...                / (gasConstant * temperature)
   >>> tmp = currentDensity1 \
   ...       * catalystVar.getInterfaceVar()
   >>> exchangeCurrentDensity = currentDensity0 + tmp
   >>> expo = exp(expoConstant * overpotential)
   >>> currentDensity = expo * exchangeCurrentDensity * metalVar \
   ...                  / bulkMetalConcentration
   >>> depositionRateVariable = currentDensity * molarVolume \
   ...                          / (charge * faradaysConstant)

.. raw:: latex

    Build the extension velocity variable $v_{\text{ext}}$. The extension
    velocity uses the

`extensionEquation` to spread the velocity at the interface to the
rest of the domain.

   >>> extensionVelocityVariable = CellVariable(
   ...     name='extension velocity',
   ...     mesh=mesh,
   ...     value=depositionRateVariable)   

Using the variables created above the governing equations will be
built.  The governing equation for surfactant conservation is given
by,

.. raw:: latex

    $$ \dot{\theta} = J v \theta + k c_{\theta}^i (1 - \theta) $$

    where $\theta$ is the coverage of catalyst at the interface,
    $J$ is the curvature of the interface, $v$ is the normal velocity
    of the interface, $c_{\theta}^i$ is the concentration of
    catalyst in the bulk at the interface. The value $k$ is given
    by an empirical function of overpotential,
    $$ k = k_0 + k_3 \eta^3 $$
    The above equation is represented by the \Class{AdsorbingSurfactantEquation}
    in \FiPy{}:

..

   >>> from fipy.models.levelSet.surfactant.adsorbingSurfactantEquation \
   ...             import AdsorbingSurfactantEquation
   >>> surfactantEquation = AdsorbingSurfactantEquation(
   ...     surfactantVar=catalystVar,
   ...     distanceVar=distanceVar,
   ...     bulkVar=bulkCatalystVar,
   ...     rateConstant=rateConstant0 \
   ...                    + rateConstant3 * overpotential**3)

.. raw:: latex

    The variable $\phi$ is advected by the

`advectionEquation` given by,

.. raw:: latex

    $$ \frac{\partial \phi}{\partial t} + v_{\text{ext}}|\nabla \phi| = 0 $$
    and is set up with the following commands:

..

   >>> from fipy.models.levelSet.advection.higherOrderAdvectionEquation \
   ...                import buildHigherOrderAdvectionEquation
   >>> advectionEquation = buildHigherOrderAdvectionEquation(
   ...     advectionCoeff=extensionVelocityVariable)

The diffusion of metal ions from the far field to the interface is
governed by,

.. raw:: latex

    $$ \frac{\partial c_m}{\partial t} = \nabla \cdot D \nabla  c_m $$

    where,

    $$ D = \begin{cases}
    D_m & \text{when $\phi > 0$,} \\
    0   & \text{when $\phi \le 0$}
    \end{cases} $$

    The following boundary condition applies at $\phi = 0$,
    $$ D \hat{n} \cdot \nabla c = \frac{v}{\Omega}. $$
    The \verb|MetalIonDiffusionEquation| is set up with the following commands.

..

   >>> from fipy.boundaryConditions.fixedValue import FixedValue
   >>> from fipy.models.levelSet.electroChem.metalIonDiffusionEquation \
   ...                      import buildMetalIonDiffusionEquation
   >>> metalEquation = buildMetalIonDiffusionEquation(
   ...     ionVar=metalVar,
   ...     distanceVar=distanceVar,
   ...     depositionRate=depositionRateVariable,
   ...     diffusionCoeff=metalDiffusionCoefficient,
   ...     metalIonMolarVolume=molarVolume,
   ... )

   >>> metalEquationBCs = FixedValue(faces=mesh.getFacesTop(), value=bulkMetalConcentration)

The `SurfactantBulkDiffusionEquation` solves the bulk diffusion of a
species with a source term for the jump from the bulk to an interface.
The governing equation is given by,

.. raw:: latex

    $$ \frac{\partial c}{\partial t} = \nabla \cdot D \nabla  c $$

where,

.. raw:: latex

    $$ D = \begin{cases}
    D_{\theta} & \text{when $\phi > 0$} \\
    0          & \text{when $\phi \le 0$}
    \end{cases} $$

The jump condition at the interface is defined by Langmuir
adsorption. Langmuir adsorption essentially states that the ability
for a species to jump from an electrolyte to an interface is
proportional to the concentration in the electrolyte, available site
density and a jump coefficient. The boundary condition

.. raw:: latex

    at $\phi = 0$ is given by,
    $$ D \hat{n} \cdot \nabla c = -k c (1 - \theta). $$
    The \verb|SurfactantBulkDiffusionEquation| is set up with the following commands.

..

   >>> from fipy.models.levelSet.surfactant.surfactantBulkDiffusionEquation \
   ...                 import buildSurfactantBulkDiffusionEquation
   >>> bulkCatalystEquation = buildSurfactantBulkDiffusionEquation(
   ...     bulkVar=bulkCatalystVar,
   ...     distanceVar=distanceVar,
   ...     surfactantVar=catalystVar,
   ...     diffusionCoeff=catalystDiffusion,
   ...     rateConstant=rateConstant0 * siteDensity
   ... )

   >>> catalystBCs = FixedValue(faces=mesh.getFacesTop(), value=catalystConcentration)
   
If running interactively, create viewers.

   >>> if __name__ == '__main__':
   ...     try:
   ...         from fipy.viewers.mayaviViewer.mayaviSurfactantViewer import MayaviSurfactantViewer
   ...         viewers = (
   ...             MayaviSurfactantViewer(distanceVar,
   ...                                    catalystVar.getInterfaceVar(),
   ...                                    zoomFactor=1e6,
   ...                                    limits={ 'datamax' : 1.0, 'datamin' : 0.0 },
   ...                                    smooth=1),)
   ...     except:
   ...         from fipy.viewers import make
   ...         viewers = (
   ...             make(distanceVar, limits={ 'datamin' :-1e-9 , 'datamax' : 1e-9 }),
   ...             make(catalystVar.getInterfaceVar()))
   ... else:
   ...     viewers = ()

The `levelSetUpdateFrequency` defines how often to call the
`distanceEquation` to reinitialize the `distanceVariable` to a
distance function.

   >>> levelSetUpdateFrequency = int(0.8 * narrowBandWidth \
   ...                               / (cellSize * cflNumber * 2))

The following loop runs for `numberOfSteps` time steps. The time step
is calculated with the CFL number and the maximum extension velocity.

.. raw:: latex

    $v$ to
    $v_\text{ext}$ throughout the whole domain using
    $\nabla\phi\cdot\nabla v_\text{ext} = 0$.

..

   >>> for step in range(numberOfSteps):
   ...
   ...     for viewer in viewers:
   ...         viewer.plot()
   ...
   ...     if step % levelSetUpdateFrequency == 0:
   ...         distanceVar.calcDistanceFunction()
   ...
   ...     extensionVelocityVariable.setValue(depositionRateVariable())
   ...
   ...     distanceVar.updateOld()
   ...     catalystVar.updateOld()
   ...     metalVar.updateOld()
   ...     bulkCatalystVar.updateOld()
   ...     distanceVar.extendVariable(extensionVelocityVariable)
   ...     dt = cflNumber * cellSize / max(extensionVelocityVariable)
   ...     advectionEquation.solve(distanceVar, dt=dt)
   ...     surfactantEquation.solve(catalystVar, dt=dt)
   ...     metalEquation.solve(var=metalVar, dt=dt,
   ...                         boundaryConditions=metalEquationBCs)
   ...     bulkCatalystEquation.solve(var=bulkCatalystVar, dt=dt,
   ...                                   boundaryConditions=catalystBCs)

The following is a short test case. It uses saved data from a
simulation with 5 time steps. It is not a test for accuracy but a way
to tell if something has changed or been broken.

   >>> import os
   >>> import examples.levelSet.electroChem
   >>> filepath = os.path.join(examples.levelSet.electroChem.__path__[0], 
   ...                         'test.gz')
   >>> from fipy.tools import dump
   >>> print catalystVar.allclose(dump.read(filepath), rtol=1e-4)
   1

   >>> if __name__ == '__main__':
   ...     raw_input('finished')

"""

__docformat__ = 'restructuredtext'

from fipy import __version__
print 'fipy version',__version__

from fipy import *

##units
mum = 1e-6
cm = 1e-2
mol = 1.
s = 1.
nm = 1e-9

## build the mesh
trenchDepth = 1.0 * mum
trenchWidth = 0.5 * mum
trenchSpacing = 1.0 * mum
boundaryLayerDepth = 1.0 * mum
spaceBelowTrench = 0.1 * trenchDepth
cellSize = trenchWidth / 20
ny = int((spaceBelowTrench + trenchDepth + boundaryLayerDepth) / cellSize)
nx = int(trenchSpacing / cellSize / 2) 
mesh = Grid2D(dx=cellSize, dy=cellSize, nx=nx, ny=ny)

## build the distance function
cellsInBand = 10
bandWidth = cellsInBand * cellSize
distanceVar = DistanceVariable(mesh=mesh,
                       value=-1,
                       narrowBandWidth=bandWidth,
                       hasOld=1)
X = mesh.getCellCenters()
x, y = X[...,0], X[...,1]
distanceVar.setValue(1, where=y > (trenchDepth + spaceBelowTrench))
distanceVar.setValue(1, where=(y > spaceBelowTrench) &
                      (x < trenchWidth / 2.0))

print 'nx * cellSize',nx * cellSize
print 'trenchWidth/2.0',trenchWidth / 2.0
raw_input("stopped")

##                      (x < (trenchSpacing + trenchWidth) / 2.0))
distanceVar.calcDistanceFunction(narrowBandWidth=1e10)

## build the surfactant variable
catalystVar = SurfactantVariable(value=0.1, distanceVar=distanceVar)

## build the ion variable
ionConcentration = 0.00025 * mol/cm**3
ionVar = CellVariable(mesh=mesh, value=ionConcentration )

## build the velocity

velocity = ionVar / ionConcentration * \
              ( 3.21 * nm/s + 660.0 * nm/s * catalystVar.getInterfaceVar())
extVelocityVar = CellVariable(mesh=mesh)

surfactantEquation = SurfactantEquation(distanceVar=distanceVar)

## build the advection equation
advectionEquation = buildHigherOrderAdvectionEquation(
    advectionCoeff=extVelocityVar)

## create the ion diffusion equation
metalEquation = buildMetalIonDiffusionEquation(
    ionVar=ionVar,
    distanceVar=distanceVar,
    depositionRate=velocity,
    diffusionCoeff=5.6e-6 * cm**2/s,
    metalIonMolarVolume=7.1 * cm**3/mol)
metalEquationBCs = FixedValue(faces=mesh.getFacesTop(), value=ionConcentration)

viewer = MayaviSurfactantViewer(distanceVar,
                                catalystVar.getInterfaceVar(),
                                zoomFactor=1 / mum,
                                limits={ 'datamax' : 1.0, 'datamin' : 0.0 },
                                smooth=1)

CFL = 0.2
updateFrequency = int(0.8 * bandWidth / (cellSize * CFL * 2))

for step in range(1000):
    if step % 10 == 0:
        viewer.plot()

    if step % updateFrequency == 0:
        distanceVar.calcDistanceFunction()

    extVelocityVar.setValue(velocity)

    distanceVar.updateOld()
    catalystVar.updateOld()
    ionVar.updateOld()

    distanceVar.extendVariable(extVelocityVar)
    dt = CFL * cellSize / max(extVelocityVar)

    advectionEquation.solve(distanceVar, dt=dt)
    surfactantEquation.solve(catalystVar, dt=dt)
    metalEquation.solve(ionVar, dt=dt,
                        boundaryConditions=metalEquationBCs)

    
##__docformat__ = 'restructuredtext'

##def _run():
##    import fipy.tests.doctestPlus
##    exec(fipy.tests.doctestPlus._getScript(__name__))
    
##if __name__ == '__main__':
##    _run()


