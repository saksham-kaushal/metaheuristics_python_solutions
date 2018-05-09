#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
import math as mt

D       = 2   # Problem Dimension
LB      = -30   # Set Size Lower Bound
UB      = 30   # Set Size Upper Bound
Name	= "chichinadze"


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------
def FitnessFunction (x):
		return (x[0]*x[0])-(12.0*x[0])+11.0+(10.0*mt.cos((mt.pi*x[0])/2.0))+(8.0*mt.sin((5.0*mt.pi*x[0])/2.0))-((1.0/5.0)**0.5)*mt.exp(-0.5*((x[1]-0.5)**2))













