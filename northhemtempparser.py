import numpy as np
import json
import datetime

# Nice one line read in that gives a structured array which is a bit hard to deal with
# global_temp = np.genfromtxt("globaltemp.csv", skip_header=1, delimiter=',',
#                             dtype=(int, float, float, float, float, float, float, float, float, float, float, float, float, float)
#                             , names=True)

# Open a csv file
global_temp = open('data/northhem.csv', 'r')
global_temp.next()

# Creation of dictionary for json file
tempdic = {}

for row in global_temp:
    vals = row.split(',') # because csv
    for i in range(12): #going through each month
        year = str(vals[0])
        month = str(i+1)

        datename = year + '_' + month #make a string of the date in year_month form
        date = datetime.datetime.strptime(datename, '%Y_%m').isoformat() #creating standard datetime format
        date = date+'z' #apparently datetime needs a z on the end so hacky fix

        tempdic[date] = vals[i+1] #fill that dictionary

json_file = open('data/north_hem_temp_ave.json', 'w') #open a json file
json.dump(tempdic, json_file) #fill that json file
json_file.write('\n')
json_file.close()

