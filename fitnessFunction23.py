import math as mt

#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 20   # Problem Dimension
LB      = -1   # Set Size Lower Bound
UB      = 1   # Set Size Upper Bound
Name	= "deb"

#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------
def FitnessFunction (x):
		sum = 0.0
		for i in range(D):
			sum+= (mt.sin(5*mt.pi*x[i]))**6
		return (-1.0/D)*sum














