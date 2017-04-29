import numpy as np
import json
import datetime

# Nice one line read in that gives a structured array which is a bit hard to deal with
# global_temp = np.genfromtxt("globaltemp.csv", skip_header=1, delimiter=',',
#                             dtype=(int, float, float, float, float, float, float, float, float, float, float, float, float, float)
#                             , names=True)

# Open a csv file
global_temp = open('globaltemp.csv', 'r')
global_temp.next()

# Creation of dictionary for json file
globaltempdic = {}

for row in global_temp:
    vals = row.split(',') # because csv
    for i in range(12): #going through each month
        year = str(vals[0])
        month = str(i+1)

        datename = year + '_' + month #make a string of the date in year_month form
        date = datetime.datetime.strptime(datename, '%Y_%m').isoformat() #creating standard datetime format
        date = date+'z' #apparently datetime needs a z on the end so hacky fix

        globaltempdic[date] = vals[i+1] #fill that dictionary

json_file = open('globaltempave.json', 'w') #open a json file
json.dump(globaltempdic, json_file) #fill that json file
json_file.write('\n')
json_file.close()


# month_list = [global_temp["Jan"], global_temp["Feb"], global_temp["Mar"],
#               global_temp["Apr"], global_temp["May"], global_temp["Jun"],
#               global_temp["Jul"], global_temp["Aug"], global_temp["Sep"],
#               global_temp["Oct"], global_temp["Nov"], global_temp["Dec"]]

# print month_list

# output_dic[global_temp["Year"]] = (global_temp["JD"], month_list)

# output_dic = {}
# years = global_temp["Year"]
#
# for year,  in years:
#     output_dic[year] =
# output_dic[global_temp["Year"]] = (monthlist)
# print output_dic
#
#
