# calculate Area by choosing Triangle or Trapezoid

#(with this 4th input, code will ask which geo_shape would like to calculate area )
geo_shape = input('Enter a shape to calculate area - triangle/trapezoid:')

# here in 8th input code, code will compare with entered geo_shape input and if geo_shape is trapezoide then it calculates area of trapezoid
# if function is used to check whether to run given program rule or not, if code successfuly passes then it will execute if or execute else statement
if geo_shape =='trapezoid':
    #here in 10th,11th,12th line the code will ask to enter top width value and bottom width value and height value
    a=float(input('Enter value of top width W1: '))
    b=float(input('Enter value of bottom width W2: '))
    h=float(input('Enter value of height h: '))
# now code will calculate area of trapezoid with given formula in 14th line of code
    trapezoid_area=((a+b)/2)*h
# print is used to display output of the line between the print brackets 
    print("Area of Trapezoid with width W1:",a,",width W2:",b,"and height:",h,"is",trapezoid_area,".")

# if we enteres geo_shape is traiangle, it will calculate are of triangle form the else function and then gives result in print statement
else:
# here in 21st and 22nd code, it will ask input for height and length    
    h = float(input("Please enter the height of the triangle: "))
    b = float(input("Please enter the base length of the triangle: "))
# now code will calculate with given inputs with give area of triangle formula 
    triangle_area= 0.5*b*h
    print("Area of a traiangle with Base:",b,"and Height:",h, "is", triangle_area, ".")
