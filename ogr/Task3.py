# program to find each address and its area of the given shapefiles

from osgeo import ogr
from osgeo import gdalconst
import sys

powerline_file = r'\GISGDAL\PowerLine\PowerLine.shp'
parcels_file   = r'\GISGDAL\Parcels\Parcels.shp'

#to define a specific file type assign a driver as esri shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')
powerline_datasource = driver.Open(powerline_file, gdalconst.GA_ReadOnly)

#check the given data source was found and opened or not
if powerline_datasource is None:
    print('System could not able to find & open the given powerline filename')
    sys.exit(1)
    
powerline_layer = powerline_datasource.GetLayer(0)
powerline_feature = powerline_layer.GetFeature(0)
powerline_geom = powerline_feature.GetGeometryRef()

parcels_datasource = driver.Open(parcels_file, gdalconst.GA_ReadOnly)
if parcels_datasource is None:
    print('System could not able to find & open the given parcels filename')
    sys.exit(1)
    
parcels_layer = parcels_datasource.GetLayer(0)
parcels_featureDefn = parcels_layer.GetLayerDefn()
parcels_featurecount = parcels_layer.GetFeatureCount()

# to get address and its area
for i in range(parcels_featurecount):
    parcels_feature = parcels_layer.GetFeature(i)
    parcels_geom = parcels_feature.GetGeometryRef()
    if parcels_geom.Crosses(powerline_geom):
        address = parcels_feature.GetField('SITUSADDR')
        area = parcels_geom.GetArea()
        print('Area of',address,' is :',area,'sq.ft')
        
powerline_datasource.Destroy()
parcels_datasource.Destroy()