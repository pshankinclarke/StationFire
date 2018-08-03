#! /usr/bin/env python3.6
filein = open('USGS_Arroyo_Seco_09_02_2009_to_08_20_2017.txt')
l=0
r=0
r1=0
t=0
t2=0
for line in filein:
    if l >= 31:
        x=line.strip().split("\t")
        if len(x)==8:
            if x[4]=='':
                print("problem at line",l+1, "with discarge calculation in USGS_Arroyo_Seco_09_02_2009_to_08_20_2017.txt")
                r1=r1+float(x[6])
                t2=t2+1
            else:
                r=r+float(x[4])
                r1=r1+float(x[6])
                t=t+1
                t2=t2+1
        elif len(x)==1:
            y=line.strip().split("    ")
            t=t+1
            t2=t2+1
            r=r+float(y[4])
            r2=r2+1
        else:
            print("problem!!!!!")
    l=l+1
a=r1/t2
b=r/t
print("the mean height for the gauge at arroyo seco in feet (15 minute intervals) is", a, "from 09/02/2009 to 08/20/2017")
print("the mean discharge rate for the gauge at arroyo seco in cubic feet per second is", b, "from 09/02/2009 to 08/20/2017")
#   print(line.strip().split("\t"))
filein.close()
