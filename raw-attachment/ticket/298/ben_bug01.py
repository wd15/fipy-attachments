from fipy import *
from fipy.meshes.numMesh.grid2D import Grid2D
from fipy.tools import numerix
import numpy as np

Lval = 2.
lval = 1.
Hval = 0.1
hval = 0.01
vval = 1.

D1 = 0.1
D2 = 0.2
K = 0.8

dt = 0.001
endT = 10
nt = endT/dt
dx = 0.01
dy = 0.0025
nxtot = Lval/dx
nx1 = (Lval-lval)/2/dx
nx2 = lval/dx
ny1 = Hval/dy
nytot = ny1
ny2 = hval/dy

mesh = PeriodicGrid2DLeftRight(dx=dx, dy=dy, 
                               nx=nxtot, ny=nytot) + [[-Lval/2], [0]]
#mesh = Grid2D(dx=dx, dy=dy, 
#                               nx=nxtot, ny=nytot) + [[-Lval/2], [0]]
#mesh.connectFacesLR()
xfc, yfc = mesh.getFaceCenters()
intedge = ((xfc == -(Lval-lval)/2) & (yfc >= hval)) | \
    ((xfc == (Lval-lval)/2) & (yfc >= hval))  | \
    ((-(Lval-lval)/2 >  xfc) & (yfc == hval)) | \
    ((xfc >  (Lval-lval)/2) & (yfc == hval))
slug = ((xfc <= -(Lval-lval)/2) & (yfc >= hval)) | \
       ((xfc >= (Lval-lval)/2) & (yfc >= hval)) 
solvent = ~slug
xc, yc = mesh.getCellCenters()
slugc = ((xc < -(Lval-lval)/2) & (yc > hval)) | \
       ((xc > (Lval-lval)/2) & (yc > hval)) 
solventc = ~slugc

phi = CellVariable(name = "solution variable",
                   mesh = mesh,
                   value = 1.)
phi.setValue(0., where=slugc)
viewer1 = Viewer(vars=(phi,))
viewer1.plot()
raw_input('Finished')