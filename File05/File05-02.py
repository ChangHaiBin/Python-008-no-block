info = {
    "name": "Michael Tan",
    "age": 18,
    "height": 170
}

print("what do you want to know about the student?")
field = input()
value = info[field]
print(f"The student's {field} is {value}")
