# program to construct a shapefile which contains 250 feet buffer on each parcels

from osgeo import ogr
from osgeo import gdalconst
import os
import sys

powerline_file = r'\GISGDAL\PowerLine\PowerLine.shp'
parcels_file   = r'\GISGDAL\Parcels\Parcels.shp'

#to define a specific file type assign a driver as esri shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')

# create data source for each shapefile and check whether is opened or not

powerlines_source = driver.Open(powerline_file, gdalconst.GA_ReadOnly)
if powerlines_source is None:
    sys.exit('System could not able to find & open the given powerline file', powerlines_source)

parcels_source = driver.Open(parcels_file, gdalconst.GA_ReadOnly)
if parcels_source is None:
    sys.exit('System could not able to find & open the given parcels file', parcels_source)
    
powerlines_layer = powerlines_source.GetLayer(0)
powerlines_feature = powerlines_layer.GetNextFeature()
powerlines_geom = powerlines_feature.GetGeometryRef()

parcels_layer = parcels_source.GetLayer(0)
parcelS_featureCount = parcels_layer.GetFeatureCount()

output = 'Buffer_250.shp'

# to avoid the program crash due to existed file, use try except concept
if os.path.exists(output):
  try:
    os.remove(output)
  except:
      print('Given file is already opened in the system, kindly close the file and run again ')

#Assign required buffer value
buffer_area = 250
      
powerlines_Buffer = powerlines_geom.Buffer(buffer_area)
print('Buffer is created successfuly')

try: 
    output_source = driver.CreateDataSource(output)   
except:
    print('Unable to create the outputfile>', output)
    
# define spatial reference system from the existed srs in the given shapefiles
SRS = parcels_layer.GetSpatialRef()    
newLayer = output_source.CreateLayer('Buffer_250',SRS,ogr.wkbPolygon)

#  check whether files is in system directory or not
if newLayer is None:
    print('Buffer_250.shp is not in a directory')
    
newLayerDefn = newLayer.GetLayerDefn()

print('Parcels within 250 feet are selected and shapefile is created')

# with the help of  while loop generate new features with ids
featureID = 0
parcels_feature = parcels_layer.GetNextFeature()
while parcels_feature:
    parcels_geom = parcels_feature.GetGeometryRef()
    parcels_Buffers = parcels_geom.Within(powerlines_Buffer)
    
    if parcels_Buffers:
        try:
            print(parcels_feature.GetField('SITUSADDR'), ": ", parcels_feature.GetField('AREA'))
            newFeature = ogr.Feature(newLayerDefn)
            newFeature.SetGeometry(parcels_geom)
            newFeature.SetFID(featureID)
            newLayer.CreateFeature(newFeature)
            
        except:
            print('system unable to print Buffer_250.shp file')
    else:
        pass
    parcels_feature = parcels_layer.GetNextFeature()  
    featureID += 1

powerlines_source = parcels_source = output_source = None