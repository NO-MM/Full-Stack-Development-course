#Sets
'''
my_set = {1, 2, 3, 4, 5}  # Creating a set with unique elements
print(my_set)  # Printing the set

my_set.add(6)  # Adding an element to the set
print(my_set)  # Printing the set after adding an element

my_set.remove(3)  # Removing an element from the set
print(my_set)  # Printing the set after removing an element
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union of two sets
union_set = set1.union(set2)
print(union_set)  # Printing the union of two sets

# Intersection of two sets
inter_set = set1.intersection(set2)
print(inter_set)  # Printing the intersection of two sets

# Difference of two sets
diff_set = set1.difference(set2)
print(diff_set)  # Printing the difference of two sets