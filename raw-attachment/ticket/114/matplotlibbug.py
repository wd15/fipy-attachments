import pylab, numpy

pylab.ion()

data0 = numpy.zeros((2,2), 'd')
data1 = numpy.zeros((2,2), 'd')

## make figure 0

fig0 = pylab.figure()
pylab.title('data0')
image0 = pylab.imshow(data0)
pylab.colorbar()
pylab.draw()
raw_input('fig 0')

## make figure 1

fig1 = pylab.figure()
pylab.title('data1')
image1 = pylab.imshow(data1)
pylab.colorbar()
pylab.draw()
raw_input('fig 1')

## redraw figure 0 with new data

newdata = numpy.array(((0.,1.),(2.,3.)))
pylab.figure(fig0.number)
image0.set_data(newdata)
##pylab.clim(vmax=3, vmin=0)
pylab.draw()
raw_input('fig 0')

## redraw figure 1 with new data

pylab.figure(fig1.number)
image1.set_data(newdata)
pylab.clim(vmax=3, vmin=0)
pylab.draw()
raw_input('fig 1')
