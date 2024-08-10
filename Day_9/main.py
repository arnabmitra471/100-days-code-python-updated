# Two types of typecasting

"""
Implicit type casting
Explicit type casting
"""

num1 = 34 # implicit type casting 34 -> 34.0 + 12.6 = 46.6
num2 = 12.6
res = num1 + num2
print("The sum is",res)
print("The type of res is",type(res))


a = "61"
b = "56"
print("The sum of",int(a),"and",int(b),"is",int(a) + int(b))

num3 = "90"
num4 = "18761543"
print(num3,type(num3))
print(num4,type(num4))

int_num3 = int(num3)
int_num4 = int(num4)

print(int_num3,type(int_num3))
print(int_num4,type(int_num4))

num3_bin = bin(int_num3)
num3_oct = oct(int_num3)
num4_oct = oct(int_num4)
print(num3_bin)
print(num3_oct)
print(num4_oct)

num5 = 671879871
oct_num5 = oct(num5)
print("The type of num5 is",type(num5))
print(oct_num5,type(oct_num5))

# num6 = "7590"
# print(bin(num6)) This thows an error since num6 is a string and it cannot be interpreted as an integer

num3_int = int(num3_bin,2)
print(num3_int,type(num3_int))

num5_hex = hex(num5)

print(num5,"in hexadecimal is",num5_hex)
num4_hex = hex(int_num4)
print(int_num4,"in hexadecimal is",num4_hex)

name = "Arnab"
# print(int(name))
# print(hex(name)) This throws an error as str cannot be interpreted as an integer