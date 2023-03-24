# Program to calculate population change between two years for all cities and creat a new data into new csv file from the know dataset

# create a dictionary to store require data 
city_dict = {}
# with open functiion, open file to load the reqired data
cpop= open('CityPop.csv','r')

# now read the lines of the rows in the data
f_pop = cpop.readlines()[1:]

# to define each data with a key, separate the each comma separated value
for i in f_pop:
    ij = i.strip()
    a = ij.split(',')
# after separating each data, specify the each data with a key 
    Id = a[0]
    city = a[3]
    lon = float(a[2])
    lat = float(a[1])
    pop_1970 = a[5] ; pop_1975 = a[6] ; pop_1980 = a[7] ; pop_1985 = a[8] ; pop_1990 = a[9] ;
    pop_1995 = a[10] ; pop_2000 = a[11] ; pop_2005 = a[12] ; pop_2010 = a[13] ;
# now insert the each data into a dictionary  
    city_dict[city]={'id': Id,'city':city, 'lon':lon,'lat':lat,'yr1970':pop_1970, 'yr1975':pop_1975, 
                     'yr1980':pop_1980,'yr1985':pop_1985, 'yr1990':pop_1990, 'yr1995':pop_1995,
                     'yr2000':pop_2000, 'yr2005':pop_2005, 'yr2010':pop_2010}
# while loop helps to re-prompt the user to enter values again if he enters wrong values instead of direct exit from the program
while True:  
        in_yr = input('Enter initial year or (Press Enter/return to Exit):') 
#write a break function fot the user to exit from the program
        if len(in_yr)<1 : break 
        elif ('yr'+in_yr) not in city_dict[city]: 
            print('Entered initial year is not available')
            
        fl_yr = input('Enter final year or (Press Enter/return to Exit):')
        if len(fl_yr)<1 : break
        
        elif ('yr'+fl_yr) not in city_dict[city]:
            print('Entered final year is wrong')
                 
        elif ('yr'+in_yr in city_dict[city]) and ('yr'+fl_yr in city_dict[city]):
# to create a new file, here use 'wt' or 'w+t' after giving new file name with open fumction
                 c_pop= open('CityPopchg .csv','w+t')
# create a first row to know what values stored in each coloumn
                 header = 'id, city, population_change\n'
                 c_pop.write(header)
                 for k in city_dict:
# wite a formula to show the population change between the user year inputs
                     pop_change=str((float(city_dict[k]['yr'+in_yr])-float(city_dict[k]['yr'+fl_yr])))
# now assign required id's, city names, population change to first row
                     input_rows = city_dict[k]['id'] + ',' + k + ',' + pop_change +'\n'
# use write() function to write the assigned values into the created file rows
                     c_pop.write(input_rows)
                 print('CityPopchg.csv is created for', in_yr, 'and',fl_yr)
#use close() function to close the file
                 c_pop.close()     

