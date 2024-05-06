# This is main.py

# Modules and pip in python

import json


students = '''
{
    "name": "Arnab",
    "age" : 19,
    "programming languages" : ["Java","Python","Javascript"],
    "has friends": true
}
'''
print(students)


parsed_str = json.loads(students)

print(parsed_str)

print(type(parsed_str))

data = {
    "name": "Arnab",
    "age" : 19,
    "programming languages" : ["Java","Python","Javascript"],
    "has friends": True
}
print(data)

parsed_data = json.dumps(data)
print(parsed_data)
