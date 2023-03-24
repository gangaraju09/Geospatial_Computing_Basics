# Programe to calculate Distance between two locations using location latitude and longitude
# formula have trignometry fuctions so we have to import math library

import math
loopcount = 0
while loopcount < 3:
    loopcount+=1
    nam1=input('Enter name of 1st location:')
    nam2=input('Enter name of 2nd location:')
    
    lat1= input('Enter 1st location latitude values:')
    dir11=input('Enter direction of 1st latitude (N or S in caps):')
    lon1=input('Enter 1st location longitude values:')
    dir12=input('enter direction of 1st logitude (E or W in caps):')
    
    lat2=input('Enter 2nd Location latitude values:')
    dir21=input('Enter direction of 2nd latitude (N or S in caps):')
    lon2=input('Enter 2nd location logitude value:')
    dir22=input('Enter direction of 2nd longitude (E or W in caps):')
    try: 
        lat1=float(lat1)
        if dir11 == 'N': 
                lat1=1*lat1
        elif dir11 == 'S': 
            lat1=-1*lat1
            
        lat2=float(lat2)
        if dir21 == 'N': 
            lat2=1*lat2
        elif dir21 == 'S':
            lat2=-1*lat2
            
        lon1=float(lon1)
        if dir12 == 'E': 
            lon1=lon1
        elif dir12 == 'W':
            lon1=-1*lon1 
            
        lon2=float(lon2)
        if dir22 == 'E':
            lon2=lon2
        elif dir22== 'W': 
            lon2=-1*lon2
        
        a1 = math.radians(lat1)
        a2 = math.radians(lat2)
        b1 = math.radians(lon1)
        b2 = math.radians(lon2)
        c1 = abs(b1-b2)
        d = math.acos((math.sin(a1)*math.sin(a2))+(math.cos(a1)*math.cos(a2)*math.cos(c1)))
        print('the distance between',nam1,'and',nam2,'is',round(d*6300),'kms')
        break
    except:
        print('Kindly enter correct numeric values, avoid alphabets and alphanumeric values')