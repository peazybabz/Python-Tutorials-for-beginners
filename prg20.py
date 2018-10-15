#20.	Python Program to Find Armstrong Number in an Interval

#take input from the user
lower = int(input("Enter your lower range: "))
upper = int(input("Enter your upper range: "))

for num in range(lower, upper + 1):

        #order of number
        order = len(str(num))

        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)
