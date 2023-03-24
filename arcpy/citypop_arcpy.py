# Extra Credit: Compare CityPop.csv to WorldCities.shp
import sys
try:
    import arcpy
except (RuntimeError, ModuleNotFoundError) as e:
    print("Unable to import arcpy:", e)
    sys.exit(1)
except Exception as e:
    print("Unexpected error attempting to import arcpy:", e)
    sys.exit(1)
print("Imported arcpy successfully")

# Verify sources
citypop = 'CityPop.csv'
worldcities = 'WorldCities.shp'
for src in (citypop, worldcities):
    if not arcpy.Exists(src):
        print('Error: %s not found in script directory' % src)
        sys.exit(1)

# Task 1: Convert CityPop.csv into a GIS layer
arcpy.MakeXYEventLayer_management(citypop, 'longitude', 'latitude', 'CityPop_lyr',
                                  arcpy.SpatialReference(4326)) # or could use 'WorldCities.prj'

# Task 2: find CityPop cities missing from WorldCities
# Read the file only once by pulling all of the fields we need into a list, then derive set
citypop_list = [r for r in arcpy.da.SearchCursor('CityPop_lyr',['label', 'SHAPE@'])]
citypop_set = set(r[0] for r in citypop_list)

# Get a dictionary with the subset of word_cities records that are in CityPop.
worldcities_dict = dict(r for r in arcpy.da.SearchCursor(worldcities,['Name', 'SHAPE@']) if r[0] in citypop_set)
print("Found", len(worldcities_dict), "of", len(citypop_set), "CityPop cities in WorldCities") # 32
missing_cities = citypop_set - set(worldcities_dict) # a dict easily converts to a set of its keys
print("CityPop cities missing from WorldCities:", ', '.join(missing_cities))

# Tasks 3-4: Find the errors and print the large ones
print('\nCities with large errors:')
print('City'.ljust(16), 'Error (km)') # Table header
print('-'*27) # 27 = 16 + len('Error (km)') + 1 for the space in between
max_error = (0, None) # for storing the largest error and the name of that city
for label, geom in citypop_list:
    if label not in worldcities_dict:
        continue # skip the 7 unmatched cities
    world_geom = worldcities_dict[label]
    error = geom.angleAndDistanceTo(world_geom)[1]/1000
    if error > 10:
        print(label.ljust(16), '%10.1f' % error)
        if error > max_error[0]:
            max_error = error, label

# Task 5: Explain the largest error
print("\nThe largest Error is %dkm for %s.\n" % max_error)

print("This is because the lat/lon for Cairo in CityPop is for Cairo, IL (USA), not Cairo, Egypt. "
      "Given the high populations, this appears to be a geocoding error in CityPop.csv.")