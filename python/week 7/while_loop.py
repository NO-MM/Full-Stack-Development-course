#While loops
# A while loop in Python repeatedly executes a block of code as long as a specified condition is true.

#using while loop to count from 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1  # Increment the count by 1

#Loop control statement in while loop

count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  # Exit the loop when count is 3
   