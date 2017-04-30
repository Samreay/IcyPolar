#!/usr/bin/env python

from __future__ import print_function

import sys
import argparse

import numpy as np
from scipy.interpolate import griddata

import common

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output_filename", required=True,
                    help="Path to the output raster file.")
parser.add_argument("files", nargs='*', help="Files to be processed.")
args = parser.parse_args()


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


def save_raster_file(data, xmin, ymin, resolution, output_filename):
    nrows, ncols = data.shape
    xllcorner = xmin
    yllcorner = ymin
    cellsize = 1

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
    x = np.array([])
    y = np.array([])
    z = np.array([])
    for f in args.files:
        # Read CSV file
        lng, lat, elev = read_NASA_csv(f)
        x2, y2, _ = common.LLA_to_ECEF(lng, lat, elev)
        z2 = elev

        x = np.concatenate((x, x2))
        y = np.concatenate((y, y2))
        z = np.concatenate((z, z2))

    # Resolution is determined by the average separation between points.
    # Use the smallest separation between longitude and latitudes for square pixels.
    # resolution = min([np.diff(sorted(x)).mean(), np.diff(sorted(y)).mean()]) * 40
    resolution = 6000

    # xu = np.mean(x)
    # xs = np.std(x)
    # yu = np.mean(y)
    # ys = np.std(y)
    # print(xu-xs, xu+xs)
    # print(yu-ys, yu+ys)

    # These values are the xu-xs, xu+xs, yu-ys and yu+ys for the first dataset (2009)
    xmin, xmax = -4167038.04665, 279277.487682
    ymin, ymax = -2685908.36468, 2479713.52965

    # grid_x, grid_y = np.meshgrid(np.arange(xu-xs, xu+xs, resolution),
    #                              np.arange(yu-ys, yu+ys, resolution))
    # grid_x, grid_y = np.meshgrid(np.linspace(xu-xs, xu+xs, resolution),
    #                              np.linspace(yu-ys, yu+ys, resolution))
    grid_x, grid_y = np.meshgrid(np.linspace(xmin, xmax, resolution),
                                 np.linspace(ymin, ymax, resolution))
    cartesian_grid = griddata(np.vstack((x, y)).T, z,
                              (grid_x, grid_y), method="linear", fill_value=-99)
    save_raster_file(cartesian_grid, x.min(), y.min(), resolution, output_filename=args.output_filename)
