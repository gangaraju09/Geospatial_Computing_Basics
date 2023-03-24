'''
This program finds the distance between two locations based on latitude and
longitude inputs from two different locations.
'''
import math

while True:
    try:
        latitudeA = float(input("enter the latitude of your first location:"))
        longitudeA = float(input("enter the longitude of yoru first location:"))
        latitudeB = float(input("enter the latitude of your second location:"))
        longitudeB = float(input("enter the longitude of yoru second location:"))
        break
    except:
        print("Invalid input. Try again.")

# Convert to radians
latitudeA = math.radians(latitudeA)
longitudeA = math.radians(longitudeA)
latitudeB = math.radians(latitudeB)
longitudeB = math.radians(longitudeB)

#Calculate the distance
distance = math.acos((math.sin(latitudeA)*math.sin(latitudeB))+(math.cos(latitudeA)*math.cos(latitudeB)*math.cos(longitudeA-longitudeB)))
totalDistance = distance * 6300

#Display the distance
print("The distance between your location 1 and location 2, is", totalDistance, "km.")

