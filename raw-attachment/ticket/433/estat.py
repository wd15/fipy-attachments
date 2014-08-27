#!/usr/bin/env python

from fipy import *
import numpy
import sys

mesh = GmshImporter3D('twin_ap_3D.msh')
x,y,z = mesh.getVertexCoords()
X,Y,Z = mesh.getFaceCenters()
z0,r = 10.,26.5
x0,y0 = 22,22
x1,y1 = -22,-22

potential = CellVariable(mesh=mesh, name='potential', value=0.)
x = numpy.arange(-60,60,.1)
X,Y = numpy.meshgrid(x,x)
z= potential.getValue()
print potential(2.2,1.1)
sys.exit(0)
permittivity = 1.
   
potential.equation = (DiffusionTerm(coeff = permittivity) == 0.)

allfaces = mesh.getExteriorFaces()
ring0 = allfaces & ( ((abs((X-x0)**2+(Y-y0)**2-r**2) < 2 ) | ((abs(X-x0)<1.5) & (Y<y0-r-1.5))) & (abs(Z-z0)<3.) )
ring1 = allfaces & ( ((abs((X-x1)**2+(Y-y1)**2-r**2) < 2 ) | ((abs(X-x1)<1.5) & (Y<y1-r-1.5))) & (abs(Z-z0)<3.) ) 
bottom_faces = allfaces & ( (((X-x0)**2+(Y-y0)**2 > (r+2.5)**2) ) & (Z<.2) )
top_faces = allfaces & ( (((X-x0)**2+(Y-y0)**2 > (r+2.5)**2) ) & (Z>9.8) )

bcs = (
	FixedValue(value=5.,faces=ring0),
	FixedValue(value=0.,faces=ring1),
	FixedValue(value=0.,faces=bottom_faces),
)

potential.equation.solve(var=potential, boundaryConditions=bcs)

viewer = viewers.vtkViewer.VTKViewer(vars=potential)
viewer.plot("/tmp/test.vtk")
raw_input("Press 'Enter' to exit.")

