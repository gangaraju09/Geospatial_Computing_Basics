# This program calculates the area of a trapezoid or a triangle depending on the user choice.
# The dimensions of the shape are determined by user input.
import sys
print("This program finds the area of a trapezoid or a triangle.")
print()

#Determine whether to calculate triangle or trapezoid.
response=input("Please enter 'triangle' or 'trapezoid' to determine which area you wish to calculate. ")

if response=='trapezoid':
    # Collect input from the user
    cnt = 0
    while True:
        cnt += 1
        try:
            height = float(input("Please enter the height of the trapezoid: "))
            base = float(input("Please enter the base length of the trapezoid: "))
            top = float(input("Please enter the top length of the trapezoid: "))

            # Calculate the area
            area = 0.5 * height * (base + top)

            # Display the area
            print("The area of a trapezoid with height", height, ", base", base,"and top",top, "is", area, ".")

            break
        except:
            if (cnt >= 4):
                sys.exit(1)
            print("Invalid input. Try again!")


elif response=='triangle':
    # Collect input from the user
    cnt = 0
    while True:
        cnt += 1
        try:
            height = float(input("Please enter the height of the triangle: "))
            base = float(input("Please enter the base length of the triangle: "))

            # Calculate the area
            area = 0.5 * height * base

            # Display the area
            print("The area of a triangle with height", height, "and base", base, "is", area, ".")

            break
        except:
            if (cnt >=4):
                sys.exit(1)
            print("Invalid input. Try again!")


else:
    print("Not a shape that this program can calculate!")
