from __future__ import division
import matplotlib
import numpy as np
matplotlib.use('TkAgg') #makes matplotlib work
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm
import math

file = open("data.csv", "r") #open given coordinates and migration data
data = file.read()
data = data.split("\n")

file2 = open("us_outline.csv", "r") #open us outline coordinates
data2 = file2.read()
data2 = data2.split("\n")


xaxis = []
yaxis = []
migration = []
points = []
usxaxis = []
usyaxis = []
datax = []
datay = []
dists = []
avg = 0
avg2 = []


for line in data: #split lines and convert to floats
    line = line.split(",")

    try:
        line[0] = float(line[0])
        line[1] = float(line[1])
        line[2] = float(line[2])
    except:
        line.remove(line[-1])
    datax.append(line[0])
    datay.append(line[1])
    migration.append(line[2])

for line2 in data2:
    line2 = line2.split(",")
    line2[0] = float(line2[0])
    line2[1] = float(line2[1])
    usxaxis.append(line2[0])
    usyaxis.append(line2[1])




kn = input("Enter number of neighbors to use:")


if kn > 0: 
    for row in range(194):
        for col in range(120):
            xaxis.append(row)
            yaxis.append(col)
            dists = []
            for i in range(len(datax)):
                dist = (math.sqrt(math.pow((row - datax[i]), 2) + math.pow((col - datay[i]), 2))) #take distance between points
                dists.append([dist, migration[i]]) #make list of tuples with distance and migration data
            dists.sort(key=lambda x:x[0]) #sort tuples by distance
            avg = 0
            for x in range(kn):
                avg+=dists[x][1] #sum of all migration data within range of k value

            avg2.append(avg/kn) #average of migration data

    plt.plot(usxaxis, usyaxis, color="black")
    splot = plt.scatter(xaxis, yaxis, c=avg2)

    plt.show()
else:
    print "This is not a valid number of neighbors!"

plt.plot(usxaxis, usyaxis, color="black")
splot = plt.scatter(xaxis, yaxis, c=avg2)


plt.show()
