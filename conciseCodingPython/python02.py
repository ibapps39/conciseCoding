# Ok, LET'S CODE! 
# For things to work with minimal overhead/installation, search for a 'Python sandbox'. Python has an official one.
# How might do you think you might tell a computer to "print" something to the screen?
# Well, we have a verb, print, and subject (something).
# In the spirit of tradition, let's print "Hello World!"
# In python, we actually just did the command! Except, we need to contain the subject.
print("Hello World!") 
# print is a function, like in math, () contains the  paramaters/input, and " " specifies a word is being passed
# Execute the above, and voila, you just wrote and executed a Python program. Off to some FAANG company right?!
# Note quite, but glad you're excited. Facebook Apple Amazon Netfelix and Google will have to wait.
# But hey, we're getting there :)

# Ok. I imageine the idea of functions and paramters is easy enough to grasp, but what about words? Numbers? 
# Other kinds of 'data'?
print("1")
# I printed a number right? No. We printed a word/string. 
# Words are known are strings (words are strings of characters, like 'a')
# A string or word is anything in quotes.
# Print number
print(1)
print(42)
# Print a character
print('a')

# Like in math, we have variables. Symbols we can give a value.
abc = 20
a = 2
# However, some predefined words, functions, and symbols, like numbers, can't be used as variables
# print = 0 wont work, but prinT does
prinT = 0
# Print a variable. The capitalization and _ aren't necessary unless using restricted word.
theMeaning_of_Life = 42
print(theMeaning_of_Life)

# What about something more ... abstract. Like true or false?
# Well, we still have binary for it. 0 = false, 1 = true.
# In Python we can do this in a couple of wayss
# Literally saying True or False. Captilization matters
yay = True
nay = False
# using numbers like in a function
if(0): print("False")
else: print("True")
# if and else are special, but think of the : as a variables = operator. : is "Do what's after this"
# In python, indentations, whitespace, matters! So the program knows 'if/else' is done after the end of the line

# Computers can save many different kinds of data, whether pictures or videos, 
# We call storage persistency, and the makeup of data can take various forms
# Take for example a photo, may be made up of pixels (the little red, green, and blue square in a monitor).
# In order to display a certain color, we pass a set of color ranges (some spectrum of red, green, and blue) using numbers
rgb = [100, 200, 150] 
# One kind of 'set' is an array, indicated by two brackets []
emptyArray = []
abcArray = ['a', 'b', 'c']
# Arrays are typically fixed in length, meaning the length doesnt change/isnt dynamic
# You can communicate with arrays by refering to an array using elements or indices
# Elements are the what we see in the array. 
# Index is 'where' the element is. Most languages assume the array starts left to right, and that
# the first element, like 'a', is an int = 0.
# SO: array[index] = element
# To print 'a' in abcArray we pass the array name, abcArray and the index of 'a' in brackets
print(abcArray[0])
# 0 since 'a' is the first element, which is almost always 0 (some languages start at 1, but Python doesnt)

# But what if we don't know how big an array will be? We can use a changing, or Dynamic, list?
# Well, in Python arrays are known as Lists, and use the array notation, or syntax.
#  

