
# Set is a completely different data structure, such that:
# If you attempt to add duplicates of the same element to that "Set"
# It will ignore your request.
numbers = set()
numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(1)
numbers.add(1)
numbers.add(1)
numbers.add(3)
numbers.add(3)
numbers.add(2)
numbers.add(2)
numbers.add(2)

print(numbers)
print("===========")
print(3 in numbers)
