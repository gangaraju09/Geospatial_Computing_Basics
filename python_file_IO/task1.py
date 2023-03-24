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
    print(city)

csv.close()
