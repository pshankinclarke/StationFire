#! /usr/bin/env python3.6
filein = open('USGS_Lytle_Creek_09_02_2009_to_08_20_2017.txt')
l=0
r=0
t=0
for line in filein:
    if l >= 31:
        x=line.strip().split("\t")
        if len(x)==5:
            r=r+float(x[3])
            t=t+1
        else:
            print("problem!!!!! at line", l+1, "on", x[2] )
    l=l+1
b=r/t

print("the mean rainfall in inches per day is", b, "from 09/02/2009 to 08/20/2017 at Lytle Creek, CA")

r2=r*0.0254*1000 # liters
t2=t/365 # years

b2=r2/t2
print("the mean rainfall in liters per square meter per year is", b2, "from 09/02/2009 to 08/20/2017 at Lytle Creek, CA")




filein.close()
