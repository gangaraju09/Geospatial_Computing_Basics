from osgeo import ogr, gdalconst
import sys

filename = 'PowerLine.shp'

# get driver
driver = ogr.GetDriverByName('ESRI Shapefile')

# open file
ds = driver.Open(filename, gdalconst.GA_ReadOnly)

# verify the file was opened, exit if not
if ds is None:
    print('Failed to open file')
    sys.exit(1)

# get the first data layer
layer = ds.GetLayer(0)

# get the first(and only) feature
feature = layer.GetNextFeature()

# get the line
line = feature.GetGeometryRef()

# get number of points on line
nPts = line.GetPointCount()

# calculate the length by adding the distance between two points
length = 0
x1 = line.GetX(0)
y1 = line.GetY(0)
for i in range(1,nPts):
    x2 = line.GetX(i)
    y2 = line.GetY(i)
    length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    x1 = x2
    y1 = y2

# convert length from feet to mile
length /= 5280

print("calculated length: ", length)

# compare to length() method
print("length() method:", line.Length()/5280)

ds = None