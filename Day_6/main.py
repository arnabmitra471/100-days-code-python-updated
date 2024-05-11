# This is main.py

# variables and data types

# Note: In python everything is an object
a = 123 + 231j
print(a)

num1 = 8 - 2j
b = "Arnab"
print(b)

c = True
print(c)
d = None
print(d)
print(a + num1)
# Determining the data type of a variable

comp1 = complex(10,12)
print(comp1)

"""
Sequence data types:
1) list
2) tuple
3) range
"""

l1 = [56,32,98,98,54,78,79,90]
print(l1)

fruits = ["Apple","Banana","Mango","Pear",67,98,90,90]
fruits_tup =  ("Apple","Banana","Mango","Pear",67,98,90,90)
print(fruits)
print(fruits_tup)
print("The type of a is",type(a))
print("The type of num1 is",type(num1))
print("The type of b is",type(b))
print("The type of c is",type(c))
print("The type of d is",type(d))
print("The type of l1 is",type(l1))
print("The type of fruits is",type(fruits))
print("The type of fruits_tup is",type(fruits_tup))

students = {"name":["Arnab","Sanya","Shubham","Harry"],
            "marks" : [89,78,90,80],
            "isProgarammer" : True
            }
print(students)
print(type(students))