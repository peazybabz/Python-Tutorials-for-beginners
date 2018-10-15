#5.	Python Program to Solve Quadratic Equation

#solve the quadratic equation ax**2 + bx + c = 0

#import complex math module
import cmath


a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)
#find two solutions

soln1 = (-b-cmath.sqrt(d))/2*a
soln2 = (-b+cmath.sqrt(d))/2*a

print("The solutions of the quadratic equation are: ",soln1,"and",soln2)
