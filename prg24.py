#24.Python Program to Convert Decimal to Binary, Octal and Hexadecimal

#A number with the prefix '0b' is considered binary, '0o' is
# considered octal and '0x' as hexadecimal

#take input from user
dec = int(input("Please enter a value: "))

print("The decimal value",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")
