fruits = ['apple', 'mango', 'peach', 'papaya', 'pear', 'plum', 'apricot', 'lime',
          'banana', 'blueberry', 'cherry', 'kiwi', 'lemon', 'papaya', 'pineapple'
          'apple', 'mango', 'peach', 'papaya', 'pear', 'plum', 'apricot', 'lime',
          'banana', 'blueberry', 'cherry', 'grape', 'kiwi', 'lemon', 'papaya',
          'apple', 'mango', 'peach', 'papaya', 'pear', 'plum', 'apricot', 'lime',
          'banana', 'blueberry', 'cherry', 'kiwi', 'lemon', 'papaya', 'pineapple']
p_fruits = []
for idx, fru in enumerate(fruits):
    if fru[0].upper()== "P" or fru[0].upper() == "L":
       p_fruits.append(fru)

print(p_fruits)