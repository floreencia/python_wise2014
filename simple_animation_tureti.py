#!/usr/bin/python

import matplotlib
matplotlib.use('GTK')
import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()

xdata = np.arange(0,6*np.pi,0.01)

func = lambda x ,p: np.sin(x)*np.cos(p)

#line, = plt.plot(xdata,func(xdata,0))
fig, ax = plt.subplots()
line, = ax.plot( xdata, func(xdata,0))

for value in np.arange( 0, 7, 0.05):
    line.set_ydata( func( xdata, value))
    plt.draw()
    time.sleep(0.02)
