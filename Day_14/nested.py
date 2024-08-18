num = int(input("Enter a number: "))

if num < 0:
    print("The number is negative")
elif num > 0:
    if num < 10:
        print("The number is less than 10")
    elif num >= 10 and num <= 20:
        print("The number lies between 10 and 20")
    elif num > 20 and num <= 40:
        print("The number lies between 20 and 40")
    elif num > 40 and num <= 50:
        print("The number lies between 40 and 50")
    else:
        print("The number is not in the specified range")
else:
    print("The number is zero")
