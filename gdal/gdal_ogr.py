import numpy as N
from osgeo import gdal
import sys

# open NIR band raster and read as array
# open Red band raster and read as array
# do math
# create new tif file with geotransform of input datasets
# write new raster to file

def calculateNDVI(nir, red):
    #read raster bands into arrays
    nirArray = nir.ReadAsArray()
    redArray = red.ReadAsArray()

    #convert to float
    arr1 = (1.*nirArray - 1.*redArray)
    arr2 = (1.*nirArray + 1.*redArray)
    return arr1/arr2

outFmt = 'GTiff'
outDriver = gdal.GetDriverByName(outFmt)

ds_nir = gdal.Open('landsat/L71026029_02920000609_B40_CLIP.TIF')
ds_red = gdal.Open('landsat/L71026029_02920000609_B30_CLIP.TIF')
if ds_nir is None or ds_red is None:
    print("Error, unable to open one of the files.")
    sys.exit()

ndviDriver = ds_nir.GetDriver()
ndviCols = ds_nir.RasterXSize
ndviRows = ds_nir.RasterYSize

ndviData = calculateNDVI(ds_nir, ds_red)

ndviGeoTransform = ds_nir.GetGeoTransform()
ndviProjection = ds_nir.GetProjection()

# create new tiff
ndvi = ndviDriver.Create('NDVI.TIF', ndviCols, ndviRows, 1, gdal.GDT_Float32)
# set geotransform & projection
ndvi.SetGeoTransform(ndviGeoTransform)
ndvi.SetProjection(ndviProjection)
# write band
band = ndvi.GetRasterBand(1)
band.SetColorInterpretation(gdal.GCI_GrayIndex)
band.WriteArray(ndviData)
band.SetNoDataValue(float(1e-7)) # set NoData to 0 doesn't work

ndvi = None
ds_nir = None
ds_red = None