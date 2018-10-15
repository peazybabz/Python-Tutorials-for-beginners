#31.	Python Program to Display Calendar

# Python program to display calendar of given month of the year

# import module
import calendar

#uncomment if you want to take input provided by the program
#yy = 2017
#mm = 9

# To ask month and year from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
