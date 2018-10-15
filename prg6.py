#6.	Python Program to Swap Two Variables

#input from user
x = input("Enter value of x: ")
y = input("Enter value of y: ")

print("The value of x before swapping is:",x)
print("The value of y before swapping is: ",y)

#create a temporary variable and swap the values
temp = x
x = y
y = temp

print("And now the value of x after swapping is:",x)
print("And of y after swapping is:",y)
