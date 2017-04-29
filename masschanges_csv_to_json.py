#!/usr/bin/env python

import csv
import json
import datetime as dt


def decimal_date_to_iso(dd):
    if isinstance(dd, str):
        dd = float(dd)

    year = int(dd)
    days = dt.timedelta((dd - year) * 365.25)
    return (days + dt.datetime(year, 1, 1)).isoformat() + 'Z'


header_length = 14

input_file = "data/ANT_mass_changes_Watkins053116.csv"
output_file = "data/mass_change.json"
json_file = open(output_file, 'w')

with open(input_file, 'r') as f:
    data = csv.reader(f, delimiter=',', skipinitialspace=True)
    output_data = {}

    for i, row in enumerate(data):
        if i < header_length:
            continue

        date = decimal_date_to_iso(row[0])
        trend_value = row[3]
        output_data[date] = trend_value

json.dump(output_data, json_file)
json_file.write('\n')
json_file.close()
