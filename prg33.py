#33.	Python Program to Find Sum of Natural Numbers Using Recursion

def recur_sum(n):
   """Function to return the sum
   of natural numbers using recursion"""
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# uncomment to take input from the program/ you can change this value for a different result
#num = 16

#take input from the user
num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))