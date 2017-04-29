import numpy as np
import json

data = np.genfromtxt("vel.csv", dtype=None, names=True, delimiter=',')

cols = ["lat", "long", "vx", "vy", "elevation"]

output = {col: data[col].tolist() for col in cols}

filename = "../static/json/greenland.json"
with open(filename, 'w') as f:
    f.write(json.dumps(output))