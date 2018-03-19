# A Python list is similar to an array in other languages. 
#How to create an empty list

my_list = []
my_list = list()

my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "Python", 5]

my_nested_list = [my_list, my_list2]
print(my_nested_list)

# Combining two lists using the extend method

combo_list = []
one_list = [4,5]
combo_list.extend(one_list)
print(combo_list)