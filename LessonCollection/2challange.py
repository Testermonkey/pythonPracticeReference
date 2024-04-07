# CHALLENGE:
# Given this list of cars:


# PART 1:
# Use a for loop and the enumerate() method to output the cars numbered from 1-9:
# 1. Ford (For Sale: Mazda)
# 2. BMW --SOLD
# etc.
# 8. Ferrari
# 9. Nissan
cars = ['Ford', 'BMW', 'Mazda', 'Mercedes', 'Chevy', 'Toyota', 'Audi', 'Ferrari', 'Nissan']
for idx, car in enumerate(cars):
    print(f" car :{idx +1}  {car}")
    if idx % 2 == 0:
        print(f"{car} --Sold!") #sold
    else:
        print(f"For Sale:{car}") #for sale

# A. Loop the cars list, using enumerate to have access to the index as well as the item:
# for
  # B. Print the index +1 followed by the car:
    print(f" car : {car}  {idx}")

# PART 2:
# output pairs of cars:
# if the list index is odd, print the car preceded by "For Sale:" (For Sale: Mazda)
# if the list index is even, print the car followed by "-- SOLD!" (Mercedes -- SOLD!)

print()

# B. Loop the cars using enumerate:
# for
# C. If the index is odd, it yields a remainder of 1 when divided by 2:
# if
# D. Print the "For Sale" message:
print('For Sale: ')
# E. Else the index is even, so output the "SOLD" message:
# else
print('-- SOLD!')

# example output:
# 1. Ford-Nissan
# 2. BMW-Ford
# 7. Audi-Nissan

print()