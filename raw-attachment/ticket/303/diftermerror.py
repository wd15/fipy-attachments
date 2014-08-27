
from fipy import *
from fipy.meshes.numMesh.grid2D import Grid2D
import numpy as np

old = True
mesh = Grid2D(dx=0.1, dy=0.1, nx=10, ny=10)

ap = CellVariable(mesh=mesh, value=0.01)
if old:
    #fails on new numpy
    coeff = mesh._getFaceAreas() * mesh._getCellDistances() / ap.getArithmeticFaceValue()
else:
    #works
    coeff = 1/ap.getArithmeticFaceValue() * mesh._getFaceAreas() * mesh._getCellDistances()
print np.array(ap.getArithmeticFaceValue(), copy=False, subok=True)
print type(mesh._getFaceAreas()), type(mesh._getCellDistances())
print 'coval', type(coeff), type(coeff.getValue())
result = coeff * numerix.identity(mesh.getDim())