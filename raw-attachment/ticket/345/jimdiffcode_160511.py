import fipy as fp


r_fuel = .534035
t_gap = 0.01143
t_clad = 0.09398

q = 37.94
q3 = q/(np.pi*r_fuel**2)

k_fuel = 0.0550
k_gap = 0.004
k_clad = 0.1070

r_total = r_fuel + t_gap + t_clad

n_fuel = 20 #num. nodes in fuel
n_gap = 10 # num. nodes in gap
n_clad = 15 # num. nodes in clad

dr_fuel = r_fuel/(n_fuel)
dr_gap = t_gap/(n_gap)
dr_clad = t_clad/(n_clad)


## mesh_fuel = fp.Grid1D(nx = n_fuel, dx = dr_fuel)
## mesh_gap = fp.Grid1D(nx = n_gap, dx = dr_gap) + ((r_fuel,),)
## mesh_clad = fp.Grid1D(nx = n_clad, dx = dr_clad) + (((r_fuel+t_gap),),)

mesh_fuel = fp.CylindricalGrid1D(nx = n_fuel, dx = dr_fuel)
mesh_gap = fp.CylindricalGrid1D(nx = n_gap, dx = dr_gap) + ((r_fuel,),)
mesh_clad = fp.CylindricalGrid1D(nx = n_clad, dx = dr_clad) + (((r_fuel+t_gap),),)

print 'Fuel Mesh:',mesh_fuel.getCellCenters().value
print 'Gap Mesh:',mesh_gap.getCellCenters().value
print 'Clad Mesh:',mesh_clad.getCellCenters().value
##comments.gmane.org/gmane.comp.python.fipy/1554

mesh_tot = mesh_fuel + mesh_gap + mesh_clad

#setting up diffusion coefficients
D = fp.FaceVariable(mesh = mesh_tot, value=0.)
x = mesh_tot.getFaceCenters()[0]
D.setValue(k_fuel, where=(r_fuel >= x))
D.setValue(k_gap, where=(r_fuel < x) & ((r_fuel+t_gap) >= x))
D.setValue(k_clad, where=((r_fuel+t_gap) < x))
#source term
y = mesh_tot.getCellCenters()[0]
S = fp.CellVariable(mesh = mesh_tot, value = 0.)
S.setValue(q3, where=(r_fuel >= y))
#boundary conditions
flux_left = 0
temp_right = 513

BC = (fp.FixedFlux(faces=mesh_tot.getFacesLeft(), value = flux_left),
      fp.FixedValue(faces=mesh_tot.getFacesRight(), value = temp_right))
## temp_left = 900
## temp_right = 500

## BC = (fp.FixedValue(faces=mesh_tot.getFacesLeft(), value = temp_left),
##       fp.FixedValue(faces=mesh_tot.getFacesRight(), value = temp_right))


phi = fp.CellVariable(name='Temperature',mesh=mesh_tot,value=0.)

eq = fp.DiffusionTerm(coeff=D) == -S
eq.solve(var = phi, boundaryConditions = BC)

fp.Viewer(vars=phi)
