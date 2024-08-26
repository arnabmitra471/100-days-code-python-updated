# This is main.py

def calculate_gmean(n1,n2,n3,n4):
    gmean = (n1 * n2 * n3 * n4)**1/4
    print("The geometric mean of the numbers is",gmean)

def is_greater(a,b):
    if a > b:
        print("First number is greater")
    elif a == b:
       print("Both the numbers are equal")
    else:
        print("Second number is greater")

def is_lesser(n1,n2):
    if n1 < n2:
        print(n1,"is lesser")
    elif n1 == n2:
        print("Both the numbers are equal")
    else:
        print(n2,"is lesser")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

calculate_gmean(num1,num2,num3,num4)
calculate_gmean(43.43,87.98,21.43,54.23)
calculate_gmean(43.98,89.90,56.76,123.876)

is_greater(num1,num2)
is_greater(num3,num4)
is_lesser(num1,num2)
is_lesser(num3,num4)