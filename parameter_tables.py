#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly.plotly as py
import plotly.graph_objs as go

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

##Chart 1
if False:
    #All paramters except erosion
    trace0 = go.Table(
      header = dict(
        values = [['Parameter'],
                      ['Upperbound control '],
                      ['Lowerbound control '],
                      ['Upperbound inside fire perimeter'],
                      ['Lowerbound inside fire perimeter']],
        line = dict(color = '#506784'),
        fill = dict(color = headerColor),
        align = ['left','center'],
        font = dict(color = 'white', size = 12)
      ),
      cells = dict(
        values = [
          [[ 'N-depositon', 'Rainfall','Fixation', 'Leaching']],
          [[601.14, 676.02, 4000, 1807.95]],
          [[136.11, 227.80, 20, 1192.99 ]],
          [[136.11, 227.80, 20, 1192.99 ]],
          [[136.11, 227.80, 20, 1192.99 ]]], 
        line = dict(color = '#506784'),
        fill = dict(color = [rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]),
        align = ['left', 'center'],
        font = dict(color = '#506784', size = 11)
        ))
    
    data = [trace0]
    py.plot(data, filename = 'line', auto_open=True)

##Chart2    
if False:
    #Erosion
    trace0 = go.Table(
      header = dict(
        values = [['Parameter'],
                      ['Upperbound control'],
                      ['Lowerbound control'],
                      ['Upperbound inside fire perimeter'],
                      ['Lowerbound inside fire perimeter']],
        line = dict(color = '#506784'),
        fill = dict(color = headerColor),
        align = ['left','center'],
        font = dict(color = 'white', size = 12)
      ),
      cells = dict(
        values = [
          [[ 'Erosion',]],
          [[335]],
          [[.0004 ]],
          [[56.0000]],
          [[.0012000 ]]], 
        line = dict(color = '#506784'),
        fill = dict(color = [rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]),
        align = ['left', 'center'],
        font = dict(color = '#506784', size = 11)
        ))
    
    data = [trace0]
    py.plot(data, filename = 'line', auto_open=True)
    
##Chart3    
if True:
    #Ash input
    trace0 = go.Table(
      header = dict(
        values = [['Parameter'],
                      
                      
                      ['Upperbound inside fire perimeter'],
                      ['Lowerbound inside fire perimeter']],
        line = dict(color = '#506784'),
        fill = dict(color = headerColor),
        align = ['left','center'],
        font = dict(color = 'white', size = 12)
      ),
      cells = dict(
        values = [
          [[ 'Ash']],
          [[5800]],
          [[2100]]], 
        line = dict(color = '#506784'),
        fill = dict(color = [rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]),
        align = ['left', 'center'],
        font = dict(color = '#506784', size = 11)
        ))
    
    data = [trace0]
    py.plot(data, filename = 'line', auto_open=True)
    

    
    
    
