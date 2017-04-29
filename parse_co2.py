#!/usr/bin/env python

import csv
import json
import datetime

header_length = 73

input_file = "data/co2_mm_mlo.txt"
output_file = "data/co2.json"
json_file = open(output_file, 'w')

with open(input_file, 'r') as f:
    data = csv.reader(f, delimiter=' ', skipinitialspace=True)
    output_data = {}

    for i, row in enumerate(data):
        if i < header_length:
            continue

        output_data[row[2]] = row[5]

json.dump(output_data, json_file)
json_file.write('\n')
json_file.close()
