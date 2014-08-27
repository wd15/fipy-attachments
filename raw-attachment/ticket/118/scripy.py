#!/usr/bin/env python

from fipy import *

gasConstant = 8.3
temperature = 1. / gasConstant
molarWeight = 1.
viscosity = 1.
vbar = 1. / 3.
e1 = -1.5
epsilon1 = 2e-4 * gasConstant
liquidDensity = 2.04
gasDensity = 0.17

liquidDensity = 2.04325
gasDensity = 0.177207
avgDensity = (liquidDensity + gasDensity) / 2.0

velocityRelaxation = 0.8
densityRelaxation = 0.5
L = 1.
maxdt = 1e-20
dt = Variable(maxdt)

from fipy.tools.parser import parse
avgDensity = parse('--density', action='store', type='float', default=avgDensity)

dx = 0.1
nx = int(L / dx)

mesh = Grid1D(nx=nx, dx=dx)

numerix.random.seed(135851)
density = CellVariable(mesh=mesh, value=avgDensity * (1 + 0.01 * (2 * numerix.random.rand(mesh.getNumberOfCells()) - 1)), hasOld=1, name='density')
avgDensity = numerix.sum(density[:]) / mesh.getNumberOfCells()

densityCorrection = CellVariable(mesh=mesh)
velocity = []
for dim in range(mesh.getDim()):
    velocity.append(CellVariable(mesh=mesh, hasOld=1))

vectorFaceVelocity = VectorFaceVariable(mesh=mesh)
ap = CellVariable(mesh=mesh)

faceDensity = density.getArithmeticFaceValue()

classicalPressure = e1 * density**2 / molarWeight**2 + gasConstant * temperature * density / (molarWeight - vbar * density)

nonClassicalPressure = classicalPressure \
                       - temperature * epsilon1 * density * density.getFaceGrad().getDivergence() \
                       + temperature * epsilon1 / 2 * density.getGrad().getMag()**2

classicalPressureDerivative = 2 * e1 * density / molarWeight**2 + gasConstant * temperature * molarWeight / (molarWeight - vbar * density)**2


apCoeff = mesh._getFaceAreas() * mesh._getCellDistances() * (1. / ap).getArithmeticFaceValue()
densityCoeff = faceDensity * apCoeff

densityDiffTerm = DiffusionTerm(classicalPressureDerivative.getArithmeticFaceValue() * densityCoeff)

class FaceGradAverage(VectorFaceVariable):
    def __init__(self, cellGrad):
        VectorFaceVariable.__init__(self, cellGrad.getMesh())
        self.cellGrad = self._requires(cellGrad)

    def _calcValue(self):
        id1, id2 = self.mesh._getAdjacentCellIDs()

        grad1 = numerix.take(self.cellGrad.getNumericValue(),id1)
        grad2 = numerix.take(self.cellGrad.getNumericValue(),id2)

        avg = (grad1 + grad2) / 2.0

        for id in mesh.getExteriorFaces():
            avg[id] = 0

        return avg

faceGradAverage = FaceGradAverage(nonClassicalPressure.getGrad())

faceGrad = nonClassicalPressure.getFaceGrad()

interVectorFaceVelocity = vectorFaceVelocity - apCoeff * (faceGrad - faceGradAverage) 

correction = densityCoeff * (classicalPressureDerivative.getFaceGrad() - temperature * epsilon1 * density.getFaceGrad().getDivergence().getFaceGrad())

higherOrderTerm = DiffusionTerm((temperature * epsilon1 * densityCoeff * faceDensity,1))

densityCorrectionEq = TransientTerm() == \
                     UpwindConvectionTerm(-vectorFaceVelocity + correction, diffusionTerm=densityDiffTerm) + \
                     densityDiffTerm - \
                     higherOrderTerm - \
                     (density - density.getOld()) / dt - \
                     (faceDensity * interVectorFaceVelocity).getDivergence()

velocityEqs = []

for dim in range(mesh.getDim()):
       
   dimVec = numerix.zeros(mesh.getDim())
   dimVec[dim] = 1
       
   velocityDiffTerm = DiffusionTerm(viscosity)
       
   extraDiffTerm = 0
       
   for dim1 in range(mesh.getDim()):
       dim1Vec = numerix.zeros(mesh.getDim())
       dim1Vec[dim1] = 1
       extraDiffTerm += (viscosity * (velocity[dim1].getFaceGradAverage().dot(dimVec)) * dim1Vec).getDivergence()

   velocityEqs.append(TransientTerm(density)  == \
                      PowerLawConvectionTerm(-faceDensity * vectorFaceVelocity,
                                             diffusionTerm=velocityDiffTerm) \
                      + velocityDiffTerm \
                      + extraDiffTerm \
                      - nonClassicalPressure.getGrad().dot(dimVec))
#
#
BCs = (FixedValue(value=0, faces=mesh.getExteriorFaces()),)
#
densitySolver = LinearLUSolver()
flowSolver = LinearLUSolver()
#
viewer = make(density, limits={'datamax' : 0.1 + max(max(density), liquidDensity) , 'datamin' : 0.0})
pviewer0 = make(nonClassicalPressure, title='nonClassicalPressure')
pviewer1 = make(classicalPressure, title='classicalPressure')
vviewer = make(velocity[0])
step = 0
while abs(max(nonClassicalPressure) - min(nonClassicalPressure)) > 1e-5:
    step += 1
    if __name__ == '__main__':
        print 'step',step
    for dim in range(mesh.getDim()):
        velocity[dim].updateOld()
    density.updateOld()

    velocityRes = 1e+10
    densityCorrectionRes = 1e+10
    sweep = 0

    tmpArray = numerix.zeros(mesh.getNumberOfCells(), 'd')
    
    while max(velocityRes, densityCorrectionRes) > 1e-1:
##        import gc
##        gc.collect()
        
        maxdt = maxdt * 10

        maxvel = 1e-10
        for dim in range(mesh.getDim()):
            maxvel = max(max(abs(velocity[dim])), maxvel)

            dt.setValue(dx / maxvel / 1.0)
        
        dt.setValue(min(maxdt, dt.getValue()))
        if step < 100:
            dt.setValue(min(dt.getValue(), 10.0))
        else:
            dt.setValue(min(dt.getValue(), 100.0))
        
        velocityRes = 0.0

        for dim in range(mesh.getDim()):
            if dim == 0:
                velocityEqs[dim].cacheMatrix()

            tmp = velocityEqs[dim].sweep(velocity[dim], dt=dt, boundaryConditions=BCs, solver=flowSolver, underRelaxation=velocityRelaxation)
            velocityRes = max(velocityRes, tmp)

            if dim == 0:
                ap.setValue(velocityEqs[dim].getMatrix().takeDiagonal())
    
            vectorFaceVelocity[:,dim] = velocity[dim].getArithmeticFaceValue()
            for id in mesh.getExteriorFaces():
                vectorFaceVelocity[id] = 0.

        densityCorrection.setValue(0)
        densityCorrectionEq.cacheRHSvector()
        densityCorrectionRes = densityCorrectionEq.sweep(densityCorrection, dt=dt, solver=densitySolver)
        densityCorrectionRHS = densityCorrectionEq.getRHSvector()
##        density.setValue(numerix.array(density.getValue() + densityRelaxation * densityCorrection.getValue()))

        density.setValue(density[:] + densityRelaxation * densityCorrection[:])
        
        for dim in range(mesh.getDim()):
            velocityCorrection = (classicalPressureDerivative * densityCorrection - temperature * epsilon1 * \
                                  (densityCorrection * density.getFaceGrad().getDivergence() + \
                                   density * densityCorrection.getFaceGrad().getDivergence() - \
                                   numerix.dot(density.getGrad(),densityCorrection.getGrad()))).getGrad()[:,dim]
            
            velocity[dim].setValue(velocity[dim] - velocityCorrection[:] / ap * mesh.getCellVolumes())
            vectorFaceVelocity[:,dim] = velocity[dim].getArithmeticFaceValue()
            for id in mesh.getExteriorFaces():
                vectorFaceVelocity[id] = 0.        
        sweep += 1
        if __name__ == '__main__':
            print 'densityRes',densityCorrectionRes
            print 'velocityRes',velocityRes
            print 'densityCorrectionRHS',max(abs(densityCorrectionRHS))
            ##viewer.plot()
            ##pviewer0.plot()
            ##pviewer1.plot()
            ##vviewer.plot()
#
print numerix.allclose(density.sum() / mesh.getNumberOfCells(), avgDensity)
# Expected:
## True
if avgDensity >= liquidDensity or avgDensity <= gasDensity:
    maxDensity = minDensity = avgDensity
else:
    maxDensity = liquidDensity
    minDensity = gasDensity
print numerix.allclose(maxDensity, max(density), atol=1e-3)
# Expected:
## True
print numerix.allclose(minDensity, min(density), atol=1e-3) 
# Expected:
## True
print numerix.allclose(velocity[0], 0, atol=2e-6)
# Expected:
## True
print numerix.allclose(nonClassicalPressure, e1 * maxDensity**2 / molarWeight**2 + gasConstant * temperature * maxDensity / (molarWeight - vbar * maxDensity), atol=1e-2)
# Expected:
## True

