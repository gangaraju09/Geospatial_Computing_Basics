import arcpy
import os
# Set the workspace to be the location of the script
arcpy.env.workspace = os.path.dirname(__file__)

powerline = 'PowerLine.shp'
parcels = 'Parcels.shp'
output_fc = 'OutputParcels.shp'

# Task 1
print("TASK 1: PowerLine length (in miles)")

FT_PER_MILE = 5280
# Since we know there is only a single feature, use next() to extract this feature
# and then [0] to extract the length, the only attribute included in the cursor
line_length_ft = next(arcpy.da.SearchCursor(powerline,'SHAPE@LENGTH'))[0]
print("\tUsing SHAPE@LENGTH   = %.2f" % (line_length_ft/FT_PER_MILE))

# Alternative using the arcpy.Geometry object.
# This has the advantage of not requiring any knowledge of the coordinate system,
# as we can specify our final desired output unit.
# However, for a large number of features, this would be slower since it accesses the full geometry object.
geom = next(arcpy.da.SearchCursor(powerline,'SHAPE@'))[0]
line_length_miles = geom.getLength(units='MILES')
print("\tUsing geom.getLength = %.2f" % line_length_miles)

# Manual calculation Extra Credit: calculate the length by adding the distance between two points
points = geom.getPart(0)
length = 0
x1 = points[0].X
y1 = points[0].Y
for i in range(1,len(points)):
    x2 = points[i].X
    y2 = points[i].Y
    length += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    x1 = x2
    y1 = y2

# convert length from feet to miles
length /= FT_PER_MILE
print("\tCalculated length    = %.2f" % length)

# Task 2
print("\nTASK 2: Parcels fields")

def print_aligned_columns(col_headers, data):
    # Function to print a data table with aligned columns
    max_col_lengths = [len(header) for header in col_headers]
    col_types = [type(val) for val in data[0]]
    for row in data:
        for i, col in enumerate(row):
            if type(col) is float:
                col_str = str(round(col,2))
            else:
                col_str = str(col)
            max_col_lengths[i] = max(len(col_str), max_col_lengths[i])

    col_underline = tuple('-'*l for l in max_col_lengths)

    def pad_col(value, col_num):
        # right justify numerical columns, left justify others
        col_type = col_types[col_num]
        col_length = max_col_lengths[col_num]
        if isinstance(value, float):
            fmt_str = f'%{col_length}.2f'
            return fmt_str % value
        elif isinstance(value, int) or col_type in (int, float): # int value or column header of number
            return str(value).rjust(col_length)
        else:
            return str(value).ljust(col_length)

    for row in [col_headers] + [col_underline] + data:
        list_of_cols = [pad_col(value, col_num) for col_num, value in enumerate(row)]
        print(' '.join(list_of_cols))


col_headers = ('Name', 'Type', 'Length')
fields = [(f.name, f.type, f.length) for f in arcpy.ListFields(parcels)]
print_aligned_columns(col_headers, fields)

# Task 3
print("\nTASK 3: Intersected Parcels")

# First, create a new layer and select the intersecting parcels
arcpy.MakeFeatureLayer_management(parcels,'parcels_lyr')
arcpy.SelectLayerByLocation_management('parcels_lyr', 'INTERSECT', powerline)

# Then create a cursor to extract the data about those parcels
rows = [row for row in arcpy.da.SearchCursor('parcels_lyr', ['SITUSADDR', 'SHAPE@AREA'])]
col_headers = ('SITUSADDR', 'AREA (sq ft)')
print_aligned_columns(col_headers, rows)

# Task 4
print("\nTASK 4: Create shapefile of parcels within 250 feet")

# Create a buffer in the in_memory workspace
# Using in_memory avoids writing to disk, speeding up processing and simplifying cleanup
buffer_path = 'in_memory\\powerline_buffer'
arcpy.Buffer_analysis(powerline, buffer_path, '250 feet')
arcpy.SelectLayerByLocation_management('parcels_lyr', 'WITHIN', buffer_path)
print(arcpy.GetCount_management("parcels_lyr"), 'parcels selected')

# Export the selected parcels to the output shapefile
arcpy.CopyFeatures_management('parcels_lyr', output_fc)

# alternative:
#arcpy.FeatureClassToFeatureClass_conversion('parcels_lyr', arcpy.env.workspace, output_fc)
