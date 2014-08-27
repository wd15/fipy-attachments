from fipy import *
from fipy.meshes.numMesh.grid2D import Grid2D
Lval = 2.      # half length of a periodic entitiy
lval = 1.      # half length of the slug
Hval = 0.1     # half height of the microchannel
hval = 0.01    # distance wall to slug
nxtot = 200    # intervalnr  in x direction
nytot = 40     # intervalnr  in y direction
dx = Lval / float(nxtot)
dy = Hval / float(nytot)
nx1 = (Lval-lval)/2/dx
nx2 = lval/dx
ny1 = Hval/dy
ny2 = hval/dy
mesh1 = Grid2D(dx=dx, dy=dy, nx=2*nx1, ny=ny1) + [[-(Lval-lval)/2], [0]]
mesh2 = Grid2D(dx=dx, dy=dy, nx=nx2/2, ny=ny2) + [[(Lval-lval)/2],[0]]
mesh3 = Grid2D(dx=dx, dy=dy, nx=nx2/2, ny=ny2) + [[-Lval/2], [0]]
mesh1 = mesh1 + mesh2