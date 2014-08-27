## This script was derived from
## '../fipy-models/jwarren/doubleObstacle/pure.py'

# This example combines a phase field problem, as given in
# ``examples/elphf/phase/input1D.py``,
# with a binary diffusion problem, such as described in the ternary example
# ``examples/elphf/diffusion/input1D.py``,
# on a 1D mesh
#
from fipy import *

delta_a=1e-5
Lx = 50*delta_a
Ly= Lx
#
nx = 100
ny = 100
#
#
#
#
dx = Lx / nx
dy = Ly/ny

##mesh = Grid1D(dx = dx,  nx = nx)
mesh = Grid2D(dx = dx, nx = nx,dy=dy,ny=ny)
#
# We create the phase field
#
temp = CellVariable(mesh = mesh, name = 'temperature', value = 0, hasOld = 1)
phiI= CellVariable(mesh = mesh, name = 'phiI', value = 0, hasOld = 0)
## New cell to face variable that assigns the non-zero value on either side of the
## face to the cell

D1= 1.0
D2= 5.0

# the chocies below give a angle of pg1-pg2/(pg1+pg2) = cos(theta)
# use theta param

import RandomArray
x, y =  mesh.getCellCenters()[...,0], mesh.getCellCenters()[...,1]
nparts=15
impurity_yes=0
l=15*dx
w=3*dx

for i in range(nparts):
    vx=(Lx)*RandomArray.random()
    vy=(Ly)*RandomArray.random()
    theta=numerix.pi*RandomArray.random()
    c=numerix.cos(theta)
    s=numerix.sin(theta)
    tx=c*(x-vx)+s*(y-vy)
    ty= -s*(x-vx)+c*(y-vy)
##    impurity_yes=(tx>=0.0)&(tx<=l)&(ty>0.0)&(ty<=w)|(impurity_yes)
    impurity_yes=(tx*tx+ty*ty<l*l)|(impurity_yes)

# initial conditions for droplet
temp.setValue(1)
temp.setValue(10,where=impurity_yes)
phiI.setValue(1,where=impurity_yes)

#
#
from fipy import *
#
Diff=(D1*phiI+(1-phiI)*D2).getArithmeticFaceValue()

tempeq = TransientTerm(coeff = (1.0)) - ImplicitDiffusionTerm(coeff = Diff)

viewer = make(vars = (temp,),limits={'datamin': 0.0, 'datamax': 10.0})
##imsave_phase=TSVViewer(vars=(phase,))
##imsave_con=TSVViewer(vars=(con,))
#
# ##     ...                           # limits = {'datamin': 0, 'datamax': 1}
#


##solver = LinearLUSolver()
solver = LinearPCGSolver()
##solver = LinearCGSSolver()
#
# ###############################
# #                             #
# #       Begin full exclusion  #
# #                             #
# ###############################
#
#

import datetime 
viewer.plot()

maxsweep=100
dt=1e-12
##import gc
for i in range(2000):
    temp.updateOld()
    tempeq.solve(var=temp,dt=dt,solver=solver)
    print 'hola',i
    if i%1==0:
        viewer.plot()

##    gc.collect()

#     if i%50==0:
#         filename="alloy2test_phase_%#05d"% (i)
#         imsave_phase.plot(filename+'.dat')
#         filename="alloy2test_con_%#05d"% (i)
#         imsave_con.plot(filename+'.dat')
# print 'file written', datetime.datetime.now()
