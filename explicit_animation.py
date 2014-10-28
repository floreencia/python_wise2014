#!/usr/bin/python

import matplotlib.animation as animation
import numpy as np
import pylab as pl

#pl.ion()

fig = pl.figure()
pl.ylim(-1.5,1.5)
xdata = np.arange(0,6*np.pi,0.01)
func = lambda x,p: np.sin(p)*np.sin(x)
line, = pl.plot(xdata, func(xdata,0))

def update(i):
    line.set_ydata(func(xdata,0.1*i))
    return line
#keep reference to Line2D-object.
#this will be executed for each frame.

swinging_sine = animation.FuncAnimation(fig, update, frames=1000, interval=50)
pl.show()

raw_input('done?')
