
cereal_list = ["Franken Berry", "Count Chocula", "Yummy Mummy", "Chucky Harms",
               "Frute Brute", "Boo Berry", "Scream of Wheat", "Cap'n Creep"]

new_list = [] # to hold the new names in a list
vowels = "AEIOUY"

# iterate over the cereal_list, each value is temporarily stored to 'wd'

for wd in cereal_list:
    print(wd) # print out each element

    # to check which characters are vowels, use an inner for loop
    new_string = ""

    # lowercase word to begin with
    for ch in wd.lower():

        # check which characters are vowels
        if ch.upper() in vowels:
          # add upper case character to our new string
          new_string += ch.upper() # shorthand for: new_string = new_string + ch.upper()
        # leave any other string alone , just copy it over
        else:
          new_string += ch
        
        print(new_string) # print out to see each step of the way how we are adding characters 

    print(new_string)
    new_list.append(new_string)

print("new list ", new_list )


# CHALLENGE  with the list below, save a the strings in a list that start with p or l. 
# EXTRA: display the counts of each element. 

fruits = ['apple', 'mango', 'peach', 'papaya', 'pear', 'plum', 'apricot', 'lime',
          'banana', 'blueberry', 'cherry', 'kiwi', 'lemon', 'papaya', 'pineapple'
          'apple', 'mango', 'peach', 'papaya', 'pear', 'plum', 'apricot', 'lime',
          'banana', 'blueberry', 'cherry', 'grape', 'kiwi', 'lemon', 'papaya',
          'apple', 'mango', 'peach', 'papaya', 'pear', 'plum', 'apricot', 'lime',
          'banana', 'blueberry', 'cherry', 'kiwi', 'lemon', 'papaya', 'pineapple']
p_fruits = []
for fru in enumerate(fruits):
    if fru[0]== "P":
       p_fruits.append(fru)

print(p_fruits)
    
