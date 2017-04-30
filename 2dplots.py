import numpy as np
import csv
import matplotlib.pyplot as plt

# Nice one line read in that gives a structured array which is a bit hard to deal with
# global_temp = np.genfromtxt("globaltemp.csv", skip_header=1, delimiter=',',
#                             dtype=(int, float, float, float, float, float, float, float, float, float, float, float, float, float)
#                             , names=True)

# Open a csv file
global_temp = open('data/globaltemp.csv', 'r')
global_temp.next()

mass = open("data/mass.csv", 'r')
mass.next()

co2data =  open("data/co2.txt", 'r') #file pointer? unsure, but looks like it
co2 = csv.reader(co2data, delimiter=' ', skipinitialspace=True) # read dat data

years = []
temp = []
massyears = []
greenlandmass = []
antarcticmass = []
co2years = []
co2time = []
colevels = []


for line in global_temp:
    numbers = line.split(',')
    years.append(float(numbers[0]))
    temp.append(float(numbers[12]))

for line in mass:
    numbers = line.split(',')
    massyears.append(int(float(numbers[0])))
    antarcticmass.append(float(numbers[2]))

for line in co2:
    co2years.append(int(line[0]))
    colevels.append(float(line[4]))
    co2time.append(float(line[1]))

for iyear in range(2009, 2014):
    tempfig = plt.figure()
    ax = tempfig.add_subplot(111)
    ax.plot(years,temp, color="#5791af")
    ax.set_xlabel("Year")
    ax.set_ylabel("Difference from Average Temperature (Celcius)")
    ax.axvline(iyear, color="#ff6060")
    ax.axhline(0, color="#6EBA22")
    # ax.text(0.65, 0.3, "Average Temperature")
    # ax.axvline(0.5*total_distance, color="black", lw="0.3")
    tempfig.savefig("2dplots/%s_temp.pdf" %iyear, bbox_inches='tight', Transparency=True, dpi=300)

    massfig = plt.figure()
    ax = massfig.add_subplot(111)
    ax.plot(massyears,antarcticmass, color="#5791af")
    ax.set_xlabel("Year")
    ax.set_ylabel("Antarctic Ice Mass Change (Gt)")
    ax.axvline(2009, color="#ff6060")
    # ax.text(0.65, 0.3, "Average Temperature")
    # ax.axvline(0.5*total_distance, color="black", lw="0.3")
    massfig.savefig("2dplots/%s_mass.pdf" %iyear, bbox_inches='tight', Transparency=True, dpi=300)

    co2fig = plt.figure()
    ax = co2fig.add_subplot(111)
    ax.plot(co2years, colevels, color="#5791af")
    ax.set_xlabel("Year")
    ax.set_ylabel("Global CO2 Average (ppm)")
    ax.axvline(2009, color="#ff6060")
    co2fig.savefig("2dplots/%s_co2.pdf" %iyear, bbox_inches='tight', Transparency=True, dpi=300)

