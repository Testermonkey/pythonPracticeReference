# # CHALLENGE:
# # Refactor our restaurant bill program so that it accepts user input
# # Provide input boxes for "Food $"", "Bev $"" and "Tip %":

# # HINTS:
# #.  Set the input() methods equal to variables to capture the input
# #.  Convert to currency format when you print prices: "${:.2f}".format(price)
# #.  Convert the inputted "stringy" numbers to actual numbers. Example:
# #food = "88.75" # This is how the input would be saved
# print('food:', food, type(food)) # food: 55 <class 'str'>
# food = float(food)
# print('food:', food, type(food))
# # food: 55 <class 'str'>
# # These steps can be combined into one:
# #food = float("88.75")
# food = float(input("Food $"))
# print('food:', food, type(food)) # food: 55 <class 'str'>

# # Do NOT provide an input for setting the tax pct. That value is hard-coded:
# tax_pct = 8.875

# # Here's the first input. Notice that the input is immediately converted from
# # string to float in one nested move. The rest is up to you. You need inputs
# # for bev and tip_pct. Then you need to do the math to calculate the bill.

# # food = float(input("Food $"))

# # A. Make the "Bev $" and "Tip %" inputs:
# # "Bev $"
# # "Tip %"

# # B. Calculate the sub-total, which is just food plus beverage:
# # 'Sub-total: "${:.2f}"

# # C. Calculate the tax and tip amounts.
# #    Divide by 100, because 8.875% = 0.0875
# # / 100
# # / 100

# # D. Print currency formatted Tax and Tip for an itemized bill:
# print('Tax:', "${:.2f}")
# print('Tip:', "${:.2f}")

# # E. Calculate and print the total:

# print('Please Pay:', "${:.2f}")

# # Example output:
# # Food $88
# # Bev $55
# # Tip %18
# # Sub-total: $143.00
# # Tax: $12.69
# # Tip: $25.74
# # Please Pay: $181.43

food = float(input("Food $"))
bev = float(input("Bev $"))
tip = float(input("tip $"))
tax_pct = 8.875
subtotal = food + bev
tax = subtotal * (tax_pct / 100)
total = subtotal + tax + tip
print('Subtotal $', round(subtotal, ndigits=2))
print('Please Pay $', round(total, ndigits=2))