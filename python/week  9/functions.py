#Writting Functions in Python

'''
def greet(name):
    print(f"Hello, {name}")
    
greet("Alice")  # Calling the function with an argument

def add(a, b):
    return a + b  # Returning the sum of two numbers

result = add(2, 5)
print(result)  # Printing the result of the addition

'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call to calculate factorial
    
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")  # Function with a default parameter
    
greet("Bob", "Good morning")  # Calling the function with a name

