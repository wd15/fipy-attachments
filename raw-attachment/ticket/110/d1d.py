from fipy import *

delta_a=1e-6
Lx = 10*delta_a
nx = 40
dx = Lx / nx

mesh = Grid1D(dx=dx, nx=nx)

con  = CellVariable(mesh = mesh)
impurity = CellVariable(mesh = mesh)

x, =  mesh.getCellCenters()

impurity_yes=(x<5*dx) #last 5 pixels

impurity.setValue(1,where=impurity_yes)

facewhere= (impurity.getFaceGrad().getMag()==0)

mobility=CellVariable(mesh=mesh)
mobility_face=mobility.getHarmonicFaceValue()

diffCoeff = mobility_face*facewhere

con.setValue(0)

coneq= TransientTerm() - ImplicitDiffusionTerm(coeff=mobility_face * facewhere) - (mobility_face * facewhere * [[1]]).getDivergence()
##coneq= TransientTerm() - ImplicitDiffusionTerm(coeff=diffCoeff) - (diffCoeff * [1,]).getDivergence()

coneq.solve(con)


print con