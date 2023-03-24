# This solution is closer to how I would do it.
# It adds some advanced features like dict(zip()) and list comprehension

import sys

# open file; if fails, exit program
fileName = "CityPop.csv"
try:
    csv = open(fileName)
except:
    print("can't open" + fileName)
    sys.exit()

# store each record dictionary in a cities dictionary
cities = {}

# save headers to a list, removing ending newline
headers = csv.readline().strip().split(',')
# pull the years from the headers as a subset of the headers that start with 'yr' using list comprehension
years = [header[2:] for header in headers if header.startswith('yr')]

# save each line to a dictionary, then add to cities dictionary
for line in csv:
    valList = line.strip().split(',')
    city = dict(zip(headers, valList))
    label = city['label'].upper() # convert to uppercase to enable case-insensitve key checking
    cities[label] = city

csv.close()

# query the attribute by city and year
cityStr = input("Please input the city name: ")
cityStr = cityStr.upper() # convert to uppercase to enable case-insensitve key checking
# test whether city exists in cities keys
if cityStr in cities:
    city = cities[cityStr]

    # choose year from a list, exit if input invalid value
    # print year list
    print("Years listed in database:")
    print(' '.join(years), '\n')
    yearStr = input("Please choose one year: ").strip()
    if yearStr in years:
        # add 'yr' to input
        val = (city['label'], yearStr, city['yr' + yearStr])
        fmt = "The population of %s in %s is %s million."
        print(fmt % val)
    else:
        print("can't find population in that year!")

else:
    print("can't find the city!")
