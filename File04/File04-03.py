# Dictionary
menu = {
    "Burger": 7,
    "Pizza": 8,
    "Salad": 6
}

# The code below will fail!
order = "Hotdog"
price = menu[order]
print(f"Your order of {order} costs ${price}")

