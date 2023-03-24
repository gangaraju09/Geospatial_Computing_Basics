import sys
import math

class City(object):
    def __init__(self,name, label, latitude ,longitude , yr1970, yr1975, yr1980, yr1985, yr1990, yr1995, yr2000, yr2005, yr2010):
        self.name = name 
        self.label = label
        self.latitude = lat
        self.longitude = lon
        self.yr1970 = yr1970
        self.yr1975 = yr1975
        self.yr1980 = yr1980
        self.yr1985 = yr1985
        self.yr1990 = yr1990
        self.yr1995 = yr1995
        self.yr2000 = yr2000
        self.yr2005 = yr2005
        self.yr2010 = yr2010 
        
   
    def printDistance(self, othercity):
        try: 
            lat1 = math.radians(float(self.latitude))
            lon1 = math.radians(float(self.longitude))
            lat2 = math.radians(float(othercity.latitude))
            lon2 = math.radians(float(othercity.longitude))
            distance =  round(6300*(math.acos(math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(lon1-lon2))))
            
            fmt = 'The Spherical distance between %s and %s is %d km'
            value = (self.label, othercity.label, distance)
            print(fmt%value)
        except: 
            print('the given cities are not valid, kindly enter correct cities')
                  
    def printPopChange(self,year1,year2): 
        # if (year1 in header) and (year2 in header):
            year1 = float(year1)
            year2 = float(year2)
            population_change = abs(year1-year2)
            print('The population change of %s is %.2f million.'%(self.label, population_change))
        # else:
        #     print('The given years are not valid, kindly enter correct years')


city_list =[]
filename = 'cityPop.csv'
try: 
    cpop= open(filename,'r')
except:
    print('Given Filename not found')
    sys.exit()
header = cpop.readline().strip().split(',')
f_pop = cpop.readlines()[1:]
for i in f_pop:
    a = i.strip().split(',')
    city_name = a[3]
    city_label = a[4]
    lon = float(a[2])
    lat = float(a[1])
    pop_1970 = a[5] ; pop_1975 = a[6] ; pop_1980 = a[7] ; pop_1985 = a[8] ; pop_1990 = a[9] ;
    pop_1995 = a[10] ; pop_2000 = a[11] ; pop_2005 = a[12] ; pop_2010 = a[13]
    
    city_list.append(City(name = city_name, label = city_label, latitude = lat, longitude = lon, yr1970 = pop_1970, yr1975= pop_1975, 
                          yr1980=pop_1980,yr1985=pop_1985, yr1990=pop_1990, yr1995=pop_1995, yr2000=pop_2000, yr2005=pop_2005, yr2010=pop_2010 ))
    
for j in city_list:
    fmt = 'Name of the city: %s at latitude: %s, langitude: %s has population (millions) for years [1970:%s,1975:%s,1980:%s,1985:%s,1990:%s,1995:%s,2000:%s,2005:%s,2010:%s]'
    values = (j.name, j.latitude, j.longitude, j.yr1970, j.yr1975, j.yr1980, j.yr1985, j.yr1990, j.yr1995, j.yr2000, j.yr2005, j.yr2010)
    print(fmt % values + '\n')
City.printDistance(city_list[0],city_list[1])
City.printPopChange(city_list[0],pop_1970,pop_1975)
