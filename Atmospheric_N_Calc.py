#! /usr/bin/env python3.6
filein = open('N-deposition1860.txt')
lon_space=3.75
lat_space=5
lon=-90 #90 south to 90 north
lat=-180 #180 west to 180 east
l=0
loni=lon
lati=lat
for line in filein:
    if l>=2:
        x=line.strip().split("\t")
        for c in range(len(x)):
            if lat>=180:
                lat=lati
                lon=lon+lon_space
            if lat==-120 and lon==33.75:
                print("In 1860 N deposition was", x[c],"mg N/m^2/yr at lat=", lat,"and lon=",lon)
            lat=lat+lat_space
    l=l+1
filein.close

filein = open('N-deposition1993.txt')
lon_space=3.75
lat_space=5
lon=-90 #90 south to 90 north
lat=-180 #180 west to 180 east
l=0
loni=lon
lati=lat
for line in filein:
    if l>=2:
        x=line.strip().split("\t")
        for c in range(len(x)):
            if lat>=180:
                lat=lati
                lon=lon+lon_space
            if lat==-120 and lon==33.75:
                print("In 1993 N deposition was", x[c],"mg N/m^2/yr at lat=", lat,"and lon=",lon)
            lat=lat+lat_space
    l=l+1
filein.close

filein = open('N-deposition2050.txt')
lon_space=3.75
lat_space=5
lon=-90 #90 south to 90 north
lat=-180 #180 west to 180 east
l=0
loni=lon
lati=lat
for line in filein:
    if l>=2:
        x=line.strip().split("\t")
        for c in range(len(x)):
            if lat>=180:
                lat=lati
                lon=lon+lon_space
            if lat==-120 and lon==33.75:
                print("In 2050 N deposition is estimated", x[c],"mg N/m^2/yr at lat=", lat,"and lon=",lon)
            lat=lat+lat_space
    l=l+1
filein.close










filein = open('NHx-deposition1860.txt')
lon_space=3.75
lat_space=5
lon=-90 #90 south to 90 north
lat=-180 #180 west to 180 east
l=0
loni=lon
lati=lat
for line in filein:
    if l>=2:
        x=line.strip().split("\t")
        for c in range(len(x)):
            if lat>=180:
                lat=lati
                lon=lon+lon_space
            if lat==-120 and lon==33.75:
                print("In 1860 NHx deposition was", x[c],"mg N/m^2/yr at lat=", lat,"and lon=",lon)
            lat=lat+lat_space
    l=l+1
filein.close

filein = open('NHx-deposition1993.txt')
lon_space=3.75
lat_space=5
lon=-90 #90 south to 90 north
lat=-180 #180 west to 180 east
l=0
loni=lon
lati=lat
for line in filein:
    if l>=2:
        x=line.strip().split("\t")
        for c in range(len(x)):
            if lat>=180:
                lat=lati
                lon=lon+lon_space
            if lat==-120 and lon==33.75:
                print("In 1993 NHx deposition was", x[c],"mg N/m^2/yr at lat=", lat,"and lon=",lon)
            lat=lat+lat_space
    l=l+1
filein.close

filein = open('NHx-deposition2050.txt')
lon_space=3.75
lat_space=5
lon=-90 #90 south to 90 north
lat=-180 #180 west to 180 east
l=0
loni=lon
lati=lat
for line in filein:
    if l>=2:
        x=line.strip().split("\t")
        for c in range(len(x)):
            if lat>=180:
                lat=lati
                lon=lon+lon_space
            if lat==-120 and lon==33.75:
                print("In 2050 NHx deposition is estimated", x[c],"mg N/m^2/yr at lat=", lat,"and lon=",lon)
            lat=lat+lat_space
    l=l+1
filein.close

























filein = open('NOy-deposition1860.txt')
lon_space=3.75
lat_space=5
lon=-90 #90 south to 90 north
lat=-180 #180 west to 180 east
l=0
loni=lon
lati=lat
for line in filein:
    if l>=2:
        x=line.strip().split("\t")
        for c in range(len(x)):
            if lat>=180:
                lat=lati
                lon=lon+lon_space
            if lat==-120 and lon==33.75:
                print("In 1860 NOy deposition was", x[c],"mg N/m^2/yr at lat=", lat,"and lon=",lon)
            lat=lat+lat_space
    l=l+1
filein.close

filein = open('NOy-deposition1993.txt')
lon_space=3.75
lat_space=5
lon=-90 #90 south to 90 north
lat=-180 #180 west to 180 east
l=0
loni=lon
lati=lat
for line in filein:
    if l>=2:
        x=line.strip().split("\t")
        for c in range(len(x)):
            if lat>=180:
                lat=lati
                lon=lon+lon_space
            if lat==-120 and lon==33.75:
                print("In 1993 NOy deposition was", x[c],"mg N/m^2/yr at lat=", lat,"and lon=",lon)
            lat=lat+lat_space
    l=l+1
filein.close

filein = open('NOy-deposition2050.txt')
lon_space=3.75
lat_space=5
lon=-90 #90 south to 90 north
lat=-180 #180 west to 180 east
l=0
loni=lon
lati=lat
for line in filein:
    if l>=2:
        x=line.strip().split("\t")
        for c in range(len(x)):
            if lat>=180:
                lat=lati
                lon=lon+lon_space
            if lat==-120 and lon==33.75:
                print("In 2050 NOy deposition is estimated", x[c],"mg N/m^2/yr at lat=", lat,"and lon=",lon)
            lat=lat+lat_space
    l=l+1
filein.close
