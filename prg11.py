#11.	Python Program to Check if a Number is Odd or Even

# A number is even if division by 2 give a remainder of 0.
# If remainder is 1, it is odd number.

num  = int(input('Enter any number: '))

if num % 2 ==0:
    print(num," is an Even Number")
else:
    print(num," is an Odd Number")