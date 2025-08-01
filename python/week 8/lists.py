
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Accessing the first element

fruits[1] = "blueberry"  # Modifying the second element
print(fruits)  # Printing the modified list

fruits.append("date")  # Adding a new element to the end of the list
print(fruits)  # Printing the list after appending

fruits.insert(1, "kiwi")  # Inserting a new element at index 1
print(fruits)  # Printing the list after inserting

fruits.remove("date")  # Removing the first occurrence of "banana"
print(fruits)  # Printing the list after removing

fruits.sort()  # Sorting the list in ascending order
print(fruits)  # Printing the sorted list

fruits.sort(reverse=True)  # Sorting the list in descending order
print(fruits)  # Printing the list sorted in descending order