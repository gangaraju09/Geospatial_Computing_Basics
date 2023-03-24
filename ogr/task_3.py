from osgeo import ogr, gdalconst
import sys

fname1 = 'PowerLine.shp'
fname2 = 'Parcels.shp'

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

# get the first data layer
layer1 = ds1.GetLayer(0)
layer2 = ds2.GetLayer(0)

# get powerline geometry
lineFeat = layer1.GetFeature(0)
powerLine = lineFeat.GetGeometryRef()

# get feature count
featCount = layer2.GetFeatureCount()

for feat in layer2:
    geom = feat.GetGeometryRef()
    # print info if parcel intersects power line
    if (geom.Intersects(powerLine)):
        name = feat.GetField('SITUSADDR')
        area = feat.GetField('AREA')
        print('name: ', name, "; area: ", area)

ds1 = None
ds2 = None
