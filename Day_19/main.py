# This is main.py

# break statement
num = int(input("Enter the number: "))
for i in range(1,21):
    if i == 10:
        break
    print("{0} X {1} = {2}".format(num,i,num*i))

print("Broken out of the loop")

"""
for c in range(1,9):
    print(c)
    for d in range(1,8):
        if d == 6:
            break
        print(d)
"""
# continue statement
for n in range(1,21):
    if n % 2 != 0:
        print("Skipping the iteration")
        continue
    print(n)

print("Skipped the iterations for even numbers")

# Emulating a do while loop in python

while True:
    user_inp = int(input("Enter a number >= 100 to break out of the loop: "))
    print(user_inp)
    if user_inp >= 100:
        break

