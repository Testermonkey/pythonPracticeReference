# Challange
import random
import string
# get ascii lowercase letters (a-z)
lower_case_letters = string.ascii_lowercase

# randomly selecting 100 indicies that correspond to letters above
rng = range(0, len(lower_case_letters) - 1)

rand_indicies = [random.randint(0,25) for i in range(100)] # 0,25 

random_selected_letters = []

for idx in rand_indicies:
        # add each letter to the randomly selected letters list
    random_selected_letters.append(lower_case_letters[idx])

unique_chars = set(random_selected_letters)
letter_counts =[]
letters_ = []

for lett in random_selected_letters:
    letter_counts.append(random_selected_letters.count(lett))
    letters_.append(lett)

print(letter_counts)
print(letters_)    

print(random_selected_letters)
#instance counter


random_selected_letters = set(random_selected_letters)
random_selected_letters = list(random_selected_letters)
print(random_selected_letters)


#new code from instructor

import string
import pprint

# get ascii lowercase letters (a-z)
lower_case_letters = string.ascii_lowercase

# randomly selecting 100 indicies that correspond to letters above
rng = range(0, len(lower_case_letters) - 1)
rand_indicies = [random.randint(0,25) for i in range(100)] # 0,25 

random_selected_letters = [] 
for idx in rand_indicies:
    # add each letter to the randomly selected letters list
    random_selected_letters.append(lower_case_letters[idx])
unique_letters = set(random_selected_letters)
letter_counts = []
for lett in unique_letters:

    # count each unique letter and save it to a list called letter_counts
    letter_count = random_selected_letters.count(lett)
    # letter_counts.append([lett, letter_count])
    letter_counts.append((lett, letter_count)) # using tuple instead of a list


pprint.pprint(letter_counts)
list(zip([1,2,3],['a','b','c'])) 

# tuple example: stripped down version of a list
tup_ = (1,2) # round parenthesis for a tuple
lst = [1,2] # square brackets for a list 

#tup_[0] = 1 # this will throw an error because tuples are immutable and cannot be changed 
lst[0] = 1