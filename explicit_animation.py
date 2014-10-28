#!/usr/bin/python

import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
xdata = np.arange( 0, 6*np.pi, 0.01)
func = lambda x, p: np.sin(x)*np.cos(p)
line1, = plt.plot( xdata, func( xdata, 0))
line2, = plt.plot( xdata, func( 0, xdata))

def update(i):
    line1.set_ydata( func( xdata, i*0.02 ))
    line2.set_ydata( func( i*0.05, xdata ))

swinging_sine = animation.FuncAnimation( fig, update, np.arange(1,200), interval=50)

#swinging_sine.save('explicit_animation.mp4')

plt.show()

