 Lesson 02: Concatenation, Formatting, User Input, Connecting to Google Drive, Displaying Images .

 # string concatenation:  with  +  :  "Hey, " + first_name + "!" 
 # string formatting  instead of using  +  :  f"Hey, {first_name}!" 
 # input()  method provides text input box  
 # int(3.99)  method converts  3.99  to  3 .
 # float(4)  method convert  4  to a  4.0 .
 # str(3.14)  method converts  3.14  to string  "3.14"*.
 # format()  method provides options such as adding commas to numbers. It returns a string, so whereas 2500 is a number, "2,500" is a string
 import IPython.display  library to enable display of images


print()

# 3. Concatenate them into one string using +

print() # BrianMcClain

# 4. That worked, but we need a space. Concatenate it as " ":

print() # Brian McClain
- Concatenation cannot handle numbers. You get an error.
- Pass the number to the  str()  method to convert it to a string

# 5. Declare two vars: username and high_score

# no commas in numbers

# 6. Concatenate a greeting and run the cell--don't even print it. Just run it.
greeting = "Welcome"
#    We get an error, because concatenation does not acccept numbers.
# greeting = "Welcome back, " + username + "! Your high score is: " + high_score + "!"

# 7. The number causes an error, so comment out that bad line and do it again.
#    This time pass high_score to the str() method:
# method to turn it into a string
# "Welcome back, ! Your high score is " + str(high_score) + "!"
print(greeting)
 input()  method provides an editable text box

- The input argument is the text box instruction / label
- Set the input() method equal to a variable to capture the input
- The input is always a string--even if the user enters a number
- To convert "stringy number" to actual number, pass it to   int()  or  float() 
-  \n  before the label text separates label and input  onto two lines
- Nothing else runs in the program until the box is dismissed by hitting enter

# 8. Make First Name and Last Names inputs, each saved to a variable
# "First Name\n"
# "Last Name\n"
# "Welcome back, ! Your high score is !"
print(greeting)
  f" " string formatting instead of concatenation 
  
  For longer concatenations, all those  +  and  " "  can be a bit much.
-  f" "  (string formatting) requires no plus signs or quotes:
-  f" "  format converts numbers to strings automatically
-  f" "  has only one set of quotes around everything
-  f" "  requires  {}  around variables to distinguish them from string



"${:.2f}".format(price)  # returns a currency format
"{:,}".format(score)     # adds commas to a 4+ digit number
# 12. Add comma to number with .format() method, which is called on a formatting symbol:
# "{:,}"
print() # 12,500 <class 'str'>

# 13. Calculate a price that results in too many decimal places:
# 88.95
# 0.0875

print("Price of shoes:",)

# 14. Convert a long float into currency format:
# "${:.2f}"
print("Price of shoes:")
 connecting to Google Drive from Colab 
We have a coding challenge coming up, and for that we have an image to display. The image is in our class files images folder on  Google Drive , so we have to connect to Google Drive.
# 15. Connect to Google Drive:


# Upon success, it should say Mounted at /content/drive
# 16. Click the folder icon at right
# 17. Open the 'drive' folder, and then the 'MyDrive' folder
#     Then open your Python Bootcamp folder, and then the 'images' folder
# 18. Find "python-challenge-input-cafe-bill.jpg" and right click the file name
#     (or click the three little dots at right)
#     Choose "Copy path"
# 19. Paste the copied path between the quotes of the url variable below:
url = ""
 import the IPython.display module  so that we can display an image here in our Notebook.
# 20. Import IPython.display, which will allow us to display images:

# 21. Pass the url to the Image() method, set equal to an image object, which we'll call img.
#.    Print the data type of img. It's display.image

print('Image() data type:') # <class 'IPython.core.display.Image'>
# 22. Call the display() method, passing it the image object:

#     The "Calculating Restaurant Bill from User Input" image should appear.
# CHALLENGE:
# Refactor our restaurant bill program so that it accepts user input
# Provide input boxes for "Food $"", "Bev $"" and "Tip %":

# HINTS:
#.  Set the input() methods equal to variables to capture the input
#.  Convert to currency format when you print prices: "${:.2f}".format(price)
#.  Convert the inputted "stringy" numbers to actual numbers. Example:
food = "88.75" # This is how the input would be saved
print('food:', food, type(food)) # food: 55 <class 'str'>
food = float(food)
print('food:', food, type(food)) # food: 55 <class 'str'>
# These steps can be combined into one:
food = float("88.75")
print('food:', food, type(food)) # food: 55 <class 'str'>

# Do NOT provide an input for setting the tax pct. That value is hard-coded:
tax_pct = 8.875

# Here's the first input. Notice that the input is immediately converted from
# string to float in one nested move. The rest is up to you. You need inputs
# for bev and tip_pct. Then you need to do the math to calculate the bill.

# food = float(input("Food $"))

# A. Make the "Bev $" and "Tip %" inputs:
# "Bev $"
# "Tip %"

# B. Calculate the sub-total, which is just food plus beverage:
# 'Sub-total: "${:.2f}"

# C. Calculate the tax and tip amounts.
#    Divide by 100, because 8.875% = 0.0875
# / 100
# / 100

# D. Print currency formatted Tax and Tip for an itemized bill:
print('Tax:', "${:.2f}")
print('Tip:', "${:.2f}")

# E. Calculate and print the total:

print('Please Pay:', "${:.2f}")

# Example output:
# Food $88
# Bev $55
# Tip %18
# Sub-total: $143.00
# Tax: $12.69
# Tip: $25.74
# Please Pay: $181.43