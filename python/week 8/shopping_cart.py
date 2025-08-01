#Creating a shopping cart that will continuesly ask the user for food product and the price of the product
#Have an edit clause if the user wishes to stop adding more thing to their cart
#At the end show the food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input ("Enter a food to to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("------ YOUR CART ------")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price
    
    print(f"\n")
print(f"Total cost: R{total}")
        
    