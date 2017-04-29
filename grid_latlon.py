#!/usr/bin/env python

import sys

import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

import common


def read_NASA_csv(filename, header_length=10):
    with open(x, 'r') as f:
        lng, lat, elev = [], [], []
        for i, line in enumerate(f):
            if i < header_length:
                continue

            line = line.replace(", ", ',')
            cells = line.split(',')

            lng.append(float(cells[1]))
            lat.append(float(cells[2]))
            elev.append(float(cells[3]))
    return lng, lat, elev


# Read CSV file
lng, lat, elev = np.loadtxt(sys.argv[1], delimiter=',', unpack=True)

x, y, z = common.LLA_to_ECEF(lng, lat, elev)

# Resolution is determined by the average separation between points.
# Use the smallest separation between longitude and latitudes for square pixels.
resolution = min([np.diff(sorted(x)).mean(), np.diff(sorted(y)).mean()])

grid_x, grid_y = np.meshgrid(np.arange(x.min(), x.max(), resolution),
                             np.arange(y.min(), y.max(), resolution))
cartesian_grid = griddata(np.vstack((x, y)).T, z,
                          (grid_x, grid_y), method="linear", fill_value=-99)

plt.imshow(np.log(cartesian_grid))
plt.show()
