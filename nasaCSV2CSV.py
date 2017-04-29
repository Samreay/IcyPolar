#!/usr/bin/env python

import os
import sys
import re
import numpy as np

header_length = 10

for x in sys.argv[1:]:
    pre, ext = os.path.splitext(x)
    # Strip the leading slashes
    pre = re.search(r"/(.*)", pre).group(1)
    output_file = pre + "_modified" + ext
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
        np.savetxt(output_file, np.vstack((lng, lat, elev)).T, delimiter=',', fmt="%.5f")
        print("Saved: %s" % output_file)
