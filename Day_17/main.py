# This is main.py
import time
name = "Arnab Mitra"
print(name)
for i in name:
    print(i)
    if i == "n" or i == "b":
        print("There is something special here")

'''
i = "A" -> print("A")
i = "r" -> print("r")
i = "n" -> print("n")
i = "a" -> print("a")
i = "b" -> print("b")
i = " " -> print(" ")
i = "M" -> print("M")
i = "i" -> print("i")
i = "t" -> print("t")
i = "r" -> print("r")
i = "a" -> print("a")
'''

colors = ["Red","Blue","Orange","Violet","Green","Yellow","Indigo","Fuschia","Firebrick","Cornflower blue"]
print(colors)

print(type(colors))

for color in colors:
    print(color)
    for i in color:
        print(i)
print()
for rev_color in range(len(colors)-1,-1,-1):
    print(colors[rev_color])

for i in range(51,0,-1):
    if i % 2 == 0:
        print(i)
        time.sleep(1.5)
    else:
        print("It is an odd number")

# for k in range(5):
#     print(k + 1)

for k in range(1,21,3):
    print(k)

print("Using a decrementing loop")

for l in range(21,0,-2):
    print(l)