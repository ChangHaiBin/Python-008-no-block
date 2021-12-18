# Dictionary
menu = {
    "Burger": 7,
    "Pizza": 8,
    "Salad": 6
}

# The search term "Burger", "Pizza", "Salad" are the "keys" to the dictionary
# The corresponding output (7, 8, 6) are called the values.

# We have multiple "key-value" pairs.
# (key="Burger", value=7)
# (key="Pizza", value=8)
# (key="Salad", value=6)

# Python "in" keyword checks only the "key", not the value
print("Burger" in menu)
print("Hotdog" in menu)

print("==========")
# It does not check the prices/values.
# In fact, in other languages, the code below may potentially fail!
print(7 in menu)
print(8 in menu)