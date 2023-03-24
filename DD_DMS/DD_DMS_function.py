# The program to convert decimal degrees(DD) to Degree minutes seconds(DMS)
#for the mathematical functions coding we import math library

import math

#def function is used to create an object to assaign a value
def dd_dms(decimal_degree):
    
#to convert the given decima_degree value into float type, float() is used
        decimal_degree = float(decimal_degree)

#to split the decimal value into 1. value before decimal and 2. value after decimal ; math.modf() function is used 
        decimal_degree = math.modf(decimal_degree)
        
# after spliting the decimal value into tuple  with math.modf, the out values are 1.before decimal is considered as [1] and 2. after decimal is [0]
        degree = decimal_degree[1]
        
# minutes value shouldn't be negative, give abs() to avoid negative value
        minute = abs(decimal_degree[0])*60 
        
# we get mintues value in a decimal form, now we again use math.modf() to split into tuple
        mins = math.modf(minute)
        minute = mins[1]
        seconds = mins[0]*60
        secs = math.modf(seconds)
        seconds = secs[1]
        dms = (int(degree),int(minute),int(seconds))
        tuple(dms)
        return print('The value in DMS form is', dms)
        
dd_dms(-79.982)