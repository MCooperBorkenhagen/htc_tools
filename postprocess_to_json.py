#!/home/groups/lcnl_grp/.local/bin/python3
import sys
import json
import os.path

def parse_to_dict(f):
    d = {}
    for line in f:
        if ':' in line:
            x = line.strip().split(':')
            d[x[0].strip().replace(' ','_')] = x[1].strip().replace(' ','_')

    return d

files = sys.argv[1:]
for filename in files:
    [name,ext] = os.path.splitext(filename)
    jsonname = name + ".json"
    with open(filename, 'r') as f:
        d = parse_to_dict(f)
        jsonstr = json.dumps(d)
        #print(jsonstr)
        with open(jsonname, 'w') as j:
            j.write(jsonstr)
