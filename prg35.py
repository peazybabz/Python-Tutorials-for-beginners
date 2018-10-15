#35.	Python Program to Convert Decimal to Binary Using Recursion

#Decimal number is converted into binary by dividing
# the number successively by 2 and printing
# the remainder in reverse order.

#define a function

def convertToBinary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number/ you can change the number
dec = 14

convertToBinary(dec)