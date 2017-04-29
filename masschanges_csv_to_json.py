import numpy as np
import math
import datetime

file = "./ANT_mass_changes_Watkins053116.csv"
data = np.loadtxt(file, skiprows=14, delimiter=',')

def decyear_to_utc(yeardec):
    frac, year = math.modf(yeardec)
    frac, day = math.modf(frac*365.25)
    frac, hour = math.modf(frac*24)
    frac, minute = math.modf(frac*60)
    frac, second = math.modf(frac*60)
    name = str(int(year)) + str(int(day)) + str(int(hour)) + str(int(minute)) + str(int(second))
    obj = datetime.datetime.strptime(name, '%Y%j%H%M%S').isoformat()
    return obj+"z"

years = data[:,0]
print 2005.54
print decyear_to_utc(2005.54)
