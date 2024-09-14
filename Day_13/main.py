name = "!!!Arnab!!!!!!!!!!!"
name_upper = name.upper()
name_lower = name.lower()

# finding the length of a string
print("The length of {} is {}".format(name,len(name)))

print()
print(name[0])
print(name[1])

# This is not possible since strings are immutable

# name[0] = "P"
print(name)
print(name_upper)
print(name_lower)

print(name.rstrip("!"))
print(name.strip("!"))

apple = "An apple a day keeps the doctor away apple"
print(apple.replace("apple","orange"))

print(apple.split(" "))

blog_heading = "introduction To JS"
cap_heading = blog_heading.capitalize()
print(cap_heading)

s1 = "Welcome to the console!!!"
print("The length of",s1,"is",len(s1))
centered_str = s1.center(50,"0")
print(centered_str)
print(len(centered_str))

apple_count = apple.count("apple")
print(apple_count)

print(s1.endswith("!!!",3,10))

print(s1[3:10])

s2 = "123AbCdEFGh"
print(s2.isalnum())

s3 = "abcdIu12 344"
print(s3.isalpha())

lang = "PYThon IS AN INterPRetED LanGUAGE"
print(lang.isupper())

lower_lang = lang.lower()
print(lower_lang)
print(lower_lang.islower())

print(lang.swapcase())
print(lang.title())