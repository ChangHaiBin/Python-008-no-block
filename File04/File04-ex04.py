# WARNING: Actual Password system is much more sophisticated than this!
# This is just a simple example.
# Do NOT actually implement your password system this way!
passwords = {
    "Henry": "Password999",
    "Joseph": "Birthday0831",
    "Kelvin": "HDBApartmentNumber7"
}

print("Who is using the computer?")
user = input()

print("What is your password?")
password = input()

# Similar to previous example:
# Depending on what is the user's input,
# Print out the following info for different cases:
#     "This user doesn't exist in our system"
#     "Password incorrect. Please try again"
#     "Password confirmed. Welcome back {user}"
