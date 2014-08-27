from fipy import *
import numpy as N
import pylab as P

###set up size of 2-D domain
nx=20.
ny=20.
dx=5
dy=5
###make uniform 2-D mesh
mesh=Grid2D(nx=nx,ny=ny,dx=dx,dy=dy)
###set variable to solve
head=CellVariable(name='hydraulic head',
                  mesh=mesh,
                  value=0)
###set hydraulic conductivity
kond=CellVariable(name='hydraulic conductivity',
                  mesh=mesh,
                  rank=0,
                  value=1.e-4)
###set specific storativity
store=CellVariable(name='specific storativity',
                   mesh=mesh,
                   value=1.e-3)
###ground-water flow equation
eq=TransientTerm(store)==ImplicitDiffusionTerm(kond)

bndry=(FixedValue(faces=mesh.getFacesTop(),value=10.0))
