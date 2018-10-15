#34.	Python Program to Find Factorial of Number Using Recursion

#define a function
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n * factorial(n-1))

#take input from user
n = int(input("Enter a number:"))
print("The Factorial of",n,"is",factorial(n))

