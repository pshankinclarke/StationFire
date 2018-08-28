#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 15:18:58 2018

@author: parkershankin-clarke
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly.plotly as py
import plotly.graph_objs as go

if False :
    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'
    
    trace0 = go.Table(
      header = dict(
        values = [[''],
                  ['1'],
                  ['2'],
                  ['3 and 4'],
                  ['5'],
                  ['6'],
                  ['7'],
                  ['8'],
                  ['9'],
                  ['10'],
                  ['11'],
                  ['12'],
                  ['13'],
                  ['14'],
                  ['15']],
        line = dict(color = '#506784'),
        fill = dict(color = headerColor),
        align = ['left','center'],
        font = dict(color = 'white', size = 15)
      ),
      cells = dict(
        values = [
          [[  'Latitude', 'Longitude', 'Elevation (Meters)', 'Topography',  'Vegetation', 'Surrounding Land Use','Geology','Fire Severity', 'Ash/Soil Description']],
          [[round(34+(25/60)+(15.3/3600),3), round(-118+(11/60)+(58.6/3600),3), 967, 'Shallow Slope on Small Mountains East of the Main San Gabriels', 'Scrub Brush, Yucca Cactua', 'Forest Service', 'None Recorded', 'Lightly Burned Area with some Evidence of Moderate Burning', 'Ash and Brown Silty Sand']],
          [[round(34+26/60+8.8/3600,3), round(-(118+5/60+19.7/3600),3), 1244, 'Moderate Slope on  Hillside', 'Desert Scrub (Buckwheat, Goldernrod, Artemisia californica)', 'Forest Service','Granitic','Unburned', 'Tan/White Granitic Soil']],
          [[round(34+35/60+27.3/3600,3),round( -(118+5/60+28.3/3600),3), 1197, 'Shallow Slope on  Hillside', 'Desert Scrub (Yucca)', 'Forest Service','Granitic','Lightly Burned with some Evidence of Moderate Burning','Black and White Ash and Sandy and Light Soil with a Granitic Component']],
          [[round(34+18/60+3.4/3600,3), round(-(118+15/60+36.2/3600),3), 532, 'Shallow Slope on Large Outwash Plain', 'Desert Scrub (Yucca, Mountain Mohogany, Sycamore)','Forest Service','Large outwash Plain', 'Lightly to Moderately Burned', 'Red and White-Black Ash and Brown Sand']],
          [[round(34+18/60+10.3/3600,3),round( -(118+15/60+28.4/3600),3), 550, 'No Description','No Description','Residence', 'None Recorded','Burned to the Ground','Ash']],
          [[round(34+17/60+50.4/3600,3),round( -(118+10/60+11.2/3600),3), 930, 'Extremely Steep Slope', 'Desert Scrub (Yucca)', 'Forest Service', 'Lightly Burned Area with Moderately Burned Out Stump Holes','Soil and White, Black and Grey Ash']],
          [[round(34+17/60+32.4/3600,3),round( -(118+14/60+23.2/3600),3), 536, 'Shallow Slope', 'Riparian (Cottonwood, Yucca)', 'Forest Service', 'Granitic', 'Moderately Burned', 'White-Black Ash and Sandy Stream Sediments']],
          [[round(34+17/60+8.0/3600,3), round(-(118+13/60+29.7/3600),3), 580, 'Not Applicable','None Recorded','Vogel Flats House','Not Applicable','House Completely Burned','Ash']],
          [[round(34+17/60+1.6/3600,3), round(-(118+13/60+26.4/3600),3), 564, 'Not Applicable','None Recorded','Vogel Flats House','Not Applicable','House Completely Burned','Ash']],
          [[round(34+18/60+29.7/3600,3),round(-(118+6/60+45.0/3600),3), 982, 'Shallow Hillside', 'Scrub (Oak, Yucca)','Forest Service','Basin, Flood Sediment from Granitic Host Rock','Moderately Burned','Grey Ash and Soil to 3 centimeters depth']],
          [[round(34+17/60+56.7/3600,3), round(-(118+6/60+43.7/3600),3), 'Not Recorded', 'Not Applicable','None Recorded','Church Camp (Camp Colby)','Granitic','Homes Burned to the Ground','Ash']],
          [[round(34+18/60+9.0/3600,3), round(-(118+6/60+47.3/3600),3), 1000, 'Not Applicable','None Recorded','Church Camp (Camp Colby)','Granitic','Buildings Completely Burned','White, Black, Yellow and Red Ash']],
          [[round(34+18/60+38.9/3600,3),round( -(118+5/60+12.1/3600),3), 1038, 'Moderate to Steep Slope','Desert Brush','None Recorded', 'Unconsolidated material made up of Igneous and Metamorphic Rock','Lightly to Moderalely Burned','Ash and Sandy, Silty, Tan/Dark Brown Soil']],
          [[round(34+18/60+52.8/3600,3),round( -(118+5/60+40.1/3600),3), 1042, 'Steep Slope on a Hillside','Chaparral', 'Forest Service','Sedimentary Units','Moderately Burned','White Ash (Charred Soil Present in Ash) and Soil']]],
        line = dict(color = '#506784'),
        fill = dict(color = [rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]),
        align = ['left', 'center'],
        font = dict(color = '#506784', size = 15)
        ))
    
    data = [trace0]
    py.plot(data, filename = 'line', auto_open=True)
    
    
if True: 
    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'
    
    trace0 = go.Table(
      header = dict(
        values = [[''],

                  ['16'],
                  ['17'],
                  ['18 and 19'],
                  ['20'],
                  ['21'],
                  ['22'],
                  ['23'],
                  ['24'],
                  ['25'],
                  ['26 and 27'],
                  ['28'],
                  ['29'],
                  ['30']],
        line = dict(color = '#506784'),
        fill = dict(color = headerColor),
        align = ['left','center'],
        font = dict(color = 'white', size = 15)
      ),
      cells = dict(
        values = [
          [[  'Latitude', 'Longitude', 'Elevation (Meters)', 'Topography',  'Vegetation', 'Surrounding Land Use','Geology','Fire Severity', 'Ash/Soil Description']],
          [[round(34+21/60+30.0/3600,3),round( -(118+6/60+35.9/3600),3), 1172, 'Moderate to Steep Slope on A Hill Side 75-100 feet off Road',  'Chaparral (Yucca), Cactus, Chamise', 'Forest Service','None Recorded','Lightly Burned', 'White Ash w/ Grey Component and Dark/Tan Soil']],
          [[round(34+16/60+36.8/3600,3),round( -(118+18/60+39.8/3600),3), 396, 'Hillside',  'Laurel Sumac (Chaparral)', 'Forest Service','Unconsolidated Sediments','Unburned', 'Soil']],
          [[round(34+14/60+50.4/3600,3),round( -(117+58/60+26.7/3600),3), 745, 'Shallow Slope on a Hillside', 'None Recorded', 'Above Cogswell Dam on Forest Service Land','Granitic','Lightly to Moderately Burned', 'Grey and White Ash and Dark, Loamy Soil']],
          [[round(34+13/60+19.0/3600,3),round( -(118+10/60+38.0/3600),3), 441, 'Moderately Steep Slope on a Hillside above Arroyo Seco River',  'Oak, Sycamore, Yucca and Laurel Sumac (Chaparral)', 'None Recorded','None Recorded','Lightly Burned', 'Grey-Withe Ash/Soil']],
          [[round(34+15/60+53.6/3600,3),round( -(118+8/60+53.7/3600),3), 988, 'Moderately Steep Slope on a Hillside above Arroyo Seco River',  'Predominately Oak with few Pines', 'None Recorded','None Recorded','Lightyly to Moderately Burned', 'Grey-White Ash and Soil']],
          [[round(34+21/60+50.3/3600,3),round( -(118+18/60+27.0/3600),3), 910, 'Moderately Steep Slope',  'Chaparral (Manzanita, Yucca)', 'Not Recorded','Not Recorded','Not Recorded', 'Grey-White Ash and Fine, Aggrigete Tan Soil']],
          [[round(34+14/60+45.0/3600,3),round( -(117+57/60+52.1/3600),3), 'Not Recorded', 'Moderate Slope',  'Chaparral', 'Forest Service Land near Cogswell','Granitic','Unburned', 'Tan to Brown Rocky Granitic Soil with Large Rock Component']],
          [[round(34+20/60+52.3/3600,3),round( -(117+56/60+35.8/3600),3), 2025, 'Moderately Sloped',  'Conifer Forest (Jeffrey Pine)', 'Forest Service Land','Granitic','Unburned', 'Sandy Soil with a Large Rock Component']],
          [[round(34+20/60+50.0/3600,3),round( -(117+59/60+29.8/3600),3), 1832, 'Moderate Slope on a Hillside',  'Yucca, Manzanita, Jeffrey Pine', 'Forest Service','Granitic','Lightly to Moderately Burned', 'Grey Ash, Charred Soil and Loamy, Sandy, medium-Brown Soil']],
          [[round(34+18/60+26.7/3600,3),round( -(118+0/60+9.8/3600),3), 1641, 'Steep Slope on a Hillside',  'Oak, Jeffrey Pine (Forest)', 'Forest Service','Granitic','Moderately Burned', 'Red, Black and Grey Ash and Soil']],
          [[round(34+16/60+41.5/3600,3),round( -(118+3/60+42.9/3600),3), 1574, 'Moderate Slope on a Hillside',  'Oak Trees', 'Surrounding Land Use','Unknown','Lightly Burned', 'Grey Ash and Brown to Black Soil']],
          [[round(34+14/60+51.7/3600,3),round( -(118+1/60+59.9/3600),3), 809, 'Shallow Slope in Lowland Below Steep Hillside',  'Chaparral (Oak, Yuca, Chamise)', 'Forest Service','Unknown','Lightly Burned', 'White-Grey Ash and Dark Loamy Soil']],
          [[round(34+19/60+30.1/3600,3),round( -(117+56/60+13.2/3600),3), 1904, 'Moderately Sloped Hillside Above Stream Channel',  'Oak, Cedar, Pine Forest', 'Forest Service','Granitic','Moderately Burned', 'Grey to White Ash and Brow to Black Soil']]],
        line = dict(color = '#506784'),
        fill = dict(color = [rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]),
        align = ['left', 'center'],
        font = dict(color = '#506784', size = 15)
        ))
    
    data = [trace0]
    py.plot(data, filename = 'line', auto_open=True)


