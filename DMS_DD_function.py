# The programm to convert degree minute second(DMS) to Degree decimal(DD)

# we used def function create object to assaign values
def dms(degrees,minutes,seconds): 

# to covert dd values into dms value, we use formula as degree+(minutes/60)+(seconds/3600)
    dd = float(abs(degrees))+float(minutes/60)+float(seconds/3600)
    
# if the input value is less than zero the output value should be in negative form, we use if else condition
    if degrees<0 : 

# if if conditon is successfuly executed then it will return the value or it will processed to else condition
        return print(-dd)
    else :
        print(dd)
        
dms(-40, 26, 46)