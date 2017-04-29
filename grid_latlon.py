#!/usr/bin/env python

import sys

import numpy as np
from scipy.interpolate import griddata


# Read CSV file
lng, lat, elev = np.loadtxt(sys.argv[1], delimiter=',', unpack=True)

# Resolution is determined by the average separation between points.
# Use the smallest separation between longitude and latitudes for square pixels.
resolution = min([np.diff(sorted(lng)).mean(), np.diff(sorted(lat)).mean()])

grid_x, grid_y = np.meshgrid(np.arange(lng.min(), lng.max(), resolution),
                             np.arange(lat.min(), lat.max(), resolution))
cartesian_grid = griddata(np.vstack((lng, lat)).T, elev,
                          (grid_x, grid_y), method="linear", fill_value=-99)

# import matplotlib.pyplot as plt
# plt.imshow(cartesian_grid)
# plt.show()
