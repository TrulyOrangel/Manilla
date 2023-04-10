import matplotlib.pyplot as plt
import numpy as np
import random as r
import math as m

""" matplotlib basics
x1 = [some list]
y1 = [some list]
x2 = [some list]
y2 = [some list]

plt.plot(x1, y1, label="line 1")
plt.plot(x2, y2, label="line 2")
plt.legend()
plt.show()
"""

## CONSTANTS AND EXAMPLE LISTS ##

RESOLUTION = 200

TIME = [i for i in range(1,RESOLUTION +1)] # length 200

N_SINE = [(m.sin(0.03*i)+r.random())*5 for i in range(RESOLUTION)]
N_LINE = [(0.3*i)+r.random() for i in range(RESOLUTION)]










## FORECASTING FUNCTIONS ##
#* all functions return a list of new values.
def simpleMovingAverage(data, width):
    ma = []

    i = 0
    while i < len(data) - (width+1):
        window = data[i:i+width]
        ma.append(round(sum(window)/width, 2))

        i += 1

    # ma is smaller than data by width+1
    for i in range(width+1):
        ma.append(ma[-1])
    return ma

plt.plot(TIME, N_SINE, label="n_sine")
plt.plot(TIME, simpleMovingAverage(N_SINE, 3), label="MA 3")
plt.plot(TIME, simpleMovingAverage(N_SINE, 6), label="MA 6")
plt.legend()
plt.show()













