from time import time
t1 = time()

import matplotlib.pyplot as plt
from numpy import zeros,arange
from math import pi


from mcCircle import *

width = 400
height = 400
a = 200
b = 200
r = 200

iterStart = 100
iterStep = 100
iterEnd = 10000

iterMarker = 10000

mapArea = width*height
circleArea = pi*(r**2)
circlePercent = (circleArea/mapArea)*100

if iterEnd > (pi*(r**2)):
    print("Sampling iteration is more than the circle area! Should be lower than %.0f." % pi*(r^2))

i = 0
totalPercent = []

for mcIter in range(iterStart,iterEnd+iterStep,iterStep):
    map01 = zeros((width,height))
    pixIn, pixPercent = createCircle(width,height,a,b,r,mcIter,map01)
    totalPercent.append(pixPercent)
    i = i+1
    if mcIter % iterMarker == 0:
        print("Iteration to %d" % mcIter)

xAxis = arange(iterStart,iterEnd+iterStep,iterStep)
fig,axs = plt.subplots()
axs.plot(xAxis,totalPercent,linewidth=0.75,label='Analytic Calc.')
axs.hlines(circlePercent,iterStart,iterEnd,color='r',linewidth=0.75,label='Monte Carlo Calc.')
axs.set_xlabel('Sampling Frequency')
axs.set_ylabel('Circle Percentage')
axs.legend(loc='upper right')

plt.show()

t2 = time()
ts = (t2 - t1)/60
print('Execution time: ', ts,' minutes.')