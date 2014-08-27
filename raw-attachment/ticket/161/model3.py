from fipy import *
from time import time

startTime=time()

nx=41
ny=3
nz=14

dx=[0.0675*1.3**abs(i-17) for i in range(nx)]
dy=[0.0675*1.3**abs(i-(ny-1)/2.) for i in range(ny)]
dz=[0.5 for i in range(nz)]

mesh=Grid3D(dx=dx,dy=dy,dz=dz,nx=nx,ny=ny,nz=nz)

X,Y,Z=mesh.getFaceCenters()

BCs = (FixedValue(mesh.getExteriorFaces()&(X==0)&(Z<5.6),5.6),
       FixedValue(mesh.getExteriorFaces()&(X==max(X))&(Z<2.9),2.9))

top=CellVariable(name='top of cell',mesh=mesh,
                 value=Z[mesh._getCellFaceIDs().data[5]])

bot=CellVariable(name='bottom of cell',mesh=mesh,
                 value=Z[mesh._getCellFaceIDs().data[4]])

X,Y,Z=mesh.getCellCenters()
head=CellVariable(name='head',mesh=mesh,value=8.,hasOld=1)

'''
These terms control teh desaturation of a cell, slowly decreasing
the permeability in the x and y directions as the cell dewaters.
permeability in the z direction is increased as the cell dewaters
to allow sorce/sink terms in the top layer to continue to influence
the saturated zone.
'''

###need to add this to satState variable 
#minDesat=-3. ## need to specify minimum satState or will get overflow

residThick=1.e-2
f=6.0
g=1./residThick-f
satState=(head<top)*(head-bot)/(top-bot)+(head>top)
cellSatH=((satState>=0)*(satState+residThick*exp(-g*satState))+
          (satState<0)* residThick*exp(f*satState))
cellSatV=(satState>=.01)/(satState)+ (satState<.01)*100

spStore=1.e-3
spYield=.2
desat=1.e-8

storage=desat+(head>=top)*spStore+((head>bot)&(head<top))*spYield

kond=CellVariable(name='hyd.cond.',mesh=mesh,rank=1,value=1.e-5)

print 'a',time()-startTime

###second method
#cellSat=kond*[cellSatH,cellSatH,cellSatV]

print 'b',time()-startTime

###recharge across top of model
rech=CellVariable(name='recharge',mesh=mesh,
                  value=where(Z==Z.max(),1.e-8,0))

print 'c',time()-startTime

###second method
#GwEqInj=TransientTerm(coeff=storage)==DiffusionTerm(coeff=cellSat)+rech
GwEqInj=TransientTerm(coeff=storage)==DiffusionTerm(coeff=kond*cellSatH+cellSatV*kond*[0,0,1])+rech
print 'd',time()-startTime


solver = LinearLUSolver(tolerance=1.0e-10, iterations=1000)

delT=1.e7
for i in range(2):
    resid=1.
    print '****************'
    while resid>1.e-3:
        head.updateOld()
        
        print satState()[where((X<25.1)&(X>25)&(Y>.12)&(Y<.13))]
        print cellSatH()[where((X<25.1)&(X>25)&(Y>.12)&(Y<.13))]
        resid=GwEqInj.sweep(var=head,
                            solver=solver,
                            dt=delT,
                            underRelaxation=None,
                            boundaryConditions=BCs 
                            )
        print resid

