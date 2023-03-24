# Program to find  population of a user given city and year

#create a dictionary to store values from an external file data
city_dict = {}
# writes a function open, to open a file from the external file source
cpop= open(r'A:\UW-Madison\GIS Spring 2022\G378\CityPop.csv','r')

# write a function to read each row of a data
f_pop = cpop.readlines()[1:]

# separate a comma separated data and define each data with some known variable
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
    
# create a while function to prompt user to enter correct values if user enters wrong value
while True: 
    cname = input('enter city name: or press Enter/Return to exit ::')
    year = str(input('enter year: or press Enter/Return to exit :: '))
# create a function to exit the user from the loop
    if len(cname)< 1 : 
        break  
    elif cname in city_dict  and ('yr'+year) in city_dict[cname]:   
        print('the population of',cname,'in',year, 'is', city_dict[cname]['yr'+year],'millions'  )
    else: 
        print('entered city nmae or year is invalid, please try again.')
        
cpop.close()