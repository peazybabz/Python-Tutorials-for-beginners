#4.	Python Program to Calculate the Area of a Triangle

print('Now we will calculate the Area of a Triangle\n')

#Take input from user
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

#calculate the semi-perimeter
s = (a + b + c)/ 2
print("The perimeter is ",s)

#calculate the area
area = (s*(s-a)*(s-b)*(s-c))** 0.5

print("The area of the triangle is %0.2f"%area)

