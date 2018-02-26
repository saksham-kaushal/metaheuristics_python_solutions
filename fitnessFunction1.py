import math as mt

#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 20   # Problem Dimension
LB      = -35   # Set Size Lower Bound
UB      = 35   # Set Size Upper Bound
Name	= "ackley"	#Name of the function

#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

"""
Ackley's Function
f(x)=-20exp(-0.02 * sqrt((1/D)sum_1_to_D(x(i)^2))) - exp((1/D)sum_1_to_D(cos(2x(i)*pi))) + 20 + exp(1)
subject to -35<=x(i)<=35. The global minimum is located at origin x*=(0,....,0) with f(x*)=0

"""

def FitnessFunction (x):
    s1=s2=0
    for i in range(0, D):
	s1 += x[i]*x[i]
	s2 += mt.cos(2*mt.pi*x[i])
    return round((-20*mt.exp(-0.02*(mt.sqrt(float(s1)/D)))-mt.exp(float(s2)/D)+20+mt.exp(1)),3)
