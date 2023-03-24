# program to claculate length of powerlines in miles from the given shapefiles

# to get and read shapefiles classes in python, import ogr library 
from osgeo import ogr
from osgeo import gdalconst
import sys
import math

filename = r'\GISGDAL\PowerLine\PowerLine.shp'

#to define a specific file type, assign a driver as esri shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')
datasource = driver.Open(filename, gdalconst.GA_ReadOnly)

#check the given data source was found and opened or not
if datasource is None:
    print('System could not able to find & open the given filename')
    sys.exit(1)

# to get the first layer data
layer = datasource.GetLayer(0)
Ltype = layer.GetGeomType()
Lextent = layer.GetExtent()
Lname = layer.GetName()

# convert the integer layer type into text type
Ltypes = ogr.GeometryTypeToName(Ltype)
print(Lname, ' consist extent', Lextent, 'is a', Ltypes)

# get non spatial layer info such as field counts, feature count
featureDefn = layer.GetLayerDefn()
fieldCount = featureDefn.GetFieldCount()
featureCount = layer.GetFeatureCount()
print('Number of field count are', fieldCount,'and Number of feature count are',featureCount)

# now, calculate length of powerline and use conversion to get values in miles as file will be in US foot values
feature  = layer.GetFeature(0)
LineGeometry = feature.GetGeometryRef()

length = LineGeometry.Length()
print('Length of powerline in us foot is',length)

length = length*0.000189394
print('After conversion length of powerline in miles is',length)


#now claculate the length using getpoint method and compare the results.

line  = feature.GetGeometryRef()

pointsCount = line.GetPointCount()
print('Number of points on a line available are',pointsCount)

gross_length = 0

for i in range(pointsCount-1):
    point1 = line.GetPoint(i)
    point2 = line.GetPoint(i+1)
    x1     = point1[0]
    x2     = point2[0]
    y1     = point1[1]
    y2     = point2[1]
    
    gross_length= gross_length + math.sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))

gross_length = gross_length*0.000189394
print('Length of powerline with GetPoint method is ', gross_length)

dataSource = None