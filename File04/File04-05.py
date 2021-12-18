
durations = {
    1: "1 day",
    2: "2 hours",
    3: "15 minutes"
}

print("Welcome to the Computer Store. How can we help you?")
print("1. Computer Repair")
print("2. Software Installations")
print("3. Software Upgrades")
user_select = int(input(">> "))

duration = durations[user_select]
print(f"This task will take {duration}")
