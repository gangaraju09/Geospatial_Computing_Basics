# program to find the distance between two location based on their latitudes and logitudes in the given file

# for the advance mathematical calculation, here import math library
import math

# create a dictionary to store values/data which are imported from the external source file
city_dict = {}
# use open function to oen a file data from the sxternal source
cpop= open('CityPop.csv','r')

# write function to read each row of the imported data
f_pop = cpop.readlines()[1:]

# now separate each comma sepate value define each value with some know variable 
for i in f_pop:
    ij = i.strip()
    a = ij.split(',')
    city = a[3]
    lon = float(a[2])
    lat = float(a[1])
    pop_1970 = a[5] ; pop_1975 = a[6] ; pop_1980 = a[7] ; pop_1985 = a[8] ; pop_1990 = a[9] ;
    pop_1995 = a[10] ; pop_2000 = a[11] ; pop_2005 = a[12] ; pop_2010 = a[13] ;
# insert the each deifined data in created dictionary and aslo define key value what it represents in the imported file data   
    city_dict[city]={'city':city, 'lon':lon,'lat':lat,'yr1970':pop_1970, 'yr1975':pop_1975, 
                      'yr1980':pop_1980,'yr1985':pop_1985, 'yr1990':pop_1990, 'yr1995':pop_1995,
                      'yr2000':pop_2000, 'yr2005':pop_2005, 'yr2010':pop_2010}

# write input function to take city inputs from the user
# create while function to prompt user to enter valid data again to avoid exit of program untill user try to exit
while True:  
    city1 = input("enter name of your first city or (Press enter/return to exit):")
    if len(city1)< 1 : 
        break 
    city2 = input("enter name of your second city or (Press enter/return to exit):") 
    if len(city2)< 1 : 
        break 
# check the user enter details are in the database or not, if entered data is correct then do the remaining required calculation to calculate distance
    elif (city1 in city_dict) and (city2 in city_dict):  
# define varaibles to latitude and logitudes of the given city names
        w = city_dict[city1]['lon']
        x = city_dict[city1]['lat']
        y = city_dict[city2]['lon']
        z = city_dict[city2]['lat'] 
# convert the latitudes and longitudes to radians value
        lon1 = math.radians(w)
        lon2 = math.radians(y)
        lat1 = math.radians(x)
        lat2 = math.radians(z)
# calculate the distance value with longitude latitude spherical distance formule
        distance = math.acos((math.sin(lat1)*math.sin(lat2))+(math.cos(lat1)*math.cos(lat2)*math.cos(lon1-lon2)))
        totalDistance = distance * 6300

    #Display the distance
        print("The distance between your location 1 and location 2, is", totalDistance, "km.")
    
    else: 
        print('entered cities are not in our database')
        
cpop.close()
    