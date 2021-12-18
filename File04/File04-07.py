# This dictionary only has words/strings as the "key" of the dictionary.
menu = {
    "Burger": 7,
    "Pizza": 8,
    "Salad": 6
}
print(menu["Burger"])
print(menu["Pizza"])
print(menu["Salad"])

print("==============================")


# This dictionary below has all sorts of data as the "key" of the dictionary
# e.g. string/word, integer, boolean/true/false
strange = {
    "Burger":  7,
    100:       "Lobster",
    True:      "Complicated"
}

# Python allows such flexibility/strangeness.
# Other languages do not.
# Try not to write code this complicated.

# Very confusing
print(strange["Burger"])
print(strange[100])
print(strange[True])


print("==============================")
# In fact, Python also allows you to create a list of mixed items
# Please be careful/avoid using such strange data structures.
strange_collections = [3.14159, "Mathematics", False, ["Another list", "inside another list"]]
for x in strange_collections:
    print(x)
