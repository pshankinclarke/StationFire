#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 17:29:38 2018

@author: parkershankin-clarke
"""


''' This is a fully working model that simulates nitrogen inputs and outputs as a function
of time with fake numbers. '''

import itertools
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
#from sympy.solvers import solve
#from sympy import Symbol




# Avg. Nitrogen measured {(Winter + Summer)/2} in the field
N_Final = 15

# Indivdual Nitrogen measurements NH4+ and NO3- (These are unknowns)

# Seasonal Variation Nitrogen Measurements 

N_final_winter = 20
N_final_summer = 15

#Examples input parameters
N_input_L = 2 
N_input_H = 10 

#Example output parameters
N_output_L = 17.5
N_output_H = 20


# An equally spaced element-list of a given input/out parameter
diff_N_input = N_output_H - N_output_L + 1
array_N_input = np.linspace(N_output_L,N_output_H,num = diff_N_input)

diff_N_output = N_input_H - N_input_L + 1
array_N_output = np.linspace(N_input_L,N_input_H,num = diff_N_output)
array_N_output = np.negative(array_N_output)



combos = itertools.product(array_N_input,array_N_output)


def iterate_parameters(array_N_input,array_N_output):
    '''This functions takes in different iterations of inputs and outputs and returns a list list of future inputts 
    to use as parameters in the ODE'''
    complete = []
    future_input = []
    
    for combo in combos: 
        complete = [combo] + complete
    
    for i in range (len(complete)):
        sum_list = sum(complete[i])
        indiv_list = complete[i]
        if abs(sum_list - target_rate) < .001:
            print('N deposition is contributing {} and N due to rain fall is contributing {}'.format(indiv_list[0],indiv_list[1]))
            future_input = future_input + [indiv_list[0],indiv_list[1]]
    return future_input





def model(y,t,k):
    '''function that returns dy/dt'''
    dydt = k
    return dydt



#MAIN

call = iterate_parameters(array_N_input,array_N_output)


# initial condition for N_final
y0 = 0

# intial conditions for N_winter and N_summer

# intial conditions for N_NH4+ and N_NO3-

# time points
t = np.linspace(0,2)

# solve ODEs

k = call[0] + call[1]
y1 = odeint(model,y0,t,args=(k,))
#k = call[2] + call[3]
#y2 = odeint(model,y0,t,args=(k,))
#k = call[4] + call[5]
#y3 = odeint(model,y0,t,args=(k,))

#d={}
#for x in range(3):
#        k = call[x] + call[x+1]
#        d["y{0}".format(x)]=odeint(model,y0,t,args=(k,))



# plot results       
plt.plot(t,y1,'r-',linewidth=2,label='k=0.1')
#plt.plot(t,y2,'b--',linewidth=2,label='k=0.2')
#plt.plot(t,y3,'g:',linewidth=2,label='k=0.5')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()



target_rate =  (N_Final - y0) / (t[49] - t[0]) 

