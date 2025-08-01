# Loop control statement(For loops)

fruits = ["apple", "banana", "cherry", "date"]

# First loop: break when "cherry" is found
for fruit in fruits:
    if fruit == "cherry":
        break  # Exit the loop when "cherry" is found
    print(fruit)  # This will print "apple" and "banana"
print()

# Second loop: continue when "cherry" is found
for fruit in fruits:
    if fruit == "cherry":
        continue  # Skip the rest of the loop when "cherry" is found
    print(fruit)  # This will print "apple", "banana", and "date"
print()

for fruit in fruits:
    if fruit == "cherry":
        pass  # Do nothing when "cherry" is found
    print(fruit)  # This will print "apple" and "banana" only
    