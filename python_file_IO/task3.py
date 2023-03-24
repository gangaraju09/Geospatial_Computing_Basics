import sys
import math

"""great circle distance calculator
calculate spherical great circle distance with lat/lon in DD
input:
two coordinates in DD format

output:
spherical great circle distance
"""
def greatCircleDist(lat1, lon1, lat2, lon2, R=6300):
    # convert from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # calculate angular distance
    distance = math.sin(lat1)*math.sin(lat2) + \
               math.cos(lat1)*math.cos(lat2)*math.cos(lon1-lon2)
    distance = math.acos(distance)

    # return spherical distance
    return distance * R


# open file; if fails, exit program
fileName = "CityPop.csv"
try:
    csv = open(fileName,'r')
except:
    print("can't open" + fileName)
    sys.exit()

# store each record in a dictionary and all records in a list
cityList = []
lineList = csv.readlines()

# save headers to a list, removing ending newline
headers = lineList[0].strip().split(',')

# save each line to a dictionary, then append to city list
for line in lineList[1:]:
    valList = line.strip().split(',')
    city = {}
    for i in range(len(headers)):
        city[headers[i]] = valList[i]
    cityList.append(city)

csv.close()

# calculate distance of two cites
cityCoordList = []
for i in range(2):
    print("Please input city name", i+1, ":")
    cityStr = input()
    cityStr = cityStr.upper() # Convert both input and data to make search case-insensitive
    findCity = False
    for city in cityList:
        if city['city'].upper()==cityStr or\
           city['label'].upper()==cityStr:
            findCity = True
            cityCoordList.append((float(city['latitude']), \
                                  float(city['longitude'])))
            break
    # exit if city not found
    if findCity == False:
        print("can't find the city!")
        sys.exit()

distance = greatCircleDist(cityCoordList[0][0],
                           cityCoordList[0][1],
                           cityCoordList[1][0],
                           cityCoordList[1][1])
print("The distance between these two city is %.2fkm." % distance)

# Solution #2
# Store coordinates as a single tuple, unpack into multiple parameters using *

coordTuple = cityCoordList[0] + cityCoordList[1]
distance2 = greatCircleDist(*coordTuple)