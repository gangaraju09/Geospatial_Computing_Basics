"""This Solution adds a few advanced Python class features"""

import sys
import math

# city class
class City:
    def __init__(self, lat=-999, lon=-999, name='n/a', label='n/a',
                 yr1970=0,yr1975=0,yr1980=0,yr1985=0,yr1990=0,yr1995=0,yr2000=0,yr2005=0,yr2010=0):
        self.lat = float(lat)
        self.lon = float(lon)
        self.name = name
        self.label = label
        self.yr1970 = float(yr1970)
        self.yr1975 = float(yr1975)
        self.yr1980 = float(yr1980)
        self.yr1985 = float(yr1985)
        self.yr1990 = float(yr1990)
        self.yr1995 = float(yr1995)
        self.yr2000 = float(yr2000)
        self.yr2005 = float(yr2005)
        self.yr2010 = float(yr2010)

    # Built in method that is evaluated whenever either str() or repr() is called
    #   - str(object) is most commonly called using print, e.g. print(city)
    #   - repr(object) is called when typing an object into the interpreter directly,
    #     or if a list or container of the objects is printed e.g. print(Cities)
    # Since no __str__ is defined, __repr__ defines behavior for both str() and repr()
    def __repr__(self):
        return "\n" + self.label + "\n" + "-"*len(self.label) + "\n" + str(vars(self))

    # Override default sort functionality for collections of the class
    def __lt__(self, othercity):
        return self.label < othercity.label

    # Python 2 way to customize sorting
##    def __cmp__(self, othercity):
##        if self.label < othercity.label:
##            return -1
##        elif self.label > othercity.label:
##            return 1
##        else:
##            return 0

    def printDistance(self, othercity):
        latA = math.radians(self.lat)
        lonA = math.radians(self.lon)
        latB = math.radians(othercity.lat)
        lonB = math.radians(othercity.lon)

        # Calculate the distance
        distance = math.acos((math.sin(latA)*math.sin(latB)) + (math.cos(latA)*math.cos(latB)*math.cos(lonA-lonB)))
        totalDistance = round(distance * 6300)

        # Display the distance (since we're rounding, use %d to avoid showing meaningless decimal)
        print("The distance between %s and %s is %d km." % (self.label, othercity.label, totalDistance))

    # print population change
    def printPopChange(self, year1, year2):
        try:
            # reverse if first year > second year
            if int(year1) > int(year2):
                temp = year1
                year1 = year2
                year2 = temp

            # Use getattr() to access each year attribute from self
            popchg = getattr(self, "yr" + str(year2)) - getattr(self, "yr" + str(year1))
            print('population change between %s and %s: %s million' % (year1, year2, popchg))
        except Exception as error:
            print("Invalid input:", year1, year2)
            print(error)

# open file; if fails, exit program
fileName = "CityPop.csv"
try:
    csv = open(fileName,'r')
except:
    print("can't open" + fileName)
    sys.exit()

# store all cities in a list
Cities = []


lineList = csv.readlines()
# save headers to a list
headers = lineList[0].strip().split(',')

for line in lineList[1:]:
    valList = line.strip().split(',')
    # create city instance
    # pass list values to multiple parameters using * (order matters!)
    city = City(*valList[1:])
    # add to list
    Cities.append(city)

    print(city) # Calls str() for each city

csv.close()

Cities.sort() # Sorts using custom __lt__ method built into the class
print(Cities) # Calls repr() of each City, since the objects aren't printed directly, but as a list

city1 = Cities[0]
city2 = Cities[1]

print("\nTesting Methods:")
city1.printDistance(city2)
city1.printPopChange(1970,1975)
