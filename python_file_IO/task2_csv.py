# Demonstrates using the csv module

import sys
import csv

# open file; if fails, exit program
fileName = "CityPop.csv"
try:
    f = open(fileName)
except:
    print("can't open" + fileName)
    sys.exit()

# store each record dictionary in a cities dictionary
cities = {}

# Create the csv.DictReader object, an iterable of dictionaries.
# Each dictionary represents one row in the file.
reader = csv.DictReader(f)

# save headers to a list
headers = reader.fieldnames
# pull the years from the headers as a subset of the headers that start with 'yr'
years = []
for header in headers:
    if header.startswith('yr'):
        years.append(header[2:])

# add each city dictionary from DictReader to the cities dictionary
for city in reader:
    label = city['label'].upper() # convert to uppercase to enable case-insensitve key checking
    cities[label] = city

f.close()

# query the attribute by city and year
cityStr = input("Please input the city name: ")
cityStr = cityStr.upper() # convert to uppercase to enable case-insensitve key checking
# test whether city exists in cities keys
if cityStr in cities:
    city = cities[cityStr]

    # choose year from a list, exit if input invalid value
    # print year list
    print("Years listed in database:")
    for year in years:
        print(year)
    print()
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
