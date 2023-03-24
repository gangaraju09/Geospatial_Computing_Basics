import sys
import math

# city class
class City:
    def __init__(self, name='n/a', label='n/a', lat=-999, lon=-999,\
                 population = {}):
        self.name = name
        self.label = label
        self.lat = lat
        self.lon = lon
        self.pop = population

    # print city attributes
    def printCity(self):
        print('city name:', self.name)
        print('city label:', self.label)
        print('city latitude:', self.lat)
        print('city longitude:', self.lon)
        print('city population:', self.pop)

    def printDistance(self, othercity):
        latA = math.radians(self.lat)
        lonA = math.radians(self.lon)
        latB = math.radians(othercity.lat)
        lonB = math.radians(othercity.lon)

        #Calculate the distance
        distance = math.acos((math.sin(latA)*math.sin(latB)) + (math.cos(latA)*math.cos(latB)*math.cos(lonA-lonB)))
        totalDistance = round(distance * 6300)

        #Display the distance
        print("The distance between location 1 and location 2 is", totalDistance, "km.")

    # print population change
    def printPopChange(self, year1, year2):
        if year1 in self.pop and year2 in self.pop:
            # reverse if first year > second year
            if float(year1) > float(year2):
                temp = year1
                year1 = year2
                year2 = temp

            popchg = self.pop[year2] - self.pop[year1]
            print('population change between', year1, 'and', year2, ':', popchg, "million")
        else:
            print("Invalid input.")



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

for i in range(1,len(lineList)):
    valList = lineList[i].strip().split(',')
    # create the dict to store population
    popDict = {}
    for i in range(5, len(headers)):
        popDict[headers[i][2:]] = float(valList[i])
    # create city instance
    city = City(valList[3], valList[4], float(valList[1]), float(valList[2]), popDict)
    # add to list
    Cities.append(city)

    city.printCity()

csv.close()

city1 = Cities[0]
city2 = Cities[1]
city1.printDistance(city2)
city1.printPopChange("1970","1975")
