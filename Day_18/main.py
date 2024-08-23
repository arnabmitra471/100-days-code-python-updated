# This is main.py

# While loops in python

count = 10

while count >= 1:
    print(count)
    count -= 1
else:
    print("I am inside else")


i = int(input("Enter a number: "))
print(i)

while i <= 100:
    i = int(input("Enter a number again: "))
    print(i)

print("We are outside the while loop now")