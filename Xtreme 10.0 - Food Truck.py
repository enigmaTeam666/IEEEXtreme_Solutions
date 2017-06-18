# Enter your code here. Read input from STDIN. Print output to STDOUT

from datetime import datetime
from math import radians, cos, sin, asin, sqrt
import sys

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6378.137 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

    
lat, lon = map(float, raw_input().split(","))
r = float(raw_input())
raw_input()
d = {}
for line in sys.stdin:
    item  = line.strip().split(",")
    try:
        dat = datetime.strptime(item[0], "%m/%d/%Y %H:%M")
        h = haversine(lon, lat, float(item[2]), float(item[1]))
        if item[3] in d:
            if dat > d[item[3]][0]:
                d[item[3]] = [dat, h]
        else:
            d[item[3]] = [dat, h]
    except:
        pass
        
    
#print d
resul = []
for key in d:
    if  d[key][1]<=r:
        resul.append((key, d[key][1]))
        
res = sorted(resul, key=lambda x:x[0])
print ",".join([i[0] for i in res])