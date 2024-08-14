# This is main.py
"""
import math

num = float(input("Enter a number: "))
sq_root = math.sqrt(num)
cb_root = math.cbrt(num)
log_2 = math.log2(num)
print("The square root of",num,"is",sq_root)
print("The cube root of",num,"is",cb_root)
print("The logarithm base 2 of",num,"is",log_2)

log_num = int(input("Enter a number to calculate logarithm of: "))
# log_base = int(input("Enter the base of the log: "))
log_value_base = math.log(log_num)
print("The logarithm of",log_num,"to the given base is",log_value_base)

num_cube = int(input("Enter the number to calculate cube of: "))
cubed_num = num_cube ** 3
print("The cube of",num_cube,"is",cubed_num)
"""


apple = "Apple is a very tasty fruit"
print(apple)
print(id(apple))

# Coverting a string to uppercase using upper() method
upper_apple = apple.upper()
print(upper_apple)

lower_apple = apple.lower()
print(lower_apple)

name = "aRnAb MiTra"
print(name)

capName = name.capitalize()
print(capName)

fruit = "Mango is a very juicy fruit"
corr_fruit = fruit.replace("Mango","Pear")
print(corr_fruit)
print(corr_fruit[:8])

char_count = fruit.count("Mango",1,11)
print(char_count)

fruit_len = len(fruit)
print(fruit[:33])
print(fruit[:39])
print(fruit[1:11])
print(fruit,"is a string of",fruit_len,"characters")

arnab = 'He is a very good boy. He is 20 years old now'

ends_with_str = arnab.endswith("old now")
ends_with_pos = arnab.endswith("very good boy",8,21)
ends_with_pos = arnab.endswith("very good boy")
print(ends_with_str,type(ends_with_str))
print(ends_with_pos)
starts_with_str = arnab.startswith("very good boy")
print(starts_with_str)

# print(arnab[8:21])

contains_str = arnab.__contains__("good boy")
print(contains_str)

centered_arnab = arnab.center(55,"a")
print(centered_arnab,"The length of",centered_arnab,"is")
# Checking the length of the range object using len() function
# r = range(1,61)

# r_len = len(r)
# print("The length of the range object is",r_len)

lang = input("Enter a string: ")
swapped_lang = lang.swapcase()
print(swapped_lang)

# upper_str = input("Enter a string in uppercase: ")
# upper_check = upper_str.isupper()
# print(upper_check)

# lower_str = input("Enter a string in lower case: ")
# lower_check = lower_str.islower()

# print(lower_check)

# digits_str = input("Enter a string containing digits only: ")
# numeric_str = digits_str.isdigit()
# print(numeric_str)

# alpha_str = input("Enter a string containg alphabets: ")
# alpha_check = alpha_str.isalpha()
# print(alpha_check)

alnum_str = "1298AsErYu134875ItReNm7652"

alnum_verify = alnum_str.isalnum()
print(alnum_verify)

t = ("a","b","c","d","e","f")
print("|".join(t))

stat_items = ["Pen","Pencil","Notebook","Marker","Whiteboard","School bag"]
print(stat_items)
print("|".join(stat_items))

stud_marks = {
    "Arnab" : 89,
    "Vrinda" : 90,
    "Shaarav" : 87,
    "Gunraaj" : 78,
    "Maahi" : 80
}
separator = " and "
print(stud_marks)

mark_str = separator.join(stud_marks)
print(mark_str)

names = "Arnab,Vrinda,Shaarav,Gunraaj,Maahi,Khushi,Aditya"
names_list = names.split(",")
print(names_list,type(names_list))

boy = "I am a good boy kkkdkdk   "
print(boy)
print(len(boy))
rem_spaces = boy.rstrip(" ")
rem_spaces = boy.rstrip("kkkkkdk  ")
print(rem_spaces)
print(len(rem_spaces))

boy = "  I am a good boy"
print()
print(len(boy))
rem_spaces = boy.lstrip("  ")
print(rem_spaces)
print(len(rem_spaces))