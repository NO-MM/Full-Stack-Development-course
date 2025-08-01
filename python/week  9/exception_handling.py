
'''
# This code snippet is for calculating the area and perimeter of a rectangle
# using functions from a separate module called calculate.py.    

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")
'''

'''
# This code snippet is for calculating the area and perimeter of a rectangle
# using functions from a separate module called calculate.py.

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
'''

try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Everything went wrong")
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
