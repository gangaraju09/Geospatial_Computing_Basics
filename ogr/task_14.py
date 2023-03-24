from osgeo import ogr, gdalconst
import sys
import os

fname1 = 'PowerLine.shp'
fname2 = 'Parcels.shp'
OutputFileName = 'OutputParcels.shp'

# get driver
driver = ogr.GetDriverByName('ESRI Shapefile')

# open file
ds1 = driver.Open(fname1, gdalconst.GA_ReadOnly)
ds2 = driver.Open(fname2, gdalconst.GA_ReadOnly)

# verify the file was opened, exit if not
if ds1 is None:
    print('Failed to open file ', fname1)
    sys.exit(1)
if ds2 is None:
    print('Failed to open file ', fname2)
    sys.exit(1)

# delete output shapefile parts if it already exists
# This removes all parts of the shapefile, including optional files like the prj
result = driver.DeleteDataSource(OutputFileName)
if result == 0:
    print(OutputFileName, "already existed and was removed")

# create data store in the same format as input
outputDS = driver.CreateDataSource(OutputFileName)
if outputDS is None:
    print('Failed to create file ', OutputFileName)
    sys.exit(1)

# get the data layers
layer1 = ds1.GetLayer(0)
layer2 = ds2.GetLayer(0)

# create polygon layer to hold output parcels
srs = layer2.GetSpatialRef()
newLayer = outputDS.CreateLayer('OutputParcels', srs, ogr.wkbPolygon)
if newLayer is None:
    print("couldn't create layer")
    sys.exit(1)

# Optionally copy the source schema to the target
sourceLayerDef = layer2.GetLayerDefn()
for i in range(sourceLayerDef.GetFieldCount()):
    newLayer.CreateField(sourceLayerDef.GetFieldDefn(i))

newLayerDef = newLayer.GetLayerDefn() # every feature in layer will have this

# get the output parcel and add to new layer

# parcel crossed by the power line
lineFeat = layer1.GetFeature(0)
powerLine = lineFeat.GetGeometryRef()
bufferGeom = powerLine.Buffer(250)

# get feature count
featCount = layer2.GetFeatureCount()

for feat in layer2:
    geom = feat.GetGeometryRef()
    # add to new layer if parcel within power line's buffer zone
    if (geom.Within(bufferGeom)):
        #print(featureID) # for debugging
        newLayer.CreateFeature(feat) #add feature to layer

# get count of output features
outCount = newLayer.GetFeatureCount()

ds1 = None
ds2 = None
outputDS = None

print("Added", outCount, "features out of", featCount, "total parcels to", OutputFileName)
