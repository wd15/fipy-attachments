from fipy import *
from fipy.meshes.numMesh.grid2D import Grid2D
from fipy.tools import numerix
import numpy as np

Lval = 2.
lval = 1.
Hval = 0.1
hval = 0.01

dt = 0.0001
endT = 0.017
nt = endT/dt
dx = 0.01
dy = 0.0025
nxtot = Lval/dx
nx1 = (Lval-lval)/2/dx
nx2 = lval/dx
ny1 = Hval/dy
nytot = ny1
ny2 = hval/dy

mesh1 = PeriodicGrid2DLeftRight(dx=dx, dy=dy, 
                    nx=nxtot, ny=nytot) 

xc1, yc1 = mesh1.getCellCenters()

a=mesh1._getFaceCellToCellNormals()
a1=mesh1._getFaceNormals()

print 'face normal:', a[0][8200],a[1][8200]
print 'cell cell normal:', a1[0][8200],a1[1][8200]

sys.exit(0)    

