menu = ["Burger", "Pizza", "Salad"]

print("What would you like to order?")
user_select = input()

if user_select in menu:
    print(f"Yes, we serve {user_select} in our restaurant")
else:
    print(f"No, we do not have {user_select}, please choose something else.")
