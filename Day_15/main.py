# This is main.py

x = int(input("Enter a value between 0 to 4: "))

match x:
    case 0:
        print("Case is 0")
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 3:
        print("Case is 3")
    case 4:
        print("Case 4")
    case _ if x != 90:
        print(x,"is not 90")
    case _ if x != 80:
        print(x,"is not 80")
    case _:
        print("Invalid value entered. Please enter a valid value")