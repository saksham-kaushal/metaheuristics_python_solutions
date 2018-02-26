import math as mt

#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 2   # Problem Dimension
LB      = -5   # Set Size Lower Bound
UB      = 5   # Set Size Upper Bound
Name	= "egg_crate"	#name of function

#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------
"""
Egg Crate Function :	For dimension = 2
f(x) = x(1)^2+x(2)^2+25(sin^2(x(1))+sin^2(x(1)))
subject to -5<=x(i)<=5. The global minimum is located at x* = (0,0) with f(x*)=0

"""

def FitnessFunction (x):
    return round(x[0]*x[0]+x[1]*x[1]+25*(mt.sin(x[0])*mt.sin(x[0])+mt.sin(x[1])*mt.sin(x[1])),7)
