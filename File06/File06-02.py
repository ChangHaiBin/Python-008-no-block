items = [
    {
        "description": "Bread",
        "price": 2.99,
        "type": "FOOD"
    },
    {
        "description": "Paper Plates",
        "price": 2.49,
        "type": "NON-FOOD"
    },
    {
        "description": "Cheese",
        "price": 4.99,
        "type": "FOOD"
    },
    {
        "description": "Tissue Paper (5 pack)",
        "price": 1.00,
        "type": "NON-FOOD"
    },
]

food_item_prices = [
    item["price"]
    for item in items
    if item["type"] == "FOOD"
]

subtotal = sum(food_item_prices)
print(f"The total price for all FOOD item is {subtotal}")

