#12.	Python Program to Check Leap Year

# To get year (integer input) from the user
# year = int(input("Enter a year: "))
year = 2012

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(year," is a leap year")
       else:
           print(year," is not a leap year")
   else:
       print(year,"is a leap year")
else:
   print(year," is not a leap year")
   