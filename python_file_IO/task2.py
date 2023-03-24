# This is a basic solution that sticks to concepts from the modules

import sys

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

# query the attribute by city and year
cityStr = input("Please input the city name: ")
cityStr = cityStr.upper()
# test whether city exists with 'city' and label
findCity = False
for city in cityList:
    if city['city'].upper()==cityStr or\
    city['label'].upper()==cityStr:
        findCity = True
        # choose year from a list, exit if input invalid value
        # print year list
        print("Years listed in database:")
        for year in range(1970,2015,5):
            print(year)
        print()
        yearStr = input("Please choose one year: ")
        # add 'yr' to input
        yearStr = 'yr' + yearStr.strip()
        if yearStr in headers:
            val = (city['label'], yearStr[-4:], city[yearStr])
            fmt = "The population of %s in %s is %s million."
            print(fmt % val)
        else:
            print("can't find population in that year!")
        break

if findCity == False:
    print("can't find the city!")
