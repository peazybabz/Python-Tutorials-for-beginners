#14.	Python Program to Check Prime Number

a = int(input("Enter your number: "))

k = 0

for i in range(2, a//2+1):
    if(a % i == 0):
        k = k + 1
if(k <= 0):
    print(a,"is a Prime number:")
else:
    print(a,"is not a Prime number:")
