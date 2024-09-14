# This is main.py
"""
marks = [11,67,94,87,98,12,38,98,76,43,"Arnab",True,False,True,True,False,33,98]

print(marks)
print(type(marks))

# Indexing a list
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

fruits = ["Apple","Orange","Banana","Pineapple","Pear","Jackfruit"]
print(fruits)

print(fruits[0])

print(marks[-3]) # Negative index
print(fruits[-3])

for mark in marks:
    print(mark)

print()
n = len(marks)
for i in range(n-1,-1,-1):
    print(marks[i])

for fruit in fruits:
    print(fruit)
print("Printing the elements of the list in reverse order")
for rev_fruit in range(len(fruits)-1,-1,-1):
    print(fruits[rev_fruit])

element = input("Enter an element in the fruits list: ")
print(type(element))

if element in fruits:
    print("Yes !! The fruit is present")
else:
    print("No!! The fruit is not present")

name = "Arnabarry"

if "arry" in name:
    print("Yes")
else:
    print("No")

fruit = input("Enter an element which is not in the fruits list: ")

if fruit not in fruits:
    print("The element is not present in the list")
else:
    print("The element is indeed present in the list")

# List slicing

print(marks[:])
print(marks[1:10])
print(marks[2:11])
print(marks[1:-1])
print(marks[1:17:2])
print(marks[1:9:3])
"""

# List comprehension

nums = [i for i in range(4)]
print(nums)

squared_nums = [j **2 for j in range(100) if j % 2 == 0]
print(squared_nums)

names = ["Milo","Sarah","Bruno","Amnatasia","Rosa"]
names_with_o = [name for name in names if "o" in name]
print(names)
print(names_with_o)

names_with_o = [name for name in names if len(name) > 4]
print(names_with_o)