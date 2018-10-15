#21.Python Program to Find the Sum of Natural Numbers

#  take input from the user so as to display
# the sum of natural numbers up to that number.
num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until it becomes zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)
