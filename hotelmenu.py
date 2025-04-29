# Define the menu of the restaurant
menu = {
    'Dal Tadka': 120,
    'Paneer Butter Masala': 150,
    'Egg Curry': 170,
    'Chicken Masala': 200,
    'Fish Curry': 220,
    'Mutton Curry': 280
}


# Greet the customer
print("Welcome to Samadhan")
print("Dal Tadka: Rs 120\nPaneer Butter Masala: Rs 150\nEgg Curry: Rs 170\nChicken Masala: Rs 200\nFish Curry: Rs 220\nMutton Curry: Rs 280")

order_total = 0

# First order
item_1 = input("What would you like to have: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, the item '{item_1}' is not available.")

# Check if customer wants to order more
another_order = input("Would you like to order anything else? (Yes/No): ")
if another_order.lower() == "yes":
    item_2 = input("What would you like to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, the item '{item_2}' is not available.")

# Final bill
print(f"The total amount of your order is Rs {order_total}.Thank you for visiting!")
