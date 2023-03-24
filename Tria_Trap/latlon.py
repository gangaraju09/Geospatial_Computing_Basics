'''
This code takes lat/lon as input and returns a message

'''
while True:
    try:
        lat = float(input("Enter the latitude of the location: "))
        lon = float(input("Enter the longtiude of the location: "))
        break
    except:
        print("Invalid input. Try again!")


if lat == 0 :
    print("That location is on the equator.")
elif 0 < lat <= 90 :
    print("That location is north of the equator.")
elif -90 <= lat < 0 :
    print("That location is south of the equator.")
else:
    print("That location does not have a valid latitude!")
if lon == 0:
    print("That location is on the prime meridian.")
elif  0 < lon <= 180 :
    print("That location is east of the prime meridian.")
elif -180 <= lon < 0 :
    print("That localtion is west of the prime meridian.")
else:
    print("That location does not have a valid longitude!")


