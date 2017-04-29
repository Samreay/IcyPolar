# -*- coding: utf-8 -*-
# NASA SPACE APPS CHALLENGE
# Authors: Glen Rees, Chris Jordan

import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def decimal_date_to_iso(dd):
    if isinstance(dd, str):
        dd = float(dd)

    year = int(dd)
    days = dt.timedelta((dd - year) * 365.25)
    return (days + dt.datetime(year, 1, 1)).isoformat() + 'Z'


def LLA_to_ECEF(u, i, h):
    """ 
    This script takes any given latitude(u) and longitude(i) and elevation (h) and converts it into x,y,z 
    positions. Equation taken from http://au.mathworks.com/help/aeroblks/llatoecefposition.html
    """
    
    R = float(6378137.0)
    b = float(6356752.3)
    f = (R-b)/b
    the=np.arctan( (1-f)**2 * np.tan(u))
    rs = np.sqrt(   R**2 / ((1+(1/1-f)**2)-1  * np.sin(the)**2   ))
    px = rs * np.cos(the) * np.cos(i) + h * np.cos(u) * np.cos(i)
    py = rs * np.cos(the) * np.sin(i) + h * np.cos(u) * np.sin(i)
    pz = rs * np.sin(the) + h * np.sin(u)

    return px, py, pz


def Gen_test(minLng=0.0, maxLng=2.0*np.pi, minLat=-np.pi/2.0, maxLat=np.pi/2.0, num=100):
    
    ''' Generates a basic sphere to test LLA to ECEF conversion'''
    lats = []
    lngs = []
    for lng in np.linspace(minLng,maxLng,num):
        for lat in np.linspace(minLat,maxLat,num):
            lats.append(lat)
            lngs.append(lng)
    elevs = np.random.normal(size=num**2)*100000
    return lats, lngs, elevs


def Plot_test():
    # Generate some data
    lats, lngs, elevs = Gen_test()
    x, y , z = LLA_to_ECEF(lats, lngs, elevs)

    # Plotting to check snesible elliptical conversion
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, s=2)
    plt.show()
