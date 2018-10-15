#39.	Python Program to Check Whether a String is Palindrome or Not

#A palindrome is a string which is same read forward or backwards.

# change this value for a different output
my_str = 'peep'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print(my_str,"is palindrome")
else:
   print(my_str,"is not palindrome")
