from fipy.tools import numerix
   
from fipy.meshes.grid2D import Grid2D
from fipy.models.levelSet.distanceFunction.distanceVariable import DistanceVariable
from fipy.models.levelSet.advection.higherOrderAdvectionEquation import buildHigherOrderAdvectionEquation
from fipy.models.levelSet.surfactant.surfactantEquation import SurfactantEquation
from fipy.models.levelSet.surfactant.surfactantVariable import SurfactantVariable
from fipy.variables.cellVariable import CellVariable

L = 1.
nx = 256
cfl = 0.1
initialRadius = L / 4.
k = 1
dx = L / nx
steps = 10 * nx / 8

mesh = Grid2D(dx = dx, dy = dx, nx = nx, ny = nx)

error = CellVariable(mesh=mesh)


distanceVariable = DistanceVariable(
    name = 'level set variable',
    mesh = mesh,
    value = numerix.sqrt((mesh.getCellCenters()[:,0] - L / 2.)**2 + (mesh.getCellCenters()[:,1] - L / 2.)**2) - initialRadius,
    hasOld = 1)

initialSurfactantValue =  1.

surfactantVariable = SurfactantVariable(
    value = initialSurfactantValue,
    distanceVar = distanceVariable
    )

velocity = 1.

surfactantEquation = SurfactantEquation(
    distanceVar = distanceVariable)



if __name__ == '__main__':
    
    import fipy.viewers
    distanceViewer = fipy.viewers.make(vars = distanceVariable, limits = {'datamin': -initialRadius, 'datamax': initialRadius})
    surfactantViewer = fipy.viewers.make(vars = surfactantVariable, limits = {'datamin': 0., 'datamax': 100.})
    errorViewer = fipy.viewers.make(vars = error)
    distanceViewer.plot()
    surfactantViewer.plot()
    errorViewer.plot()

    totalTime = 0

    L1 = list(numerix.zeros(10, 'd'))
    L2 = list(numerix.zeros(10, 'd'))
    Linf = list(numerix.zeros(10, 'd'))
##    errorList = (list(numerix.zeros(10, 'd'))

    for step in range(steps):
##        print 'step',step
        timeStepDuration = cfl * dx / velocity
        distanceVariable.updateOld()
        distanceVariable.setValue(numerix.array(distanceVariable) - velocity * timeStepDuration)
        surfactantEquation.solve(surfactantVariable)
        
        totalTime += timeStepDuration
        
        distanceViewer.plot()
        surfactantViewer.plot()
        errorViewer.plot()

        finalRadius = initialRadius + totalTime * velocity + distanceVariable
        answer = initialSurfactantValue * initialRadius / finalRadius
        coverage = surfactantVariable.getInterfaceVar()

        error.setValue(numerix.where((coverage > 1e-3) & (distanceVariable > 0), abs(coverage - answer), 0))

        adjDistanceVariables = numerix.take(distanceVariable,  mesh._getCellToCellIDs())
        adjCoverages = numerix.take(coverage,  mesh._getCellToCellIDs())
        flag = (adjDistanceVariables < 0) & (adjCoverages > 1e-6)




        error.setValue(0, where=numerix.sum(flag, index=1) > 0)

        
        del L1[0]
        del L2[0]
        del Linf[0]

        L1.append(numerix.array(numerix.sum(error)/nx))
        L2.append(numerix.array(numerix.sqrt(numerix.sum(error**2)/nx)))
        Linf.append(numerix.array(max(error)))

##        argmax = numerix.argmax(error)

##        del errorList[0]

##        errorList.append(max(error))

##        argmax = numerix.argmax(error)
        

##        print

##        print 'error[argmax]',error[argmax]
##        print 'coverage[argmax]',coverage[argmax]
##        print 'answer[argmax]',answer[argmax]
##        print 'distanceVariable[argmax]',distanceVariable[argmax]
##        print 'dx',dx
##        print 'distanceVariable.getGrad()[argmax]',distanceVariable.getGrad()[argmax]

##        flag = 0
##        for ID in mesh._getCellToCellIDs()[argmax]:
##            print 'distanceVariable[ID]',distanceVariable[ID],'coverage[ID]',coverage[ID]
##            print 'adjDistanceVariables[argmax]',adjDistanceVariables[argmax]
##            if coverage[ID] > 1e-5 and distanceVariable[ID] < 0:
##                flag = 1

##        print 'L1',L1
##        print 'L2',L2
##        print 'Linf',Linf

        print 'step',step,'nx',nx,'max(L1)',max(L1),'max(L2)',max(L2),'max(Linf)',max(Linf) 
        
##        N = numerix.sum(coverage > 1e-3)
        
##        error = 0.
##        size = 0
##        for i in range(len(coverage)):
##            if coverage[i] > 1e-3:
##                error += (coverage[i] - answer)**2
##                size += 1

##        error

##        print 'answer',answer
##        print 'coverage',coverage

##        l1 = numerix.sum(error) / N
##        l2 = numerix.sqrt(numerix.sum(error**2) / N)
##        linf = numerix.max(error)

##        del L1[0]
##        del L2[0]
##        del Linf[0]

##        L1.append(numerix.array(numerix.sum(error) / N))
##        L2.append(numerix.array(numerix.sqrt(numerix.sum(error**2) / N)))
##        Linf.append(numerix.array((numerix.max(error))))

##        print 'L1 norm',L1
      
      
##        print 'L1 norm',max(L1)
##        print 'L2 norm',max(L2)
##        print 'Linf norm',max(Linf)

##        argmax = numerix.argmax(error)



##        print 'coverage',coverage[argmax]
##        print 'answer',answer
##        phi = distanceVariable[argmax]
##        realAnswer = initialSurfactantValue * initialRadius / (initialRadius + totalTime * velocity + phi)
##        print 'real answer',realAnswer
##        print 'error 1',abs(coverage[argmax] - realAnswer)
##        print 'error 2',abs(coverage[argmax] - answer)
        


        

    raw_input('finished')
