#8.	Python Program to Convert Kilometres to Miles

#input provided by program
# kilometers = 5.3

#input from user
kilometers = float(input("Enter value in kilometers:"))

#conversion factor
conv_fac = 0.621371

#calculate miles
miles = kilometers * conv_fac

print("%0.2f kilometers is equal to %0.2f miles"%(kilometers,miles))