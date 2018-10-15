#43.	Python Program to Count the Number of Each Vowel

# string of vowels
vowels = 'aeiou'

# take input from the user
ip_str = input("Please enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels, 0)

# count the vowels
for char in ip_str:
    if char in count:
        count[char] += 1

print(count)