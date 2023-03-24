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

# caculate population change and write to file
print("Years listed in database:")
for year in range(1970,2015,5):
    print(year)
print()
yearStr1 = input("Please input the first year:")
yearStr2 = input("Please input the second year:")

if 'yr'+yearStr1 in headers and 'yr'+yearStr2 in headers:
    # open file for output
    outputFileName = "CityPopChg.csv"
    try:
        outputFile = open(outputFileName, 'wt')
    except:
        print("can't write to file" + outputFileName)

    # reverse if first year > second year
    if float(yearStr1) > float(yearStr2):
        temp = yearStr1
        yearStr1 = yearStr2
        yearStr2 = temp
    # output header
    outputFile.write('id,city,population_change\n')
    # caculate for each city and output
    for city in cityList:
        popchg = float(city['yr'+yearStr2]) - float(city['yr'+yearStr1])
        outputFile.write(city['id'] + ',' + city['city'] + ',' +\
                         str(popchg) + '\n')
else:
    print("Invalid input.")
    sys.exit()

print("CityPopChg.csv succeffully created!")
outputFile.close()
