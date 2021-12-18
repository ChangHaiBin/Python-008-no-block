numbers = [2, 4, 6, 8, 10]

x = 4
y = 5

print(x in numbers)
print(y in numbers)

# Although there is the "__contains__" function
# It is never used directly this way
print(numbers.__contains__(x))
print(numbers.__contains__(y))