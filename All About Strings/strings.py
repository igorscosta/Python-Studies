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

################ String Slicing ##################

my_string = "I like Python!"
print(my_string[0:1])
print(my_string[:1])
print(my_string[0:12])
print(my_string[0:13])
print(my_string[0:14])
print(my_string[0:-5])
print(my_string[:])
print(my_string[2:])

#Access individual characters in a string via indexing
print(my_string[0])


################# Stting Formating #################

#The old way

my_string = "I like %s" % "Python"
print(my_string)

var = "cookies"
new_string = "I like %s" % var
print(new_string)

another_string = "I like %s and %s" % ("Python", var)
print(another_string)
# You have to pass the same number of strings to the arguments

# integers and floats
my_string = "%i + %i = %i" % (1, 2, 3)
print(my_string)

float_string = "%f" %(1.23)
print(float_string)

float_string2 = "%.2f" % (1.23)
print(float_string2)

float_string3 = "%.2f" % (1.237)
print(float_string3)


#The new way (templates)
print("%(lang)s is fun!" % {"lang" : "Python"})

print("%(value)s %(value)s %(value)s !" % {"value" : "SPAM"})

print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2, "z":3})

#Using string's format method!
print("Python is as simple as {0}, {1}, {2}".format("a", "b", "c"))

print("Pythos is as simple as {1}, {0}, {2}".format("a", "b", "c"))

xy = {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy))