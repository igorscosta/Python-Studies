########### How To Create a String ###############

# Strings in Python can be created using single, double or triple quotes

my_string = "Welcome to Python!"
another_string = 'The bright red fox jumped the fence.'
a_long_string = '''This is a multi-line string. 
It covers more than one line'''

#The triple quote line can be done with three single quotes or three double quotes.


my_string = "I'm a Python programmer!"
other_string = 'The word "python" usually refers to a snake'
triple_string = """Here's anothe way to embed "quotes" in a string"""

#Using the str method
my_number = 123
my_string = str(my_number)

############## String Concatenation ###############

string_one = "My dog ate"
string_two = "my homework!"
string_three = string_one + string_two

############# String Methods ################

my_string = "This is a string!"
print(my_string.upper())
print(my_string.lower())
print(dir(my_string))

#Introspection allows you to ask Python about itself
print(help(my_string.rpartition))
print(type(my_string))


