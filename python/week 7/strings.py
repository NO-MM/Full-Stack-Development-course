#strings

#message = """bob's worlds 
#is cool"""

#print(message)

#Advanced string formatting

#Print first letter of the string and the second letter and last letter.
message = ' Hello, world! '
#print(message[0])
#print(message[1])
#print(message[-1])

#How long is the string?
#print(len(message))  # prints the length of the string
print(len(message)) 
#using strip
print(message.strip())  # removes leading and trailing whitespace
# using lower
print(message.lower())  # converts to lowercase
#using split
print(message.split(','))  # splits the string into a list of words
#using upper
print(message.upper())  # converts to uppercase
#using replace
print(message.replace('world', 'Python'))  # replaces 'world' with 'Python'
