# The program to convert Degree decimal to degree minutes seconds and vice versa based on given input value

# to perform mathematical functions we import math library
import math

#### Task : 1 : to convert dms values into dd values

# we used def function create object to assaign values
def dms_dd(degrees,minutes,seconds): 
    
# to covert dd values into dms value, we use formula as degree+(minutes/60)+(seconds/3600)
    dd = float(abs(degrees))+float(minutes/60)+float(seconds/3600)
    
# if the input value is less than zero the output value should be in negative form, we use if else condition
    if degrees<0 : 
        
# if if conditon is successfuly executed then it will return the value or it will processed to else condition
        return print('the given input values are in dms form\n its DD form is',-dd)

    else :
        print('the given input values are in dms form\n its DD form is',dd)
        
### Task 2 : to convert dd values into dms
        
def dd_dms(decimal_degree):
    
#to convert the given input decimal_degree value into float type, float() is used
        decimal_degree = float(decimal_degree)
        
#to split the decimal value into 1. value before decimal and 2. value after decimal ;as tuple, math.modf() function is used 
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
        return print('the given input values are in DD form\n its DMS form is',dms)
    
### Task 3 : to convert between DD and DMS based on intput form of value
        
#  to give input value by the end user, we put input function
a = input('enter the latitude/longitude values:')

# to know the given value is in dd form or dms form, if the input value have coma(,) separated value then it is DMS form or else it is a DD form
# we use count function to know ',' values in given input 
b = a.count(',')

#  to enter 3 values with ',' ; we use 2 no's of ',' to separate three values ; there fore we check whether there is 2 ',' are there or not with if condition and ==
if b == 2:
    
#if, if condition is satisfied then we have to split the given value into tuple formate to calculate dms to dd value or it jumps to else condition
    c = a.split(',')
    a = tuple(c)
    dms_dd(float(a[0]),float(a[1]),float(a[2]))
    
# if, if conditons is not satidfies than it should calculate else condition to calculate dd to dms value
else:
    dd_dms(float(a))
    
