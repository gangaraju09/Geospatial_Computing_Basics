# This program calculates the area of a triangle.  The base and height
# of the triangle are determined by user input.

print("This program finds the area of a triangle.")
print()

# Collect input from the user and make sure it is floating point
height = float(input("Please enter the height of the triangle: "))
base = float(input("Please enter the base length of the triangle: "))

# Calculate the area
area = 0.5 * height * base

# Display the area
print("The area of a triangle with height", height, "and base length of", base, "is", area, ".")
