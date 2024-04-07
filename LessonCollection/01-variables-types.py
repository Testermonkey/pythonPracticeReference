""" 
multi-line comments
    can go from line to line 
"""

# single line comment
a = 3.14 #single line comment can also follow code

my_string = "hello"  # Strings need to be in quotes
my_string = 'hello'  # quotes can be single or double
my_num = 123         # numbers create int
my_num = 123.4       # a decmial value will create a float
my_num = int("345")  # casting a string to int
my_num = float("345")# casting to float
my_bool =  True    # bool only have 
complex_txt = 'there\'s an issue with using single quotes' 
#  \ is an control char used to display the single quote
#  Other control characters
#  \' 	Single Quote 	
#  \\ 	Backslash 	
#  \n 	New Line 	
#  \r 	Carriage Return 	
#  \t 	Tab 	
#  \b 	Backspace 	
#  \f 	Form Feed 	
#  \ooo 	Octal value 	
#  \xhh 	Hex value
print("methods always have parentheses") # but the parentheses dont always require values
print("\nprints whats in the quotes and  \\n makes it print on a new line")
print(f"formated printing  {my_bool} {my_num} {my_string}")
#print("Favorite Fruit:", my_string)
my_num = 123.456 
print(f"round to 2 places; {round(my_num, 2)}")
print(type(my_num)) # <class 'float'>
fruits =['apple', 'banana', 'cherry', 'grape', 'kiwi', 'lime', 'mango', 'orange', 'peach']
print('fruits:' '\ntype:', type(fruits), '\nlength:', len(fruits)) #fruits: type: <class 'list'> length: 9
print('first:',fruits[0], '\nlast:', fruits[-1]) # apple peach
nums = [3,5,8,13,21,34]
print('\nnums:', nums, '\ntype:', type(nums), '\nlength:', len(nums))
print('second:', nums[1], '\nlast:',nums[-2] ) # 5 21
fruits = ['apple', 'banana', 'cherry', 'grape', 'grapefruit', 'kiwi', 
          'lemon', 'lime', 'mango', 'orange', 'peach', 'pear', 'plum', 'papaya']
