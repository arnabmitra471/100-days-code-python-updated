# This is main.py
name = "Arnab"
friend = "Rohan"
another_friend = "Lovish"
print("My name is",name)
print("Hello, "+name)

apple = "He said ,\"I want to eat an apple\""
print(apple)

# Multiline strings

conv = '''
Hey I am good
How are you
I am fine and you
Everything is going fine
He said I want to eat an apple
'''
print(conv)

# string indexing - To access each character of a string we can refer to the indices

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # This throws an error

# Looping through a string

print("Let's use a for loop \n")
for char in name:
    print(char)

print("Let's use a for loop for the string apple \n")

for char in apple:
    print(char)

for letter in conv:
    print(letter)
