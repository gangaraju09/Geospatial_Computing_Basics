# Program to know the location with known latitude and logitude values
# first we should ask user to enter lat and long values with input function
lat=input('Enter value of latitude:')
lon=input('Enter value of longitude:')
# try is used if the iputs are out of the programme than it dispalayes a message with except function,with input values code fails to execute the except block is entered, instead of crashing
try:
# converting lat and long values into float type
    lat=float(lat)
    lon=float(lon)
# latitude are sucessfuly converted into float then we write if function to show location between different latitude values
    if lat=='0': 
        print('That Location is on the Equator') 
    elif 0<lat<=90 :
        print('That Location is North of the Equator')
    elif -90<=lat<0 :
        print('That Location is south of the equator') 
# if given values are not in range than we dispaly the value are invalid with else function 
    else : 
        print('The location does not have a valid latitude!')
# longitude are sucessfuly converted into float then we write if function to show location between different longitude values 
    if lon==0 :
        print('The location is on the prime meridean')
    elif 0<lon<=180:
        print('The Location is East of prime meridian')
    elif -180<=lon<0:
        print('The Location is West of the prime meridian')
# if given values are not in range than we dispaly the value are invalid with else function 
    else :
        print('The location does not have a valid Longitude')
    print ('The latitude and logitude is at',lat, 'and',lon)
#  if entered values are not number then except is used to display to enter correct values to run the program, instead of crashing
except:
    print('Please Enter a correct number, dont enter alphabets \n Restart the program again')
    
