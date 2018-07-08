#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 21:00:27 2018

@author: parkershankin-clarke
"""

''' This code is where the real numbers will be used'''

import numpy as np 
import itertools
from itertools import product
import scipy.integrate 
#import odeint
import matplotlib.pyplot as plt

#Final amount of Nitrogen at a given location 
Final_Nitrogen = (11.804 *.14)/256



# The area of Passedena in m^2
Area_Passadena = 5.988052e+7

''' Nitrogen Deposition (mg/m^2/year) '''
N_dep_L = 87.1351
N_dep_H = 785.3832

# Nitrogen due to Rainfall

# Concentration of nutrients in rain in Pasadena (NH4+ + NO3-) (mg/l)
N_rain_rate_NH4_L = 0.292
N_rain_rate_NO3_L = 1.41

N_rain_rate_NH4_H = .379
N_rain_rate_NO3_H = 1.94


N_rain_rate_L = N_rain_rate_NH4_L + N_rain_rate_NO3_L 
N_rain_rate_H = N_rain_rate_NH4_H + N_rain_rate_NO3_H
#
## Amount of rainfall (liters/m^2/year)
rainfall_rate_H = 1.429e+10 / Area_Passadena 
rainfall_rate_L = 7.144e+7 / Area_Passadena 

'''Rate rainfall (mg/m^2/year)'''
n_rate_final_L = rainfall_rate_L * N_rain_rate_L 
n_rate_final_H = rainfall_rate_H  * N_rain_rate_H 

'''Rate nitrogen fixation (mg/m^2/year)'''
n_fixation_L = 20
n_fixation_H = 4000

''' N out from burning (mg/m^2/yr)'''

n_volitization_L = 850
n_volitization_H = 1000 ##This is filler data





diff_N_dep = N_dep_H - N_dep_L + 1
array_N_dep = list(np.linspace(N_dep_L,N_dep_H,num = round(10)))

diff_N_rain = n_rate_final_H - n_rate_final_L + 1
array_N_rain = np.linspace(n_rate_final_L,n_rate_final_H,num = round(10))

diff_n_fixation = n_fixation_H - n_fixation_L + 1
array_n_fixation = list(np.linspace(n_fixation_L, n_fixation_H,num = round(10)))





combos = product(array_N_dep,array_N_rain)

   
#def iterate_parameters(array_N_dep,array_N_rain):
#    """ """
#    complete = []
#    future_input = []
#    
#    for combo in combos: 
#        complete = [combo] + complete
#    
#    for i in range (len(complete)):
#        sum_list = sum(complete[i])
#        indiv_list = complete[i]
#        if sum_list == 15:
#            print('N deposition is contributing {} and N due to rain fall is contributing {}'.format(indiv_list[0],indiv_list[1]))
#            future_input = future_input + [indiv_list[0],indiv_list[1]]
#    return future_input
#
##fucntion that returns dydt
#def model(N_rain_rate,N_dep_rate,N,t):
#    dndt = N_rain_rate + N_dep_rate 
#    return dndt
#
##intial conditions 
#n0 = 5
#
##times points 
#t = np.linspace(0,20)
#
#
##plot results 
#plt.ploy(t,y)
#plt.xlabel('time')
#plot.ylabel('Nitrogen')
#plt.show()
#    
#
##MAIN
#            
#call = iterate_parameters(array_N_dep,array_N_rain)
#
##solve the ode 
#n_rain_rate1 = call[1]
#n_dep_rate1 = call[2]
#
#n1 = odeint(model,n0,t,args=(n_rain_rate1,n_dep_rate1))
#
#n_rain_rate2 = call[2]
#n_dep_rate2 = call[3]
#
#n2 = odeint(model,n0,t,args=(n_rain_rate2,n_dep_rate2))
