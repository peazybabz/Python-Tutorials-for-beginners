#28.	Python Program to Find Factors of Number

#take input from user
num = int(input("Enter a number: "))
# define a function
def print_factors(x):

   # This function takes a number and prints the factors
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

print_factors(num)
