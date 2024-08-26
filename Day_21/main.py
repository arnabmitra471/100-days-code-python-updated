# This is main.py

# n is a required argument to be passed in the factorial function
def factorial(n):
    fact = 1
    if n < 0:
        print("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        for i in range(1,n+1):
            fact *= i
        return fact

res1 = factorial(5)
res2 = factorial(10)
res3 = factorial(12)
res4 = factorial(13)

num = int(input("Enter a number to obtain its factorial: "))
res = factorial(num)
print("The factorial of {0} is {1}".format(num,res))
print(res1)
print(res2)
print(res3)
print(res4)

def average(n1,n3,n2=45):
    print("The average is",(n1 + n2 + n3)/2)

average(17,25)
average(34,98)
average(78,100)

# Default arguments passed while creating the function
average(43,23,198)

# Keyword Arguments - Python will identify the arguments passed by the parameter name
average(n3=67,n1=54)
average(n1=23,n2=98,n3=76)

# Variable length arguments

def calculate_mean(*args):
    total = 0
    n = len(args)

    for i in args:
        total = total + i
    mean = total/n
    return mean

nums = (34,86,98,12,65,45,18,20)
res5 = calculate_mean(*nums)
print(res5)

def print_name(**kwargs):
    print(type(kwargs))
    print(kwargs)

print_name(fname="Arnab",lname="Mitra")