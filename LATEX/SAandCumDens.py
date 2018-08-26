#! /usr/bin/env python3.6
import time
import numpy as np
import matplotlib.pyplot as plt
start_time = time.time()
d=[0, 0.04, 0.07, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 3, 4, 5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 25, 28, 32, 36, 38, 40, 45, 50, 53, 56, 63, 71, 75, 80, 85, 90, 95, 100, 106, 112, 125, 130, 140, 145, 150, 160, 170, 180, 190, 200, 212, 242, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

#reading averages
SAtot={}
SAfrac={}
filein = open('STFin.txt', 'r')
s=-1
avDat=np.zeros((23,101))
for line in filein:
    if len(line) == 6:
        s=s+1
        a, b = [float(a) for a in line.split()]
        i=-1
    else:
        i=i+1
        m1, m2, av, di = [float(a) for a in line.split()]
        avDat[s][i+1]=av
filein.close()

#total surface area
filein2 = open('STFin.txt', 'r')
s=-1
for line in filein2:
    if len(line) == 6:
        s=s+1
        a, b = [float(a) for a in line.split()]
        i=-1
        tot=0
        listSum=[]
    if len(line) != 6:
        i=i+1
        m1, m2, av, di = [float(a) for a in line.split()]
        zzz=(avDat[s][i+1]-avDat[s][i])*((di/2)**2)*(4)*(np.pi)
        listSum.append(zzz)
        if di == 2500:
            SAtot[b]=sum(listSum)
filein2.close()

#relevant surface area fractions
filein3 = open('STFin.txt', 'r')
fileout = open('SAfrac.txt', 'w')
s=-1
for line in filein3:
    if len(line) == 6:
        s=s+1
        a, b = [float(a) for a in line.split()]
        s0t38 = []
        s38t106 = []
        s106t180 = []
        s180t2000 = []
        i=-1
    if len(line) != 6:
        i=i+1
        m1, m2, av, di = [float(a) for a in line.split()]
        zzz=(avDat[s][i+1]-avDat[s][i])*((di/2)**2)*(4)*(np.pi)
        if di >= 0 and di <= 38:
            s0t38.append(zzz)
        elif di > 38 and di <= 106:
            s38t106.append(zzz)
        elif di > 106 and di <= 180:
            s106t180.append(zzz)
        elif di > 180:
            s180t2000.append(zzz)
        if di == 2500:
            l1=sum(s0t38)/SAtot[b]
            l2=sum(s38t106)/SAtot[b]
            l3=sum(s106t180)/SAtot[b]
            l4=sum(s180t2000)/SAtot[b]
            SAfrac[b]=[l1, l2, l3, l4]
            fileout.write('{0:5.0f} {1:5.3f} {2:5.3f} {3:5.3f} {4:5.3f} \n'.format(b, l1, l2, l3, l4))

filein3.close()
fileout.close()

# pie chart plots
filein4 = open('STFin.txt', 'r')
for line in filein4:
    if len(line) == 6:
        t, u = [float(a) for a in line.split()]
        w, b, c, r = SAfrac[u][0], SAfrac[u][1], SAfrac[u][2], SAfrac[u][3]
        e=w+b+c+r
        labels = '0-38 microns', '38-106 microns', '106-180 microns', '180-2000 microns'
        sizes = [(100*w/e), (100*b/e), (100*c/e), (100*r/e)]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        nombre="Surface Area Percentages for Particles in Site "+str(int(u))
        save='SAsite'+str(int(u))
        plt.title(nombre)
        #plt.show()
        plt.savefig(save)
filein4.close()

#plots cumulative distribution functions (CDF) and population density functions (PDF) logscale
d=[0, 0.04, 0.07, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 3, 4, 5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 25, 28, 32, 36, 38, 40, 45, 50, 53, 56, 63, 71, 75, 80, 85, 90, 95, 100, 106, 112, 125, 130, 140, 145, 150, 160, 170, 180, 190, 200, 212, 242, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500]

dLog10=[]
for i in range(len(d)):
    if d[i] != 0:
        dLog10.append(np.log10(d[i]))

filein5 = open('STFin.txt', 'r')
for line in filein5:
    if len(line) == 6:
        i=-1
        t, u = [float(a) for a in line.split()]
        cumY=[]
    if len(line) != 6:
        i=i+1
        m1, m2, av, di = [float(a) for a in line.split()]
        cumY.append(av)
    if i == 99:
        fig = plt.figure()
        ety="Cumulative Distribution for Particles in Site "+str(int(u))
        fig.suptitle(ety, fontsize=14, fontweight='bold')
        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)
        ax.set_xlabel('Log10(Diameter in Microns)')
        ax.set_ylabel('Cumulative Fraction of Particle Abundance')
        save='CDFsite'+str(int(u))
        plt.plot(dLog10, cumY, '-o')
        #plt.show()
        plt.savefig(save)
        useY=[0]
        densY=[]
        for q in range(len(cumY)):
            useY.append(cumY[q])
        for v in range(len(cumY)):
            xyz=(useY[v+1]-useY[v])/(np.log10(d[v+1])-np.log10(d[v]))
            densY.append(xyz)
        fig = plt.figure()
        rty="Population Density for Particles in Site "+str(int(u))
        fig.suptitle(rty, fontsize=14, fontweight='bold')
        ax = fig.add_subplot(111)
        fig.subplots_adjust(top=0.85)
        ax.set_xlabel('Log10(Diameter in Microns)')
        ax.set_ylabel('Particle Frequency in a Given Sample')
        save='PDFsite'+str(int(u))
        plt.plot(dLog10, densY, '-o')
        #plt.show()
        plt.savefig(save)
filein5.close()
print("--- %s seconds ---" % (time.time() - start_time))


