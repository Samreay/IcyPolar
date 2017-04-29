#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import re

import numpy as np
from scipy.interpolate import griddata

import common


def read_NASA_csv(filename, header_length=10):
    with open(filename, 'r') as f:
        lng, lat, elev = [], [], []
        for i, line in enumerate(f):
            if i < header_length:
                continue

            cells = line.replace(", ", ',').split(',')
            lng.append(float(cells[1]))
            lat.append(float(cells[2]))
            elev.append(float(cells[3]))
    return lng, lat, elev


def save_raster_file(data, xmin, ymin, resolution, output_filename=None):
    nrows, ncols = data.shape
    xllcorner = xmin
    yllcorner = ymin
    cellsize = resolution

    if output_filename is None:
        pre, _ = os.path.splitext(f)
        # Strip the leading slashes
        pre = re.search(r"/(.*)", pre).group(1)
        output_filename = pre + "_raster.txt"

    with open(output_filename, 'w') as o:
        o.write("ncols %s\n" % ncols)
        o.write("nrows %s\n" % nrows)
        o.write("xllcorner %s\n" % xllcorner)
        o.write("yllcorner %s\n" % yllcorner)
        o.write("cellsize %s\n" % cellsize)
        o.write("nodata -99.0\n")

        for l in data:
            o.write('\t'.join([str(v) for v in l]))
            o.write('\n')
    
    print("Saved: %s" % output_filename, file=sys.stderr)
    

if __name__ == "__main__":
    for f in sys.argv[1:]:
        # Read CSV file
        lng, lat, elev = read_NASA_csv(f)
        x, y, z = common.LLA_to_ECEF(lng, lat, elev)

        # Resolution is determined by the average separation between points.
        # Use the smallest separation between longitude and latitudes for square pixels.
        resolution = min([np.diff(sorted(x)).mean(), np.diff(sorted(y)).mean()])

        grid_x, grid_y = np.meshgrid(np.arange(x.min(), x.max(), resolution),
                                     np.arange(y.min(), y.max(), resolution))
        cartesian_grid = griddata(np.vstack((x, y)).T, z,
                                  (grid_x, grid_y), method="linear", fill_value=-99)
        save_raster_file(cartesian_grid, x.min(), y.min(), resolution)
