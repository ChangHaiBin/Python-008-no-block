
# Similar to the previous file, but now we save the list of students into a file.

# Write a simple program, such that
# when the user has typed in one of the student's name
#     print "{student} is in our classroom"
# else:
#     print "There is no such person in our classroom named {student}"

with open("students.txt", "r") as f:
    students = f.read().splitlines()

# Change to Lower case
students = [student.lower() for student in students]

print("Please type in a student's name")
check = input().lower()    # Auto switch to lower case.
