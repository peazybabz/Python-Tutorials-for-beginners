#26.Python Program to Find HCF or GCD
#The highest common factor (H.C.F) or greatest common divisor (G.C.D)
#  of two numbers is the largest positive integer that perfectly divides the two given numbers.

# define a function
def computeHCF(x, y):
    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1, "and", num2, "is", computeHCF(num1, num2))
