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
    for count in range(num,0,-1):
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
