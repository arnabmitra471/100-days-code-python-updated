# This is main.py

# While loops in python
"""
count = 100

while count >= 1:
    print(count)
    count -= 1
else:
    print("I am inside else")
"""
""" 
i = int(input("Enter a number: "))
print(i)

while i <= 100:
    i = int(input("Enter a number again: "))
    print(i)
else:
    print("We are outside the while loop now") 
"""

# Sum of first n natural numbers using while loop

""" 
n = int(input("Enter the number of terms: "))

count = 1
total = 0

while count <= n:
    total += count
    count += 1

print("The sum of the first",n,"natural numbers is",total) 
"""


num = int(input("Enter a number: "))
rev = 0

temp = num
while num > 0:
    last_digit = num % 10 # calulate the last digit
    rev = rev * 10 + last_digit # multiply 10 with the reversed number and add the last digit
    num //= 10 # remove the last digit

print("The reversed number is",rev)

if rev == temp:
    print(temp,"is a palindrome number")
else:
    print(temp,"is not a palindrome number")


num = int(input("Enter the number: "))

fact = 1
if num < 0:
    print("Factorial doesn't exist for negative numbers")
elif num == 0:
    print("The factorial is",fact)
else:
    for count in range(1,num+1):
        fact *= count
    print("The factorial of the number is",fact)


n = int(input("Enter the number of terms: "))
t1 = 0
t2 = 1

if n == 1:
    print(t1)
else:
    print(t1)
    print(t2)
    for _ in range(1,n+1):
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(t3)


# Infinite while loop
while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            celsius = float(input("Enter the temperature value: "))
            fahrenheit = (celsius * 9/5) + 32
            print("{} degree celsius is {} degree fahrenheit".format(celsius,fahrenheit))
        case 2:
            fahrenheit = float(input("Enter the temperature value: "))
            celsius = (fahrenheit - 32) * 5/9
            print("{} degree fahrenheit is {} degree celsius".format(fahrenheit,celsius))
        case 3:
            celsius = float(input("Enter the temperature value: "))
            kelvin = celsius + 273
            print("{} degree celsius is {} kelvin".format(celsius,kelvin))
        case 4:
            kelvin = float(input("Enter the temperature value: "))
            celsius = kelvin - 273
            print("{} kelvin is {} degree celsius".format(kelvin,celsius))
        case 5:
            break
        case _:
            print("Invalid choice. Please select a valid option")
