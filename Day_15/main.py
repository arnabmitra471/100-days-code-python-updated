# This is main.py

# x = int(input("Enter a value between 0 to 4: "))
# Using match case statement to check the value of x against several cases
"""
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
"""
# Providing options to the user for temperature conversion
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
# Taking input from the user as an integer for the choice
choice = int(input("Enter your choice: "))
# Writing a match statement with the respective cases and logic
match choice:
    case 1:
        temp = float(input("Enter a temperature value in fahrenheit: "))
        celsius = (temp - 32) * 5/9
        print("{0} degrees fahrenheit is {1} degree celsius".format(temp,celsius))
    case 2:
        temp = float(input("Enter a temperature value in celsius: "))
        fahrenheit = (temp * 9/5) + 32
        print("{0} degrees celsius is {1} degrees fahrenheit".format(temp,fahrenheit))
    case 3:
        temp = float(input("Enter the temperature in celsius: "))
        kelvin = temp + 273
        print("{0} degrees celsius is {1} kelvin".format(temp,kelvin))
    case 4:
        temp = float(input("Enter the temperature in kelvin: "))
        celsius = temp - 273
        print("{0} kelvin is {1} degrees celsius".format(temp,celsius))
    case _:
        print("Invalid choice")