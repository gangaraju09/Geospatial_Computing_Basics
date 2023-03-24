from osgeo import ogr, gdalconst
import sys

filename = 'Parcels.shp'

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

# get feature defination
featDefn = layer.GetLayerDefn()

# get number of fields
fieldCount = featDefn.GetFieldCount()

print(fieldCount, "fields:")

# print info of every field
for i in range(fieldCount):
    fieldDef   = featDefn.GetFieldDefn(i)
    fname      = fieldDef.GetNameRef()
    fwidth     = fieldDef.GetWidth()
    fprecision = fieldDef.GetPrecision()
    ftype      = fieldDef.GetType()

    #convert integer ftype to text equiv
    ftypeS = fieldDef.GetFieldTypeName(ftype)

    values = (fname,ftypeS,fwidth,fprecision)
    fmt  = '%s: %s (%d.%d)'
    print(fmt % values)

ds = None