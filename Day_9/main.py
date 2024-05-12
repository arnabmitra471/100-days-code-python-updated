# This is main.py

# Explicit type casting - Done by the programmer himself for converting one data type to another
num1 = int("27")
num2 = int("22")
print("The sum of the numbers is",num1 + num2)

# Two types of typecasting
"""
1. Explicit typecasting
2. Implicit typecasting
"""

#implicit type casting - Python converts a lower order data type into higher order data type to prevent data loss

num3 = 87.12
num4 = 25
res = num3 + num4
print("The type of num3 is",type(num3))
print("The type of num4 is",type(num4))
print("The sum of num3 and num4 is",res)
print("The type of res is",type(res))

n5_bin = bin(num2)
print(n5_bin)
print("The type of n5_bin is",type(n5_bin))
hex_n5 = hex(num2)
print("The hexadecimal representation of",n5_bin,"is",hex_n5)