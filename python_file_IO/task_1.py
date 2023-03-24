#Program to read a required file and to store file data in a container

#create a empty dictionary with some name related to file name to store values later
city_dict = {}

#create a variable to open a file with open function
cpop= open('CityPop.csv','r')

# write the fuunction to read each row of the data
f_pop = cpop.readlines()[1:]

# split the coma separated with a variable and define each value for what that each value mean
for i in f_pop:
    ij = i.strip()
    a = ij.split(',')
    city = a[3]
    lon = float(a[2])
    lat = float(a[1])
    pop_1970 = a[5] ; pop_1975 = a[6] ; pop_1980 = a[7] ; pop_1985 = a[8] ; pop_1990 = a[9] ;
    pop_1995 = a[10] ; pop_2000 = a[11] ; pop_2005 = a[12] ; pop_2010 = a[13] ;
    
# Now insert, separated and defined values in created dictionary
   
    city_dict[city]={'city':city, 'lon':lon,'lat':lat,'yr1970':pop_1970, 'yr1975':pop_1975, 
                     'yr1980':pop_1980,'yr1985':pop_1985, 'yr1990':pop_1990, 'yr1995':pop_1995,
                     'yr2000':pop_2000, 'yr2005':pop_2005, 'yr2010':pop_2010}
    
    print(city_dict)

cpop.close()