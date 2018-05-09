#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
import math as mt

D       = 2   # Problem Dimension
LB      = -10   # Set Size Lower Bound
UB      = 10   # Set Size Upper Bound
Name	= "trefethen"

#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------
def FitnessFunction (x):
		return (mt.exp(mt.sin(50*x[0])))+(mt.sin(60*mt.exp(x[1])))+(mt.sin(70*mt.sin(x[0])))+(mt.sin(80*x[1]))-(mt.sin(10*(x[0]+x[1])))+((1.0/4.0)*((x[0]*x[0])+(x[1]*x[1])))













