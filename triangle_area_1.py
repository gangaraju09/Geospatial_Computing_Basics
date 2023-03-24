# This program calculates the area of a triangle.

# [This line will execute the line in 4th input and shows output as This program finds the area of a triangle. ]
print("This program finds the area of a triangle.")
print()

# [when we execute 8th and 9th input code this will ask us to enter the height of the traingle and base lenght of the triangle ]
height = float(input("Please enter the height of the triangle: "))
base = float(input("Please enter the base length of the triangle: "))

# [after giving height and base values, the 12th input code will calculate area with 0.5*height*base]
area = 0.5 * height * base

# [now with 15th input code it will display the line as output as The area of a triangle with height (value entered), and base (value entered is area(calculated value of area).)]
print("The area of a triangle with height", height, "and base", base, "is", area, ".")
