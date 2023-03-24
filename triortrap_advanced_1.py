# write a code which will ask to choose shape between triangle or trapezoid with input value error checking
# 3rd input will ask to choose shape between triangle or trapezoid
geo_shape = input('Enter a shape to calculate area - triangle/trapezoid:')
# now write if conditon to execute area of triangle or area of trapezoid based on prevoius input
# if entered shape is compared to trapezoid then create a while function to avoid errors in input values
if geo_shape =='trapezoid':
# creat how many times does the code repaat untill the correct values are given
 loopCount = 0
 while loopCount<4:
    loopCount += 1
# now give inputs to ask value =s required to calculate trapezoid
    a=input('Enter value of top width W1: ')
    b=input('Enter value of bottom width W2: ')
    h=input('Enter value of height h: ')
# now give input to convert given values into float datatypes
    try:
      a=float(a)
      b=float(b)
      h=float(h)
#if all given values are successfuly converted into float values then calculate the area of trapezoid
      trapezoid_area=((a+b)/2)*h
      print("Area of Trapezoid with width W1:",a,",width W2:",b,"and height:",h,"is",trapezoid_area,".")
# give break to while loop to donot repeat the function
      break
#donot give break to while loop, if given values are not converted ito float
    except:
        print('please enter a value which can convert into float')
# if the shape is requested other than trapezoid then write else statement to calculate area of triangle
else:
# creat how many times does the code repaat untill the correct values are given
    loopCount = 0
    while loopCount<4:
       loopCount += 1
# now give inputs to ask value is required to calculate triangle
       h = input("Please enter the height of the triangle: ")
       b = input("Please enter the base length of the triangle: ")
# now give input to convert given values into float datatypes
       try:
           b=float(b)
           h=float(h)
#if all given values are successfuly converted into float values then calculate the area of triangle
           triangle_area= 0.5*b*h
           print("Area of a traiangle with Base:",b,"and Height:",h, "is", triangle_area, ".")
# give break to while loop to donot repeat the function
           break
#donot give break to while loop, if given values are not converted ito float
       except:
           print('please enter a value which can convert into float')
           