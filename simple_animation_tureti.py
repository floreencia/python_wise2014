#!/usr/bin/python

import matplotlib
matplotlib.use('GTK')
import numpy as np
import pylab as pl
import time


pl.ion()

xdata = np.arange(0,6*np.pi,0.01)

func = lambda x,p: np.sin(p)*np.sin(x)

line, = pl.plot(xdata,func(xdata,0))
pl.ylim(-1.5,1.5)

for value in np.arange(0,7,0.1):
    line.set_ydata(func(xdata,value))
    pl.draw()
    time.sleep(0.05)
