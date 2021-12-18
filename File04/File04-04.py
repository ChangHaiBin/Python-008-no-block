# Dictionary
menu = {
    "Burger": 7,
    "Pizza": 8,
    "Salad": 6
}

# This is OK
order = "Hotdog"
if order in menu:
    price = menu[order]
    print(f"Your order of {order} costs ${price}")
else:
    print(f"I don't understand your order of {order}")
