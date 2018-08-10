#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 21:00:27 2018

@author: parkershankin-clarke
"""

''' This code is where the real numbers will be used'''

import itertools
import random
from itertools import product
import scipy.integrate 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot
import operator 


"""Data"""
"""The formation of the data is as follows : ##Sections : , #subsections [description] (units) --relevant time period when data was obtained-- """


##Unburnt locations : 

#Intial amount of Nitrogen at a given unburnt location (wt %) --Summer--

ub2_s09 = 0.03
ub17_s09 = 0.06
ub23_s09 = 0.19
ub30_s09 = 0.47


#Final amount of Nitrogen at a given unburnt location (wt %) --Summer--

ub2_s17 = 0.1772493 
ub17_s17 = 0.016721675 
ub23_s17 = 0.11240128
ub30_s17 = 0.86988475


##Burnt locations:

#Intial amount of Nitrogen at a given burnt location (wt %) --Summer--
b1_s09 = 0.19 
b3_s09 = 0.13
b5_s09 = 0.23
b7_s09 = 0.25
b8_s09 = 0.15
b9_s09 = 0.06
b11_s09 = 0.16
b14_s09 = 0.23
b15_s09 = 0.15
b16_s09 = 0.20
b18_s09 = 0.26
b20_s09 = 0.27
b21_s09 = 0.59
b22_s09 = 0.18
b25_s09 = 0.23
b26_s09 = 0.12
b28_s09 = 0.26
b29_s09 = 0.10

#Final amount of Nitrogen at a given burnt location (wt %) --Winter--

b3_w17 =	0.1207012
b7_w17 = 0.25390755
b8_w17 =	0.031408405
b11_w17 = 0.13450135
b14__w17 = 0.14602965
b15__w17 =0.113312845
b16__w17 =0.11892277
b18__w17 =0.1653279
b21__w17 =0.4682268
b22__w17 =0.68432165
b29_w17 =	0.03949062




#Final amount of Nitrogen at a given burnt location (wt %) --Summer--
b1_s17 = 0.1444084
b3_s17 = 0.16114415
b5_s17 = 0.09600845
b7_s17 = 0.038680695
b8_s17 = 0.0621249
b9_s17 = 0.09576093
b11_s17 = 0.098756345
b14_s17 = 0.16202085
b15_s17 = 0.108324275
b16_s17 = 0.085744605
b18_s17 = 0.03214277
b20_s17 = 0.362902
b21_s17 = 0.6096518
b22_s17 = 0.12671475
b25_s17 = 0.1422021
b26_s17 = 0.1154969
b28_s17 = 0.032442245
b29_s17 = 0.008741861


##Ancillary data :

#Ash concentrations at sites (wt%) --Summer--

ba_b1_s09 = 0.35
a_b3_s09 = 0.15
a_b5_s09 = 0.33
a_b7_s09 = 0.11
a_b8_s09 = 0.14
wa_b8_s09 = 0.02
a_b9_s09 = 0.06
a_b11_s09 = 0.15
a_b14_s09 = 0.17
a_b15_s09 = 0.15
a_b16_s09 = .08
wa_b16_s09 = .03
a_b18_s09 = 0.12
a_b20_s09 = 0.17
a_b21_s09 = 0.24
wa_b21_s09 = .05
a_b22_s09 = 0.06
a_b25_s09 = 0.19
a_b26_s09 = 0.08
ba_b26_s09 = .27
a_b28_s09 = 0.20
b29_s09 = 0.02

#The area of Passedena in m^2
Area_Passadena = 5.988052e+7

#density of soil (mg/m^2)
density_soil = 1.33e+7
depth_sampled = .05
area_sampled = 1

"""Manipulated Data"""
"""##Section:,#Subsection, Description --relevant time period when data was obtained-- """

##Data converted to numpy arrays:

#Intial unburned sites --Summer--
IUBS = np.array([ub2_s17, ub17_s17, ub23_s17 ,ub30_s17])

#Final unburned sites --Summer--
FUBS = np.array([ub2_s09, ub17_s09, ub23_s09 ,ub30_s09])

#IUBS/FUBS labels
IFUBS_labels = np.array([2,17,23,30])

#Intial burned sites --Summer--
IBS = np.array([b1_s09,b3_s09,b5_s09,b7_s09,b8_s09,b9_s09,b11_s09,b14_s09,b15_s09,b16_s09,b18_s09,b20_s09,b21_s09,b22_s09,b25_s09,b26_s09,b28_s09,b29_s09])

#Final burned sites --Winter--
FBSW = np.array([b3_w17, b7_w17 , b8_w17, b11_w17, b14__w17 , b15__w17 , b16__w17,b18__w17,b21__w17 ,b22__w17 ,b29_w17])
#Final burned sites filled with zeros --Winter--
FBSW_filled = np.array([0,b3_w17,0, b7_w17, b8_w17,0, b11_w17, b14__w17 , b15__w17 , b16__w17,b18__w17,0,b21__w17 ,b22__w17,0,0,0,b29_w17])

#Final burned sites --Summer--
FBS = np.array([b1_s17,b3_s17,b5_s17,b7_s17,b8_s17,b9_s17,b11_s17,b14_s17,b15_s17,b16_s17,b18_s17,b20_s17,b21_s17,b22_s17,b25_s17,b26_s17,b28_s17,b29_s17])

#IBS/FBS labels
IFBS_labels = np.array([1,3,5,7,8,9,11,14,15,16,18,20,21,22,25,26,28,29])

#FBSW labels
FBSW_labels = np.array([3,7,8,11,14,15,16,18,21,22,29])

#Intial ash concentration --Summer--
IACG = np.array([a_b3_s09,a_b5_s09,a_b7_s09,a_b8_s09,a_b9_s09,a_b11_s09,a_b14_s09,a_b15_s09,a_b16_s09,a_b18_s09,a_b20_s09,a_b21_s09,a_b22_s09,a_b25_s09,a_b26_s09])
IACW = np.array([wa_b8_s09,wa_b16_s09,wa_b21_s09])
IACB = np.array([ba_b1_s09,ba_b26_s09,b29_s09])
# Ash lists filled with zeros where locations were not sampled
IACG_filled = np.array([0,a_b3_s09,a_b5_s09,a_b7_s09,a_b8_s09,a_b9_s09,a_b11_s09,a_b14_s09,a_b15_s09,a_b16_s09,a_b18_s09,a_b20_s09,a_b21_s09,a_b22_s09,a_b25_s09,a_b26_s09,0,0])
IACW_filled = np.array([0,0,0,0,wa_b8_s09,0,0,0,0,wa_b16_s09,0,0,wa_b21_s09,0,0,0,0,0])
IACB_filled =  np.array([ba_b1_s09,0,0,0,0,0,0,0,0,0,0,0,0,0,0,ba_b26_s09,0,b29_s09])

#Ash labels --Summer--
IACG_labels = np.array([3,5,7,8,9,11,14,15,16,18,20,21,22,25,26])
IACW_labels = np.array([8,16,21])
IACB_labels = np.array([1,26,29])

##Comparision_Data:

#Time-Scale regeneration data burned sites 
TSR = np.array([[b1_s09,b1_s17],[b3_s09,b3_s17,b3_w17],[b5_s09,b5_s17],[b7_s09,b7_s17,b7_w17],[b8_s09,b8_w17,b8_s17],[b9_s09,b9_s17],[b11_s09,b11_w17,b11_s17],[b14_s09,b14__w17,b14_s17],[b15_s09,b15__w17,b15_s17],[b16_s09,b16__w17,b16_s17],[b18_s09,b18__w17,b18_s17],[b20_s09,b20_s17],[b21_s09,b21__w17,b21_s17],[b22_s09,b22__w17,b22_s17],[b25_s09,b25_s17],[b26_s09,b26_s17],[b28_s09,b28_s17],[b29_s09,b29_w17,b29_s17]])

#Time-Scale regeneration data unburned sites 
UTSR = np.array([[ub2_s09,ub2_s17],[ub17_s09,ub17_s17],[ub23_s09,ub23_s17],[ub30_s09,ub30_s17]])


"""N-parameters"""
""" '''N-parameter /n #defintion /n #source upperbound /n #source lowerbound (if source is identical) --> #source"""


''' Soil export due erosion after fire(mg/m^2/yr) '''
#IFE = inside the fire perimeter 
#OFE = outside the fire perimeter
#https://www.sciencedirect.com/science/article/pii/S001282521100002X
#note : upper bound and lower bound are calucalted in the main function

IFE = np.array([56,13.1,6.6,(.5+2.2)/2,45,(.2+2.9)/2,.17,.1,.07,4.34,.24,.48,(2.6+3.5)/2,(1+2)/2,12* (3.5/18), 12 * .5 * ((2.6+3.5)/20),12 * 3.5/18,12 * 21.8/18,.2,8.5,40,.7,.016+.021,8.8,12,.3,.1,.8,.9,.036,12 * .0005/5])
OFE  = np.array([(170+500)/2,(37+94)/2,74,(112+180),3.6,6,18,(13+18)/2,.0004,.31,.16,(.05+1.9)/2,3.4,.3,41.2,27,37.8,.6,4,(2.3+8.9)/2,(40.7+69.1)/2,(11.6+29.5),(2+4)/2,(16+25)/2,.25,.005,.94,.009,1.60])


''' Nitrogen Deposition (mg/m^2/year) '''
#N_dep_L =  lowerbound for nitrogen deposition
#N_dep_H = upperbound fr nitrogen deposition
#source  = https://daac.ornl.gov/CLIMATE/guides/global_N_deposition_maps.html
#note : the upperbound and the lowerbound were calculated in the program Atmospheric_N_Calc.py...
# ...which can be found in the GITHUB repository https://github.com/pshankinclarke/StationFire

N_dep_L = 136.11
N_dep_H = 601.14

# Nitrogen due to Rainfall
# Concentration of nutrients in rain in Pasadena (NH4+ + NO3-) (mg/l)
# source: https://authors.library.caltech.edu/26001/1/AC-2-80.pdf
N_rain_rate_NH4_L = 0.292
N_rain_rate_NO3_L = 1.41

N_rain_rate_NH4_H = .379
N_rain_rate_NO3_H = 1.94


N_rain_rate_L = N_rain_rate_NH4_L + N_rain_rate_NO3_L 
N_rain_rate_H = N_rain_rate_NH4_H + N_rain_rate_NO3_H

## Mean amount of rainfall (liters/m^2/year)
#source:
#note : the upperbound is calculated in the program rain_calc.py...
# ...which can be found in the GITHUB repository https://github.com/pshankinclarke/StationFire
# LOWER BOUND FROM https://www.usclimatedata.com/climate/palmdale/california/united-states/usca0829 from 1981-2010 MAYBE NEED BETTER DATA
rainfall_rate_H = 676.0237095664147 
rainfall_rate_L = 187.96

'''Rate rainfall (mg/m^2/year)'''
n_rate_final_L = rainfall_rate_L * N_rain_rate_L 
n_rate_final_H = rainfall_rate_H  * N_rain_rate_H 

'''Rate nitrogen fixation after fire(mg/m^2/year)'''
#source : Ellis and Kummerow, 1989; Poth, 1982
nf_fixation_L = 20
nf_fixation_H = 4000

''' N deposited from ash mg/m^2'''
#source: upperbound https://link.springer.com/content/pdf/10.1007%2FBF00396774.pdf
#source: lowerbound 
Ash_LB = 2100
Ash_UB = 5800

#soil export due to erosion after fire(mg/m^2/yr)
#nf_erosion_L = -(.0005 * 100000 * FBS[1]/100)
#nf_erosion_H = -(107 * 100000 * FBS[1]/100)


##diff_N_dep = N_dep_H - N_dep_L + 1
##array_N_dep = list(np.linspace(N_dep_L,N_dep_H,num = round(10)))
##
##diff_N_rain = n_rate_final_H - n_rate_final_L + 1
##array_N_rain = np.linspace(n_rate_final_L,n_rate_final_H,num = round(10))
##
##diff_n_fixation = n_fixation_H - n_fixation_L + 1
##array_n_fixation = list(np.linspace(n_fixation_L, n_fixation_H,num = round(10)))




def most_common(List):
  '''These functions calculate the most common values in a list and return the values'''
  #Credit https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(List))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(List)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

def plot_histogram(List1):
    '''Plots  histogram ''' 
    List1_hist = np.histogram(List1)
    plt.hist(List1_hist, bins='auto')
    
def generate_barplot(Array1,Array2,Array3,Array4,title,xlabel,ylabel,label_list,labelA1,labelA2,labelA3,labelA4):
    
    #data to plot
    n_groups = 18

    #create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    
    if Array3 != 'n/a':
        bar_width = 0.2
    elif Array4 != 'n/a':
        bar_width = 0.2
    else :
        bar_width = 0.35
    

    opacity = 0.95
         
    color_list = ['salmon','teal','red','aqua']
     
    rects1 = plt.bar(index, Array1, bar_width,
                     alpha=opacity,
                     color='salmon',
                     label=labelA1)
  
    if Array2 != 'n/a':
        rects2 = plt.bar(index + bar_width, Array2, bar_width,
                         alpha=opacity,
                         color='teal',
                         label=labelA2)
    
    
    if Array3 != 'n/a':
        rects3 = plt.bar(index + 2*bar_width, Array3, bar_width,
                         alpha=opacity,
                         color='red',
                         label=labelA3)     
    if Array4 != 'n/a':
        rects4 = plt.bar(index + 3*bar_width, Array4, bar_width,
                         alpha=opacity,
                         color='aqua',
                         label=labelA4)     


     
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    
    plt.xticks(index + bar_width, label_list)
    plt.legend()
     
    plt.tight_layout()
    plt.show()
    
#fucntion that returns dndt for rates inside the fire perimeter
def model_inside(y,t,k):
    dndt = k
    return dndt

#function that returns dndt for rates outside the fire perimeter
def model_outside(y,t,k):
    dndt = k
    return dndt

def relative_N(List1,List2,labels_list):
    
    if List1 > List2: 
       return print('for site {} the nitrogen decreased over an eight year period from {} to {}'.format(labels_list,'summer','summer'))
    else:
       return  print('for site {} the nitrogen increased over an eight year period frin {} to {}'.format(labels_list,'summer','summer'))

def plot(t,n1,n2,titles,ULB,Final_soilweights,Final_soilweightW):
        plt.plot(t,n1,'b-',linewidth=2,label='k=N_burn_max')
        plt.plot(t,n2,'b--',linewidth=2,label='k=N_burn_min')
        plt.plot(8,Final_soilweights,'ro')
        plt.plot(7,Final_soilweightW,'bo')
        
#        for elem in titles:
        plt.title('{} for site {}'.format(ULB,titles))
#        plt.xlabel('time')
#        plt.ylabel('N/m^2')
        plt.show()

def main():
    #Find the upper and lower bounds for erosion of soil
    if False:
        #If True then the two most frequent erosional values are found and the larger value is used for the upperbound and the smaller value is used for the lowerbound
      
        #upper/lower bound for inside the fire
        call = most_common(IFE)
        newlist = []
        for item in IFE:
            if item != call :
                newlist.append(item)
        call2 = most_common(newlist)
            
        if call2 > call:
            UBE = call2
            LBE = call
        else:
            UBE = call
            LBE = call2        
        
        #upper/lower bound for outside the fire    
        call3 = most_common(OFE)
        for item in OFE:
            if item != call3 :
                newlist.append(item)
        call4 = most_common(newlist)

        if call3 > call4:
            UBEO = call3
            LBEO = call4
        else:
            UBEO = call4
            LBEO = call3       
 
    else:
        ##max and min upper and lower bounds
        UBE = max(IFE)
        LBE = min(IFE)
        
        UBEO = max(OFE)
        LBEO = min(OFE)
    
    #Compare intial and final values --Summer-- nitrogen using barplot.
    generate_barplot(IBS,FBS,FBSW_filled,'n/a','nitrogen v. time','site','n wt%',IFBS_labels,"Summer '09","Summer '17","Winter '17",'n/a')

 
    #Compare final and final values --Summer-- and --Winter-- nitrogen using barplot
    generate_barplot(FBSW_filled,FBS,'n/a','n/a','nitrogen v. time','site','n wt%',IFBS_labels,"Winter '17","Summer '17","n/a",'n/a')
    
    #Compare ash and intial --Summer-
    generate_barplot(IBS,IACG_filled,IACW_filled,IACB_filled,'nitrogen in soil and ash','site','n wt%',IFBS_labels,"Summer '09","Grey ash","White ash","Black ash")    
  
    generate_barplot(IBS,FBS,'n/a','n/a','nitrogen v. time','site','n wt%',IFBS_labels,"Summer '09","Summer '17","Winter '17",'n/a')


    for i in range(len(IFBS_labels)):
        call = relative_N(IBS[i],FBS[i],IFBS_labels[i])


    for i in range(len(IBS)):
        
        #nitrogen export due to erosion outside fire(mg/m^2/yr)
        nf_erosion_L = -(.0005 * 100000 * FBS[i]/100)
        nf_erosion_H = -(107 * 100000 * FBS[i]/100)
    
     
        Intial_weightpercent = IBS[i]
        Final_weightpercent_summer = FBS[i]
        Final_weightpercent_winter = FBSW[i]


        #intial conditions 
        Intial_soilweightU = ( density_soil * depth_sampled * area_sampled ) * Intial_weightpercent + Ash_UB
        
        print((density_soil * depth_sampled * area_sampled ) * Intial_weightpercent)
        Intial_soilweightL = ( density_soil * depth_sampled * area_sampled ) * Intial_weightpercent + Ash_LB

        
        #final conditions
        Final_soilweightS =( density_soil * depth_sampled * area_sampled ) * Final_weightpercent_summer
        Final_soilweightW =( density_soil * depth_sampled * area_sampled ) * Final_weightpercent_winter
        
        
        #times points 
        t = np.linspace(0,8)
        
        #Calculate upper and lower bounds :
        Nf_burn_min = N_dep_L + n_rate_final_L + + nf_fixation_L + nf_erosion_L
        Nf_burn_max = N_dep_H + n_rate_final_H + + nf_fixation_H + nf_erosion_H
        
        ##solve the ode 
      
    
        k = Nf_burn_max
        n1 = odeint(model_inside,Intial_soilweightU,t,args=(k,))
        
        k = Nf_burn_min
        n2 = odeint(model_inside,Intial_soilweightU,t,args=(k,))
        
        model_plots = plot(t,n1,n2,IFBS_labels[i],'upperbound',Final_soilweightS,Final_soilweightW)
        
        k = Nf_burn_max
        n3 = odeint(model_outside,Intial_soilweightL,t,args=(k,))
        
        k = Nf_burn_min
        n4 = odeint(model_outside,Intial_soilweightL,t,args=(k,))
        
        model_plots = plot(t,n1,n2,IFBS_labels[i],'lowerbound',Final_soilweightS,Final_soilweightW)

    
    #    call = plot(t,n1,n2,Final_soilweightS)
    #    plt.plot(7,Final_soilweightW,'ro')


    



if  __name__ == "__main__":
    main()




##combos = product(array_N_dep,array_N_rain)
#
#   
##def iterate_parameters(array_N_dep,array_N_rain):
##    """ """
##    complete = []
##    future_input = []
##    
##    for combo in combos: 
##        complete = [combo] + complete
##    
##    for i in range (len(complete)):
##        sum_list = sum(complete[i])
##        indiv_list = complete[i]
##        if sum_list == 15:
##            print('N deposition is contributing {} and N due to rain fall is contributing {}'.format(indiv_list[0],indiv_list[1]))
##            future_input = future_input + [indiv_list[0],indiv_list[1]]
##    return future_input
##
#

#

#def plot(t,n1,n2,finalS):
#    plt.plot(t,n1,'r-',linewidth=2,label='k=N_burn_max')
#    plt.plot(t,n2,'r--',linewidth=2,label='k=N_burn_min')
#    plt.plot(8,Final_soilweightS,'ro')
#    plt.show()

#

#    ###MAIN

#

###plt.plot(t,n3,'b-',linewidth=2,label='k=N_burn_max')
###plt.plot(t,n4,'b--',linewidth=2,label='k=N_burn_min')
##

