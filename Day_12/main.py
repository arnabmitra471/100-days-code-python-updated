# This is main.py

apple = "An apple a day keeps the doctor away"

print(apple)

name = "Arnab Mitra"
print(name)

# Accessing the characters of a string

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
# print(name[11])

# String slicing
names = "Arnab,Shubham,Rohan,Vrinda"
print(names[0:5])
print(names[6:13])
print(names[0:5])

namesLen = len(names)
print(namesLen)

print("The length of",name, "is",len(name))

fruit = "Mango is a sweet and delicious fruit"
# Slicing syntax string[start:end]
print(fruit[1:8])
print(fruit[1:8])
print(fruit[1:8])
print(fruit[1:16])
print(fruit[0:13])
print(fruit[:13])
print(fruit[:len(fruit)])
# Negative slicing

# print(len(fruit))
# print(fruit[:-3])
# print(fruit[:len(fruit)-3])
print(fruit[-3:-1])

'''
len(fruit) = 36 -3 = 33 36-1 = 35
33:35
'''
'''
nm = "Harry"
print(nm[-4:-2])
len(nm) -4 = 5 - 4 = 1 | len(nm) - 2 = 3
'''
nm = "Harry"
print(nm[-4:-2])
