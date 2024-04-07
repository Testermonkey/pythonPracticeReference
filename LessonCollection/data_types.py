import math

# String data type

# Literal assignmet
first = 'Dave'
last = 'Gray'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
pizza = str("Peperoni")

# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concationation
full_name = first + " " + last
print(full_name)

full_name += "!"
print(full_name)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s"
print(statement)

# Multiple lines
multiline = """
Hey, how are you?

I was just checkiing in
                        All god

"""

print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at \\located'
print(sentence)

# String Methods
print (first.lower())
print (first.upper())
print (first)

print(multiline.title())
print(multiline.replace("god", "ok"))

print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a string menu

title =  "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffen".ljust(16, ".") + "$1".rjust(4))
print("Cheese Cake".ljust(16, ".") + "$1".rjust(4))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Coffee".ljust(16, ".") + "$1".rjust(4))

# String Index Values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("z"))

# Numeric data types

price = 100
best_pirce = int(80)
print(type(price))
print(isinstance(best_pirce, int))

# float type
gpa = 3.28
y = float(1.4)
print(type(gpa))

# Complex type
comp_value = 5 + 3j
print(comp_value)

print(abs(gpa))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number

zipcode = "1000001"
zipcode = int(zipcode)
print(zipcode)