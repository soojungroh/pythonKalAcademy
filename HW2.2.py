#prompt user to input radius
radius = eval(input("What is the radius of the cylinder?: "))

#prompt user to input length
length = eval(input("What is the length of the cylinder?: "))

#constant
PI = 3.14159265

#compute area
area = radius * radius * PI

#compute length
volume = area * length

#Display result
print ("The area of the cylinder is", area , "and the volume is", volume)
