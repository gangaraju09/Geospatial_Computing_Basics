# program to find each field name and its types for the given shapefile

# to get and read shapefiles classes in python, import ogr library 
from osgeo import ogr
from osgeo import gdalconst
import sys

filename = r'\GISGDAL\Parcels\Parcels.shp'

#to define a specific file type to assign a driver as esri shapefile
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
print(Lname, ' consists an extent', Lextent, 'is a', Ltypes)

# get non spatial layer info such as field counts, feature count
featureDefn = layer.GetLayerDefn()
fieldCount = featureDefn.GetFieldCount()
featureCount = layer.GetFeatureCount()
print('Number of field count are', fieldCount,'and Number of feature count are',featureCount)

# to get each field name with its type of data
for i in range(fieldCount):
    fieldDef   = featureDefn.GetFieldDefn(i)
    fieldname  = fieldDef.GetNameRef()
    fieldtype  = fieldDef.GetType()
    fieldtypes = fieldDef.GetFieldTypeName(fieldtype)
    
    print('Fieldname is', fieldname,'and its type is',fieldtypes)
    

dataSource = None