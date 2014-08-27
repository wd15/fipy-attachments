from fipy import *

dr= 5e-04
DR =[dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr, dr]
r_int = 0.00125
R_est = len(DR)*dr + r_int

#mesh = CylindricalGrid1D(dx=DR) + (r_int,) 

    # SHOULD BE EQUAL TO:

mesh = CylindricalGrid1D(dr=dr, nr=(len(DR))) + (r_int,) 



x = mesh.getCellCenters()[0]

sigma = (1./3.) #Electrical conductivity
W = 20. #POWER
sp = 0.02 # depth (z direction in cylindrical coord.)
Z = (((1/sigma)*log((R_est/r_int)))/(2*pi*sp)) #electrical impedance
I = sqrt((W/Z))  # electric current
J = I/(2*pi*sp*x)  #Current density

q = CellVariable(name = "Resistive Heat", mesh = mesh, value = 0.)  

q = (1/(sigma)) * (J**2)  #heat source by joule heating

teta = CellVariable(name = "Temperature", mesh = mesh, value = 20.)
totaltime = CellVariable(name = "Time", mesh = mesh, value = 0.)

# BCs

valueLeft = 0. 
valueRight = (20.)
facesLeft = mesh.getFacesLeft()
facesRight = mesh.getFacesRight()
BCs = (FixedValue(faces=facesRight, value=valueRight), FixedFlux(faces=facesLeft, value=valueLeft))


# viewer 
if __name__ == '__main__':
    viewer = Viewer(vars=teta, datamin=0., datamax=100.)
    viewer.plot()

# def time steps and equation
timeStepDuration = 1
steps =40
time = 0.
for step in range(steps):
    time += timeStepDuration
    totaltime.setValue(time)
            
    OmegaH = 3500000.
    
    GammaH = 0.5 

   

    eqH = (TransientTerm(coeff = OmegaH)) == (DiffusionTerm(coeff = GammaH)) + (q)
      
    #eqH = (DiffusionTerm(coeff = GammaH))+ q == 0
    
        
    eqH.solve(var=teta, boundaryConditions=BCs, dt=timeStepDuration)
   
    viewer.plot()
   
