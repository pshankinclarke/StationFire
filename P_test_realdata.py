#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 21:00:27 2018
@author: parkershankin-clarke
"""


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
FBSW_labels_Filled = np.array([0,3,0,7,8,0,11,14,15,16,18,0,21,22,0,0,0,29])

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
""" '''N-parameter''' /n #defintion /n #source upperbound /n #source lowerbound (if source is identical) --> #source"""

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
# not used LOWER BOUND FROM https://www.usclimatedata.com/climate/palmdale/california/united-states/usca0829 from 1981-2010 MAYBE NEED BETTER DATA
# lower bound used for rain from 09/02/2018 to 8/20/2018 located at 34.4938	-118.2713 near Acton, CA from file "1435436 (ACTON USED)" on github, from NCDC CDO, Order #1435436 (Custom GHCN-Daily CSV) -- link to database https://www.ncdc.noaa.gov/cdo-web/
rainfall_rate_H = 676.0237095664147 
#rainfall_rate_L = 187.96
rainfall_rate_L = 227.7951807

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

'''N leaching mg/m^2/day'''
#http://80.24.165.149/webproduccion/PDFs/01ART05.PDF
#units converted in def main
ResFix_weights = np.array([37,77,136,169])
Sed_weights = np.array([56,115,148])

Res_values_NH4_c = np.array([.17,2.49,.81,0])
Res_values_NH4_f = np.array([.5,2.35,.31,0])

Fix_values_NH4_c = np.array([.32,2.66,.59,0])
Fix_values_NH4_f = np.array([.69,1.78,.62,0])

Sed_values_NH4_c = np.array([.36,.24,0])
Sed_values_NH4_f = np.array([.28,.93,0])

Res_values_NO3_c = np.array([.62,11.38,2.50,.62])
Res_values_NO3_f = np.array([8.88,17.86,0,.73])

Fix_values_NO3_c = np.array([.9,13.13,1.95,.51])
Fix_values_NO3_f = np.array([8.28,17.59,.17,.37])

Sed_values_NO3_c = np.array([.94,.05,.02])
Sed_values_NO3_f = np.array([12.72,.32,1.15])

"""Functions"""

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
    '''Generates barplot'''
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

def relative_N(List1,List2,labels_list,burn,finaltime):
    
    if List1 > List2: 
       return print('for {} site {} the nitrogen decreased over an eight year period from {} to {}'.format(labels_list,burn,'summer',finaltime)),0
    else:
       return  print('for {} site {} the nitrogen increased over an eight year period frin {} to {}'.format(labels_list,burn,'summer',finaltime)),1

def plot(t,n1,n2,n3,n4,titles,ULB,Final_soilweights,Final_soilweightW):
       
        if True:
            plt.plot(t,n1,'b-',linewidth=2,label='k=N_burn_max')
            plt.plot(t,n2,'b--',linewidth=2,label='k=N_burn_min')
        if False:
            plt.plot(t,n3,'r-',linewidth=2,label='k=N_outsideburn_max')
            plt.plot(t,n4,'r--',linewidth=2,label='k=N_outsideburn_min')
        plt.plot(8,Final_soilweights,'ro')
        if Final_soilweightW != 0 and Final_soilweightW != 'n/a' :
            plt.plot(7,Final_soilweightW,'bo')
        
#        for elem in titles: 
        plt.title('{} for site {}'.format(ULB,titles))
        plt.xlabel('time')
        plt.ylabel('N/m^2')
        plt.show()

        
def weighted_mean(values,weights):
    weighted_value = 0
    weight_sum = 0
    for i in range(len(values)):
        weighted_value = (weighted_value + values[i]*weights[i])
        weight_sum = weight_sum + weights[i]
    
    final = weighted_value/weight_sum
    return final


def comb(array_N_input,array_N_output,label):
        
        complete = []
        flab = []
        combos = itertools.product(array_N_input,array_N_output)

        for combo in combos: 
            complete = [combo] + complete
            flab = [label] + flab
        if False:
            print('This is the complete list of combinations for site {}'.format(label))
            print(complete)
            print(len(complete))
        
        return complete,flab
 
    
def iterate_parameters(complete,t,N_Final,y0,label):
    '''This functions takes in different iterations of inputs and outputs and returns a list list of future inputs 
    to use as parameters in the ODE'''
    future_input = []
    target_rate =  (N_Final - y0) / (t[len(t)-1] - t[0]) 
    epsillon = 0
    first_half = True

   
    if first_half:
        for i in range (len(complete)):
            sum_list = sum(complete[i])
            indiv_list = complete[i]
            eptol = True
            while eptol:
                if abs(sum_list - target_rate) < epsillon:
                    print('the minimum epsillon needed is {} for site{}'.format(epsillon,label[0]))
                    print('N input is contributing {} and N output is contributing {} for site {}'.format(indiv_list[0],indiv_list[1],label[0]))
                    future_input = future_input + [indiv_list[0],indiv_list[1]]
                    eptol = False
                else : epsillon += 100
        return future_input
            
def metric(upperbound,lowerbound,point,time,timepoint):
    position_of_timepoint = time.index(timepoint)
    if point <= upperbound[position_of_timepoint] and point >= lowerbound[position_of_timepoint]:
        return 1
    else :
        return 0

def main(): 
    
    ##intialization of lists :
    #call_list, calll_list callll_list are used in order to collect data that determines whether points fit between the upper and lower bounds
    
    metric_sum = np.array([])
    metric_wint =  np.array([])
    metric_control = np.array([])
    relNs = []  
    relNw = []
    relNc = []
    
    
    #Find the upper and lower bounds for erosion of soil
    #If most frequent is true then the two most frequent erosional values are found and the smaller value is
    # designated as the lower bound the larger value is designated as the upperbound 
    
    #UBE = upperbound for erosion inside the fire perimeter
    #LBE = lowerbound for eroision inside the fire perimeter
    #UBEO = upperbound for erosion outside of the fire perimeter
    #LBEO = lowerbound for erosion outside of the fire perimeter
    
    
    mostfrequent = False
    if mostfrequent:
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
    
    if False:
        #prints value for upper and lower bounds respectively (control and non-control)
        print(UBE)
        print(LBE)
        print(UBEO)
        print(LBEO)
        
    if False:
        ## If true  the following barplots are generated:
        
        #Compare intial and final values --Summer-- nitrogen using barplot.
        generate_barplot(IBS,FBS,FBSW_filled,'n/a','intial and final values for nitorgen in soil','site','n wt%',IFBS_labels,"Summer '09","Summer '17","Winter '17",'n/a')
    
        #Compare final and final values --Summer-- and --Winter-- nitrogen using barplot
        generate_barplot(FBSW_filled,FBS,'n/a','n/a','seasonal variation for nitrogen in soil','site','n wt%',IFBS_labels,"Winter '17","Summer '17","n/a",'n/a')
        
        #Compare ash and intial --Summer--
        generate_barplot(IBS,IACG_filled,IACW_filled,IACB_filled,'nitrogen in soil and ash','site','n wt%',IFBS_labels,"Summer '09","Grey ash","White ash","Black ash")    
        
        #Compares intial and final --Summer-- points
        generate_barplot(IBS,FBS,'n/a','n/a','intial and final values for nitorgen in soil','site','n wt%',IFBS_labels,"Summer '09","Summer '17","Winter '17",'n/a')

    
    ##Manipulated data for leaching:
    #Res = resprouters
    #sed = seeders
    #ResFix = resprouster fixators
    
    #control    
    control1 = weighted_mean(Res_values_NH4_c,ResFix_weights)
    control2 = weighted_mean(Fix_values_NH4_c,ResFix_weights)
    control3 = weighted_mean(Sed_values_NH4_c,Sed_weights)
    
    control4 = weighted_mean(Res_values_NO3_c,ResFix_weights)
    control5 = weighted_mean(Res_values_NO3_c,ResFix_weights)
    control6 = weighted_mean(Sed_values_NO3_c,Sed_weights)
    
    #fire
    fire1 = weighted_mean(Res_values_NH4_f,ResFix_weights)
    fire2 = weighted_mean(Fix_values_NH4_f,ResFix_weights)
    fire3 = weighted_mean(Sed_values_NH4_f,Sed_weights)
    
    fire4 = weighted_mean(Res_values_NO3_f,ResFix_weights)
    fire5 = weighted_mean(Fix_values_NO3_f,ResFix_weights)
    fire6 = weighted_mean(Sed_values_NO3_f,Sed_weights)
    
    #firepoints
    firepointsNH4 = [fire1] + [fire2] +[fire3]
    firepointsNO3 = [fire4] + [fire5] +[fire6]
    
    #controlpoints
    controlpointsNH4 = [control1] + [control2] + [control3]
    controlpointsNO3 = [control4] + [control5] + [control6]
    
    #maximum/minimum fire
    maxfireNH4 = -max(firepointsNH4) * 365.242199
    minfireNH4 = -min(firepointsNH4) * 365.242199
  
    maxfireNO3 = -max(firepointsNO3) * 365.242199
    minfireNO3 = -min(firepointsNO3) * 365.242199
    
    #maximum/minimum control
    maxcontrolNH4 = -max(controlpointsNH4) * 365.242199
    mincontrolNH4 = -min(controlpointsNH4) * 365.242199
    
    maxcontrolNO3 =  -max(controlpointsNO3) * 365.242199
    mincontrolNO3 =  -min(controlpointsNO3) * 365.242199
   
    #sum of maxium/minimum fire
    maxfireleach = maxfireNH4 + maxfireNO3
    minfireleach = minfireNH4 + minfireNO3
    
    maxcontrolleach = maxcontrolNH4 + maxcontrolNO3
    mincontrolleach = mincontrolNH4 + mincontrolNO3
   

    if False:
        #if true then a function is called that tells the user whether or not nitrogen has increased between the two sampling periods of the fire for --Summer-- and --Winter-- respectively 
        for i in range(len(IFBS_labels)):
            call = relative_N(IBS[i],FBS[i],IFBS_labels[i],'burn','summer')
            if IBS[i] != 0:
                call,number = relative_N(IBS[i],FBSW_filled[i],IFBS_labels[i],'burn','winter')
                relNw = np.append(relNw,number)
        sum_relNw = (sum(relNw)/len(relNw)) * 100
        print('nitrogen has increased at {}% of winter sites sampled'.format( sum_relNw))
                
                        
    if False: 
        #if true then a function is called that tells the user whether or not nitrogen has increased between the two sampling periods of the control for --Summer-- 
        for j in range(len(IFUBS_labels)):
            call,number = relative_N(IUBS[j],FUBS[j],IFUBS_labels[j],'control','summer')
            relNs = np.append(relNs,number)
        sum_relNs = (sum(relNs)/len(relNs)) * 100
        print('nitrogen has increased at {}% of winter sites sampled'.format( sum_relNs))
            

    if True :
        ##This block of code analyzes the control samples
        for j in range(len(IFUBS_labels)):
            
            #nitrogen export due to erosion inside fire(mg/m^2/yr)
            no_erosion_L = -(LBEO * 100000 * IUBS[j]/100)
            no_erosion_H = -(UBEO * 100000 * IUBS[j]/100)
            
            #input parameters
            No_input_L = N_dep_L + n_rate_final_L + nf_fixation_L
            No_input_H = N_dep_H + n_rate_final_H + nf_fixation_H
            
            #output parameters
            No_output_L = no_erosion_L + mincontrolleach 
            No_output_H = no_erosion_H + maxcontrolleach    
            
            #upper and lower bounds
            No_max = No_input_H + No_output_H
            No_min =  No_input_L + No_output_L
            
            #intial and final weight percent for control
            Intial_weightpercent_control = IUBS[j]/100
            Final_weightpercent_summer_control = FUBS[j]/100
        
            #intial conditions 
            Intial_soilweightU = ( density_soil * depth_sampled * area_sampled ) * Intial_weightpercent_control + Ash_UB
            Intial_soilweightL = ( density_soil * depth_sampled * area_sampled ) * Final_weightpercent_summer_control + Ash_LB
            
            #final conditions
            Final_soilweightS_control =( density_soil * depth_sampled * area_sampled ) * Final_weightpercent_summer_control

            #times points 
            t = np.linspace(0,8)
                
            if False:
                #Iterations possible to get from iintial condition to --Summer-- points for points outside the fire perimeter
                #Nos = nitrogen outside fire perimeter summer
                number_of_equally_spaced_points  = 5
                Noslabs = []
                #make sure that you are making your arrays in the correct order
                if No_output_H < No_output_L and No_input_H < No_input_L :
                    if False:
                        print('There is an error for the control iterations')
                        print('the No_output_H is {} and the No_output_L is {} '.format(No_output_H, No_output_L))
                        print('the No_input_H is {} and the No_input_L is {} '.format(No_input_H, No_input_L))
                    array_Nos_output = np.linspace(No_output_H,No_output_L,num = number_of_equally_spaced_points)
                    array_Nos_input = np.linspace(No_input_H,No_input_L,num = number_of_equally_spaced_points)
                    IFUBS_label = IFUBS_labels[j]
                    combinations,Noslabs = comb(array_Nos_input,array_Nos_output,IFUBS_label)
                    call = iterate_parameters(combinations,t,Final_soilweightS_control,Intial_soilweightU,Noslabs)
                else: 
                    if False:
                        print('There is an error for the control iterations')
                        print('the No_output_H is {} and the No_output_L is {} '.format(No_output_H, No_output_L))
                        print('the No_input_H is {} and the No_input_L is {} '.format(No_input_H, No_input_L))
                    array_Nos_output = np.linspace(No_output_L,No_output_H,num = number_of_equally_spaced_points)
                    array_Nos_input = np.linspace(No_input_L,No_input_H,num = number_of_equally_spaced_points)
                    IFUBS_label = IFUBS_labels[j]
                    combinations,Noslabs = comb(array_Nos_input,array_Nos_output,IFUBS_label)
                    call = iterate_parameters(combinations,t,Final_soilweightS_control,Intial_soilweightU,Noslabs)   
            
            if True:
                ##Solve differential equations
                
                #Calculate upper and lower bounds outside the burn area :
                Nf_control_min = N_dep_L + n_rate_final_L + nf_fixation_L + no_erosion_L + mincontrolleach
                Nf_control_max = N_dep_H + n_rate_final_H + nf_fixation_H + no_erosion_H + maxcontrolleach
                
                if False:
                    #if there is a problem one can view the values of the individual parameters and total inputs and outputs
                    if False:
                        print('N_dep_L is {}'.format(N_dep_L))
                        print('N_dep_H is {}'.format(N_dep_H))
                        print('n_rate_final_L is {}'.format(n_rate_final_L))
                        print('n_rate_final_H is {}'.format(n_rate_final_H))
                        print('nf_fixation_L is {}'.format(nf_fixation_L))
                        print('nf_fixation_H is {}'.format(nf_fixation_H))
                        print('no_erosion_L is {}'.format(no_erosion_L))
                        print('no_erosion_H is {}'.format(no_erosion_H))
                        print('mincontrolleach is {}'.format(mincontrolleach))
                        print('maxcontrolleach is {}'.format(maxcontrolleach))
                    if False:
                        print('Nf_control_min is {}'.format(Nf_control_min))
                        print('Nf_control_max is {}'.format(Nf_control_max))

          

                # solving ODE using the intial conditions for the upperbound value for soil
                k = Nf_control_max
                c1U = odeint(model_inside,Intial_soilweightU,t,args=(k,))
                k = Nf_control_min
                c2U = odeint(model_inside,Intial_soilweightU,t,args=(k,))
                
                # solving ODE using the intial conditions for the lowerbound value for soil
                k = Nf_control_max
                c1L = odeint(model_inside,Intial_soilweightL,t,args=(k,))
                k = Nf_control_min
                c2L =  odeint(model_inside,Intial_soilweightL,t,args=(k,))
                
                #check values
                if False:
                    print('the value for c1U is {}'.format(c1U))
                    print('the value for c2U is {}'.format(c2U))
                    print('the value for c1L is {}'.format(c1L))
                    print('the value for c2L is {}'.format(c2L))
                            
                        
                if False :
                    #plots the differential equations         
                    model_plotsU = plot(t,c1U,c2U,'n/a','n/a',IFBS_labels[j],'upperbound',Final_soilweightS_control,'n/a')
                    model_plotsL = plot(t,c1L,c2L,'n/a','n/a',IFBS_labels[j],'lowerbound',Final_soilweightS_control,'n/a')
            
            met = True
            if met:
                #Metric that shows percentage of point between the upper and lower bound
                 metricc = metric(list(c2U),list(c1U),Final_soilweightS_control,list(np.linspace(0,8)),8)
                 metric_control = np.append(metric_control,metricc)
        
        if met:
            #prints the percentage of points that are inbetween the upper and lower bounds         
            sum_controlpoints = (sum(metric_control)/len(metric_control)) * 100
            print('The percentage of points that is exist between the upper and lower control bounds is {}%'.format(sum_controlpoints))
        
    
    if False:
        for i in range(len(IBS)):    
           
            #nitrogen export due to erosion inside fire(mg/m^2/yr)
            nf_erosion_L = -(LBE * 100000 * FBS[i]/100)
            nf_erosion_H = -(UBE * 100000 * FBS[i]/100)
            
            no_erosion_L = -(LBEO * 100000 * IBS[i]/100)
            no_erosion_H = -(UBEO * 100000 * IBS[i]/100)
            
            #intial and final weight percent
            Intial_weightpercent = IBS[i]/100
            Final_weightpercent_summer = FBS[i]/100
            Final_weightpercent_winter = FBSW_filled[i]/100
        
            #intial conditions 
            Intial_soilweightU = ( density_soil * depth_sampled * area_sampled ) * Intial_weightpercent + Ash_UB
            Intial_soilweightL = ( density_soil * depth_sampled * area_sampled ) * Intial_weightpercent + Ash_LB
        
            #final conditions
            Final_soilweightS =( density_soil * depth_sampled * area_sampled ) * Final_weightpercent_summer
            Final_soilweightW =( density_soil * depth_sampled * area_sampled ) * Final_weightpercent_winter
                    
            #times points 
            t = np.linspace(0,8)
            
            #Calculate upper and lower bounds inside the burn area :
            Nf_burn_min = N_dep_L + n_rate_final_L + + nf_fixation_L + nf_erosion_L  + minfireleach
            Nf_burn_max = N_dep_H + n_rate_final_H + + nf_fixation_H + nf_erosion_H  + maxfireleach
            
            #input parameters
            Nf_input_L = N_dep_L + n_rate_final_L + nf_fixation_L
            Nf_input_H = N_dep_H + n_rate_final_H + nf_fixation_H
            
            
            #output parameters
            Nf_output_L = nf_erosion_L + minfireleach 
            Nf_output_H = nf_erosion_H + maxfireleach
            

            

                 
            
            if False :
                #Iterations possible to get from intial condition to summer points for points inside the fire perimeter
                #Nfs = nitrogen inside fire perimeter summer
                Nfslabs = []
                array_Nfs_output = np.linspace(Nf_output_H,Nf_output_L,num = 5)
                array_Nfs_input = np.linspace(Nf_input_H,Nf_input_L,num = 5)
                IFBS_label = IFBS_labels[i]
                combinations,Nfslabs = comb(array_Nfs_input,array_Nfs_output,IFBS_label)
                call = iterate_parameters(combinations,t,Final_soilweightS,Intial_soilweightU,Nfslabs)
                
            
            if False:
#                #iterations possible to get from intial condition to winter points
                 #Nfw
                Nfwlabs = []
                array_Nfw_output =  np.linspace(Nf_output_H,Nf_output_L,num = 5)
                array_Nfw_input = np.linspace(Nf_input_H,Nf_input_L,num = 5)
                FBSW_label = FBSW_labels_Filled[i]
                if FBSW_label != 0 :
                    combinations,Nfwlabs = comb(array_Nfw_input,array_Nfw_output,FBSW_label)
                    call = iterate_parameters(combinations,t,Final_soilweightS,Intial_soilweightU,Nfwlabs)

                
            if True :
                #Solves the differentials equations  
                k = Nf_burn_max
                n1 = odeint(model_inside,Intial_soilweightU,t,args=(k,))
                k = Nf_burn_min
                n2 = odeint(model_inside,Intial_soilweightU,t,args=(k,))

                
            
            
            if True :
                #plots the differential equations         
                model_plots = plot(t,n1,n2,'n/a','n/a',IFBS_labels[i],'upperbound',Final_soilweightS,Final_soilweightW)
                model_plots = plot(t,n1,n2,'n/a','n/a',IFBS_labels[i],'lowerbound',Final_soilweightS,Final_soilweightW)
                    
                    
           
            metricsummer = True 
            if metricsummer:
                #metric(upperbound,lowerbound,point,time,timepoint)
#                #Metric that shows percentage of point between the upper and lower bound
                 
#                metric for summerpoint
                metrics = metric(list(n2),list(n1),Final_soilweightS,list(np.linspace(0,8)),8)
                metric_sum = np.append(metric_sum,metrics)
                
        if metricsummer:        
            sum_controlpoints = (sum(metric_sum)/len(metric_sum)) * 100
            print('The percentage of points that is exist between the upper and lower control bounds for the summer points is {}%'.format(sum_controlpoints))
             

    if False:
        #code finds metrics for winter points
        for i in range(len(FBSW)):    
           
            #nitrogen export due to erosion inside fire(mg/m^2/yr)
            nf_erosion_L = -(LBE * 100000 * FBSW[i]/100)
            nf_erosion_H = -(UBE * 100000 * FBSW[i]/100)
            
            
            #intial and final weight percent
            Intial_weightpercent = IBS[i]/100
            Final_weightpercent_winter = FBSW[i]/100
        
            #intial conditions 
            Intial_soilweightU = ( density_soil * depth_sampled * area_sampled ) * Intial_weightpercent + Ash_UB
            Intial_soilweightL = ( density_soil * depth_sampled * area_sampled ) * Intial_weightpercent + Ash_LB
        
            #final conditions
            Final_soilweightW =( density_soil * depth_sampled * area_sampled ) * Final_weightpercent_winter
                    
            #times points 
            t = np.linspace(0,7)
            
            #Calculate upper and lower bounds inside the burn area :
            Nf_burn_min = N_dep_L + n_rate_final_L + + nf_fixation_L + nf_erosion_L  + minfireleach
            Nf_burn_max = N_dep_H + n_rate_final_H + + nf_fixation_H + nf_erosion_H  + maxfireleach
            
            #input parameters
            Nf_input_L = N_dep_L + n_rate_final_L + nf_fixation_L
            Nf_input_H = N_dep_H + n_rate_final_H + nf_fixation_H
            
            
            #output parameters
            Nf_output_L = nf_erosion_L + minfireleach 
            Nf_output_H = nf_erosion_H + maxfireleach
            

            if True :
                #Solves the differentials equations  
                k = Nf_burn_max
                n1 = odeint(model_inside,Intial_soilweightU,t,args=(k,))
                k = Nf_burn_min
                n2 = odeint(model_inside,Intial_soilweightU,t,args=(k,))

             
            if True:
       
                metricw = metric(list(n2),list(n1),Final_soilweightW,list(np.linspace(0,7)),7)
                metric_wint = np.append(metric_wint,metricw)
        
        sum_controlpoints = (sum(metric_wint)/len(metric_wint)) * 100
        print('The percentage of points that is exist between the upper and lower control bounds for the winter points is {}%'.format(sum_controlpoints))
     

if  __name__ == "__main__":
    main()


