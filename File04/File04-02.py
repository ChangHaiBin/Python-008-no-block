# Dictionary
menu = {
    "Burger": 7,
    "Pizza": 8,
    "Salad": 6
}

print("What do you like to order?")
order = input()
price = menu[order]
print(f"Your order of {order} costs ${price}")

