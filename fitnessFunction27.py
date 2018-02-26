import math as mt

#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2   # Problem Dimension
LB      = -100   # Set Size Lower Bound
UB      = 100   # Set Size Upper Bound
Name	= "easom" 	#Name of function

#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------
"""
Easom Function :	For dimension = 2
f(x) = -cos(x1)cos(x2) * exp[-(x1-pi)^2 -(x2-pi)^2]
subject to -100<=x(i)<=100. The global minimum is located at x* = (pi,pi) with f(x*)=-1

"""

def FitnessFunction (x):
    return round(-mt.cos(x[0])*mt.cos(x[1])*mt.exp(-((x[0]-mt.pi)*(x[0]-mt.pi))-((x[1]-mt.pi)*(x[1]-mt.pi))),7)
