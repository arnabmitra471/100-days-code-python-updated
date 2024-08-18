# This is main.py
# Taking inputs for the apple price and the budget
applePrice = int(input("Enter the apple price: "))
budget = int(input("Enter your budget: "))

if (budget - applePrice > 50):
    print("Alexa add 1 kg apples to the cart")
    print("Please buy some more groceries")
else:
    print("Alexa don't add apples to the cart")

print("Done")

# Program to check whether an year is a leap year or not
# year = int(input("Enter a year: "))

# if year % 100 == 0 and year % 4 == 0:
#     print("It is a century leap year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("It is a normal leap year")
# else:
#     print("It is not a leap year")

# num = int(input("Enter a number: "))

# if num % 2 == 0 and num % 3 == 0:
#     print(num,"is divisible by 2 and 3")
# elif num % 2 == 0 and num % 3 != 0:
#     print(num,"is divisible by 2 but not by 3")
# else:
#     print("The number is not divisible by 2 and 3")

# print(num/3) # This is the normal division operator. This always gives a floating point quotient
# print(num//3) # This is the floor division operator. This removes the floating point part and gives the integer quotient

num = int(input("Enter a number: "))

print(num > 18)
print(num < 18)
print(num >= 18)
print(num <= 18)
print(num == 18)
print(num != 18)
if num > 0:
    print("The number is positive")
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")

age = int(input("Enter your age: "))

if age > 18:
    result = "You can drive"
else:
    result = "You cannot drive"

print(result)

# Ternary operator in python
res = "age cannot be negative, or zero or something too high" if age <= 0 or age >= 200 else "Your age is a valid one"
print(res)

result = "You can drive" if age > 18 else "You cannot drive"
print(result)

marks = [32,56,87,98,98,98,34,78,32,90,76,100,123,156,187,198,200]
mark = int(input("Enter an element: "))

if mark not in marks:
    print("The element does not exist in the list")
else:
    print("The element exists in the list")